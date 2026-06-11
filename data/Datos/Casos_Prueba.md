# Casos de Prueba

| Caso  | Entrada                          | Resultado Esperado                                        |
| ----- | -------------------------------- | --------------------------------------------------------- |
| CP-01 | Legajo inexistente               | Mostrar error y solicitar nuevamente el legajo            |
| CP-02 | Texto en lugar de número de días | Mostrar error y solicitar nuevamente la cantidad          |
| CP-03 | Días negativos                   | Mostrar error y solicitar nuevamente la cantidad          |
| CP-04 | Días igual a cero                | Mostrar error y solicitar nuevamente la cantidad          |
| CP-05 | Saldo insuficiente               | Rechazar solicitud y notificar motivo                     |
| CP-06 | Saldo suficiente                 | Aprobar solicitud, actualizar saldo y notificar resultado |
