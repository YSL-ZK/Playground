# TASKS

## Atrys

### Done

- [X] En el subformulario de creación de proyectos se guardan actividades relacionadas con los proyectos, en la plantilla que me manden, generar una función/widget que les permita por ejemplo cuando se haga la creación del proyecto, las actividades se crean antes y se seleccionan para cada proyecto especifico. Cada actividad, tiene subactividades, debe haber una forma de trackear el proceso total, dependiendo de la cantidad de actividades y subactividades que hayan.

### To-Do

- [ ] Crear plantilla mail merge en zoho sign o zoho writer (dinamico a partir de campos del zoho crm) a partir de un documento base. Realizar la función deludge o el sistema que integre esa plantilla desde Zoho Sign al crm, de forma que cuando un cliente pase de fase, se recuperen los campos del modulo, y se envie a firmar el documento, esto se creo que se podria hacer con un workflow, luego, ver lo de notificaciones saleSignals o algo que ayude para que cuando el documento sea firmado, se cambie: el estado del contrato y se adjunte como un campo adicional. Se debe crear un registro en el modulo casos cuando este firmado (Este despues cambiara a llamarse Seguimientos Proyecto) (En Pausa)

### Notes

- No se volvió a comentar nada sobre la implementación de la plantilla mail merge.

---

## Yalitech

### Done

- [X] Realizamos hasta el 7° sprint del proyecto, según lo planeado y documentado en el repositorio de GitHub y en figma.

### To-Do

- [ ] Corregir: Flujos en todas las pestañas, errores de lint, consistencia en las interfaces, módulo de equipos con web-storage.

### Notes

- Yalitech congeló el proyecto.

---

## CBRE

### To-Do

- [ ] Revisar el documento, revisar en que momento se envía el contrato, verificar si se puede integrar dentro de Zoho Sign con un webhook o en Zoho Flow.

### Notes

- No se volvió a comentar nada sobre esta integración.

---

## GSE

### Done

- [X] Realizar un bot que cuando el cliente ingrese el NIT, se haga una búsqueda en el crm para verificar si es cliente nuevo o viejo.
- [X] Ver si se puede añadir una opción para que se le pide el numero del ticket, se bsuque ese ticket en desk y se retorne el estado en el bot de aulapp.
- [X] Integrar la API de GSE con el Zobot para buscar estado de solicitudes con el numero de documento.
- [X] Se corrigieron todos los flujos de los siguientes bots: GSE, Aulapp, Letmi Ecuador y Panamá.

### Notes

- Esta pendiente de integrar la API de whatsapp.
- Credenciales API:
  - <https://gse-ecd-corecertification-pre.gse.com.co/auth/login-app-user>
  - <consultacertificados631@gmail.com>
  - lQ.K!&2L93Ot

---

## RISK

### Done

- [X] Agregar una sección llamada formato de anuncio en el módulo de cuentas con los campos que faltan del documento.
- [X] Crear en el CRM una plantilla mail merge dinámica basada en el documento que recoja los datos de estos campos.
- [X] Hacer que cuando se convierta en cuenta, se pase la ultima propuesta a la cuenta nueva que se acaba de crear. Agregar otra casilla en la plantilla y mapearla en la función, que sea Descuento aplicado a la propuesta.
- [X] Se realizaron bastantes ajustes que Erika propuso por correo, como cambios en la plantilla, en el orden de los datos y en la información específica.


### To-Do

- [ ] Restaurar / Recrear la plantilla de Propuesta Comercial 3 que se eliminó.
- [ ] Hacer que los formularios que tienen en su pagina web de WordPress envíen información a Marketing Automation, esto se hace reemplazando en WordPress los formularios que tienen con los del plugin de ZMA y las credenciales que me llegaron al correo.

### Notes

- Se está a la espera de la información para los formularios de WordPress.
- Ellos no han pagado bolsa de horas para realizar el resto de los requisitos que comentó por correo.

---

## ASIA

### To-Do

- [ ] Corregir el traslado de datos de Facebook con Zoho Social a Zoho CRM que llegan incompletos.

### Notes

- Pendiente de respuesta por parte del cliente.

---

## AspenView

### To-Do

- [ ] Arreglar la función actual para que los correos que se envíen desde el botón se guarden en el módulo de email-logs correctamente.

### Notes

- Cancelado por el cliente.

---

## DataWifi

### Done

- [X] Se implementó la integración de correos electrónicos enviados desde Zoho CRM para el seguimiento de una reunión.

