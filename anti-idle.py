import threading
import time
import random
from dataclasses import dataclass
from typing import Optional, Tuple

import pyautogui
from pynput import keyboard

# --------- CONFIG (edit as you like) ---------
CLICK_INTERVAL_SECONDS = 45         # how often to click
JIGGLE_ENABLED = True               # do a small move to avoid idle
JIGGLE_PIXELS = 4                   # max jiggle distance (±)
RETURN_TO_ORIGINAL_POS = True       # go back to where the cursor was before clicking
MOUSE_BUTTON = "left"               # "left", "right", or "middle"
# ---------------------------------------------

pyautogui.FAILSAFE = True   # move mouse to any corner to raise FailSafeException
pyautogui.PAUSE = 0.05

@dataclass
class State:
    running: bool = False
    target_pos: Optional[Tuple[int, int]] = None
    stop_event: threading.Event = threading.Event()
    worker_thread: Optional[threading.Thread] = None

state = State()

def pick_position():
    pos = pyautogui.position()
    state.target_pos = (pos.x, pos.y)
    print(f"[INFO] Target set to: {state.target_pos}")

def toggle_running():
    if state.target_pos is None:
        print("[WARN] No target set. Press Ctrl+Alt+P while hovering the desired spot to set one.")
        return

    state.running = not state.running
    if state.running:
        print("[INFO] Anti-idle started. Press Ctrl+Alt+S to stop, Ctrl+Alt+Q to quit.")
        state.stop_event.clear()
        state.worker_thread = threading.Thread(target=worker, daemon=True)
        state.worker_thread.start()
    else:
        print("[INFO] Anti-idle paused.")
        state.stop_event.set()
        # thread will naturally end on next loop tick

def quit_program():
    print("[INFO] Quitting…")
    state.running = False
    state.stop_event.set()
    # give the worker a moment to exit cleanly
    time.sleep(0.2)
    raise SystemExit

def safe_move(x: int, y: int, duration: float = 0.0):
    # Wrapper in case you want to add extra guards later
    pyautogui.moveTo(x, y, duration=duration)

def small_jiggle():
    if not JIGGLE_ENABLED:
        return
    dx = random.randint(-JIGGLE_PIXELS, JIGGLE_PIXELS)
    dy = random.randint(-JIGGLE_PIXELS, JIGGLE_PIXELS)
    pyautogui.moveRel(dx, dy, duration=0.05)

def do_click_at_target():
    if state.target_pos is None:
        return

    # Remember current mouse location
    current = pyautogui.position()

    try:
        # Jiggle a bit (optional)
        small_jiggle()

        # Move to target & click
        safe_move(state.target_pos[0], state.target_pos[1], duration=0.05)
        pyautogui.click(button=MOUSE_BUTTON)

    finally:
        # Return cursor if desired
        if RETURN_TO_ORIGINAL_POS:
            safe_move(current.x, current.y, duration=0.05)

def worker():
    # Runs until stop_event is set
    next_time = time.time()
    while not state.stop_event.is_set():
        now = time.time()
        if now >= next_time:
            try:
                if state.target_pos is None:
                    print("[WARN] Target cleared. Pausing.")
                    state.running = False
                    break
                do_click_at_target()
            except pyautogui.FailSafeException:
                print("[ALERT] PyAutoGUI failsafe triggered (mouse hit a screen corner). Stopping.")
                state.running = False
                break
            except Exception as e:
                print(f"[ERROR] {e}")

            next_time = now + CLICK_INTERVAL_SECONDS

        # Sleep a tiny bit to keep CPU low and keep hotkeys responsive
        time.sleep(0.05)

    # mark stopped
    state.running = False

def main():
    print("=== Anti-Idle Clicker ===")
    print("• Hover over desired spot, press Ctrl+Alt+P to set target.")
    print("• Ctrl+Alt+S to start/stop. Ctrl+Alt+Q to quit.")
    print(f"• Interval: {CLICK_INTERVAL_SECONDS}s | Button: {MOUSE_BUTTON} | Jiggle: {JIGGLE_ENABLED} (±{JIGGLE_PIXELS}px)")
    print("• Safety: move mouse to a screen corner to trigger PyAutoGUI failsafe.")

    # Global hotkeys
    hotkeys = {
        "<ctrl>+<alt>+p": pick_position,
        "<ctrl>+<alt>+s": toggle_running,
        "<ctrl>+<alt>+q": quit_program,
    }

    with keyboard.GlobalHotKeys(hotkeys) as h:
        h.join()

if __name__ == "__main__":
    main()
