 # TPI — Chatbot Gestión de Licencias
## Organización Empresarial | UTN — Tecnicatura Universitaria en Programación

Simulador de consola para gestión de solicitudes de licencias y vacaciones,
desarrollado como Trabajo Práctico Integrador de la materia Organización Empresarial.

---

## Equipo
| Integrante | Usuario GitHub | Rol |
|---|---|---|
| Integrante 1 | braianmartinez | Desarrollo principal |
| Integrante 2 | bramart96 | Revisión y base de datos |

---

## Estructura del repositorio

tpi-chatbot-licencias/
├── src/Python/          → Código fuente del simulador
├── data/Base_Datos/     → Archivo Excel y diseño de base de datos
├── data/Datos/          → Diccionario de datos, gestión de estados y casos de prueba
├── docs/BPMN/           → Diagrama de proceso (Bizagi Modeler)
├── docs/Maquina_Estados/→ Diagrama de máquina de estados
├── requirements.txt     → Dependencias del proyecto
└── README.md            → Documentación del proyecto

---

## Tecnologías utilizadas
- Python 3
- openpyxl — lectura y escritura del archivo Excel
- pandas — procesamiento de datos
- Google Colab — entorno de desarrollo y versionado
- GitHub — control de versiones
- Jira — gestión de tareas (proyecto: CHATBOT-VACACIONES-UTN)
- Bizagi Modeler — modelado de procesos BPMN

---

## Gestión del proyecto — Jira
| Issue | Descripción | Responsable |
|---|---|---|
| CVU-1 | Crear repositorio e inicializar estructura | P1 |
| CVU-2 | Configurar entorno Colab y GitHub | P1 |
| CVU-3 | Modelar proceso BPMN | P1 |
| CVU-4 | Diseñar máquina de estados | P1 |
| CVU-5 | Diseñar estructura de datos y base de datos | P2 |
| CVU-6 | Desarrollar simulador Python | P1 |
| CVU-7 | Revisión y aprobación mediante Pull Request | P2 |
| CVU-8 | Integración final y documentación técnica | P1 |

---

## Decisiones técnicas
- Se utilizó `os.system()` en lugar de comandos `!git` directos para tener
  control programático sobre los resultados, verificar el output de cada
  operación y evitar la exposición de credenciales en el historial del notebook.
- El token de GitHub se almacenó como secreto en Google Colab mediante
  `userdata.get()`, sin exposición en ningún archivo ni historial de commits.
- Cada celda del notebook incluye un docstring explicando su propósito,
  el participante responsable y el issue de Jira asociado, garantizando
  trazabilidad completa del proceso de desarrollo.
- Se implementó una celda de reconexión al inicio del notebook que restaura
  las variables de entorno y clona el repositorio si la sesión de Colab
  fue reiniciada. Esto resuelve el problema de pérdida de variables entre
  sesiones, evitando commits vacíos y errores por variables no definidas.
---

## Inconsistencias documentadas

### 1. Autoría de commits en GitHub
Los commits se encuentran correctamente identificados con el integrante
responsable en el mensaje de cada uno (sufijo — P1 o — P2). Sin embargo,
GitHub muestra todos los commits bajo el usuario Bramart96 debido a que
el email configurado para P1 (braianmartinez96@gmail.com) no está
registrado en ninguna cuenta de GitHub, siendo Bramart96 el único usuario
registrado en la plataforma. La trazabilidad correcta se verifica leyendo
el mensaje de cada commit.

### 2. Gestión de ramas durante el desarrollo

Las etapas CVU-1 a CVU-7 fueron desarrolladas sobre la rama `main`,
ya que el proyecto se ejecutó bajo una modalidad de trabajo colaborativo
simulada, sin desarrollo paralelo entre integrantes reales.
Para dar cumplimiento a las prácticas de integración propuestas por
la consigna, en la etapa final se creó la rama `dev`, desde la cual se
gestionó el Pull Request, la revisión de cambios y la integración final
al repositorio principal.


### 3. Auto-aprobación del Pull Request
GitHub no permite que el mismo usuario que abre un Pull Request lo apruebe
formalmente. Al trabajar con una única cuenta de GitHub (Bramart96), el
botón de aprobación estuvo inhabilitado. El flujo de revisión quedó
documentado mediante comentarios en el PR identificando a cada participante
(P1 y P2), y el merge se realizó correctamente una vez completada la revisión.

---


### 4. Archivos de documentación commiteados vacíos
Durante el commit `1c75fec` (CVU-5: Agregar documentacion de base de datos — P2),
los archivos `Casos_Prueba.md`, `Diccionario_Datos.md` y `Gestion_Estados.md`
fueron commiteados sin contenido. Los archivos fueron creados como marcadores
de estructura del repositorio pero su contenido no fue completado en esa instancia.
Adicionalmente, `Diseño_Base_de_Datos.md` fue eliminado por no contener información
relevante, dado que la estructura de datos ya se encuentra documentada en
`Diccionario_Datos.md`. Como corrección, se completó el contenido de cada archivo
y se realizó un nuevo commit en CVU-8 documentando el cambio.

## Instalación y ejecución
1. Clonar el repositorio:
   `git clone https://github.com/Bramart96/tpi-chatbot-licencias.git`
2. Instalar dependencias:
   `pip install -r requirements.txt`
3. Ejecutar el simulador:
   `python src/Python/chatbot_vacaciones.py`