### Notes

- Se realizó con la ayuda de Sebas.

---

## WWB

### To-Do

- [ ] Entender y reestructurar las funciones actuales y tener una reunión para determinar que está fallando.

---

## Gardelo

### Done

- [X] Se corrigieron varios errores en la implementación del formulario de Agente Motor dentro de la plataforma de Zoho Sites, lo cual estaba evitando el envío de datos a Zoho CRM.
  
### Notes

- El cliente comenta algunos errores más pero no hemos tenido reunión para aclararlos.

---

## Lais Same

### Done

- [X] Se crearon canvas y reglas de trabajo para la gestión de módulos dentro del CRM 

### Notes

- Se hizo con ayuda de Santi Velez.

---

## Gerenciar

### To-Do

- [ ] Conectar Sinco ERP con Zoho CRM para la creación automatica de documentos de firma con información combinada de ambas plataformas a través de Zoho Sign.

### Notes

- Se tuvo una reunión donde se habló de esta integración, se propusieron soluciones y se quedó pendiente de una reunión con Sinco ERP para comentar endpoints y posibilidades.
  
---

## Orion

### Done

- [X] Se les configuró varias encuentas en Zoho Survey de forma que se integren bien con Zoho CRM y estén alineadas esteticamente.
- [X] Se les conectó Zoho CRM con Meta Suite para la gestión de Leads provenientes de formularios.

### Notes

- Aún están decidiendo si quieren una implementación en Zoho SalesIQ.

---

## Casapropia

### Done

- [X] Se corrigió el flujo del bot Eva con código dentro de Zoho SalesIQ.
- [X] Se creó el bot sin código MarIA para las integraciones con WhatsApp, Facebook Messenger y otras herramientas de Zoho.
- [X] Se modificó y arregló las notificaciones por correo electronico con respecto a la regla que determina los Bonos.
- [X] Se corrigieron unos Workflows que estaban duplicando correos de notificación a Anderson con respecto a la creación de conversiones.
- [X] Se crearon dos funciones que revisan cuando un posible cliente es verdaderamente nuevo o es un tipo de recontacto, en ese caso se configuraron reglas de prioridad de datos, notificaciones y plantillas de correo.

---

## PMO

### Done

- [X] Se realizó una integración entre Zoho CRM y Zoho Projects para la creación automática de proyectos al momento de que una oportunida pase al estado de ganado, asociando también las tareas y los documentos correspondientes.

### Notes

- Se realizaron contactos con soporte debido a la falta de endpoints para la asociación de documentos específicos al proyecto.

---
## Paynet

### Done

- [X] Se creó un widget para el seguimiento de actividades como tareas, llamadas y eventos con recordatorios que permite la edición, creación y eliminación de actividades desde el mismo widget.

### Notes

- Se están realizando ajustes con respecto a los últimos comentarios de Zulma.

---

## Incomelec

### Done

- [X] Se realizó una actualización masiva de tickets de Zoho Desk para corregir su área de cierre con respecto a reglas y busquedas de correos y palabras especificas.

### Notes

- Se realizó con la ayuda de Santi Velez.

---

## UMECIT

### Done

- [X] Se reestructuró completamente el bot dentro de Zoho SalesIQ para que esté mas acorde a la plantilla y datos que ellos esperan, además de corregir errores y mejorar la experiencia del usuario e implementar el flujo comercial.

### To-Do

- [ ] Se necesita implementar el bot con tarjetas de Chatgpt para la caracterización de leads y puntajes en tiempo real.
  
---

## Colpatria

### Done

- [X] Se creó un formulario en Zoho Forms, el cual está integrado con Zoho CRM para la recolección de datos de clientes potenciales.

---

## GSH

### Done

- [X] Se migraron módulos desde Salesforce hasta ZCRM para que los registros lleguen con toda su información relacionada.

---

## PROYECTO DE PRACTICA

### Done

- [X] Se creó y entregó un prototipo inicial del bot que realiza busquedas multiplataforma (Zoho CRM, Zoho Desk y una API externa) para el seguimiento de tickets, reuniones, facturas y datos del cliente.

### To-Do

- [ ] Desarrollar en Zoho Cliq y Zoho People una conexión que permita que se muestre el tiempo de conexión de las personas que trabajen en remoto. Explorar los permisos y los espacios de desarrollador de las dos plataformas y las conexiones e integraciones.

- [ ] Seguir mejorando el bot para que sea más amigable y útil.

---
