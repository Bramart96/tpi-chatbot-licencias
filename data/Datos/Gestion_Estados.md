# Gestión de Estados del Chatbot

| Estado              | Descripción                                                     |
| ------------------- | --------------------------------------------------------------- |
| ESTADO_INICIAL      | Muestra mensaje de bienvenida e inicia la conversación          |
| ESPERANDO_LEGAJO    | Espera el ingreso del número de legajo                          |
| VALIDANDO_EMPLEADO  | Verifica la existencia del empleado en la base de datos         |
| ESPERANDO_DIAS      | Espera la cantidad de días de vacaciones solicitados            |
| VALIDANDO_DIAS      | Verifica que la cantidad ingresada sea numérica y mayor a cero  |
| CONSULTANDO_SALDO   | Consulta el saldo de vacaciones disponible                      |
| SOLICITUD_APROBADA  | Actualiza saldo, registra la operación y notifica la aprobación |
| SOLICITUD_RECHAZADA | Registra el rechazo y notifica el motivo correspondiente        |
