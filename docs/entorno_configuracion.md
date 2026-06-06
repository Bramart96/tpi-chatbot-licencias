# Configuración del Entorno de Trabajo
## TPI — Chatbot Gestión de Licencias | UTN

## Herramientas utilizadas
- Google Colab (notebook principal: tpi_chatbot_licencias.ipynb)
- GitHub (repositorio: Bramart96/tpi-chatbot-licencias)
- Jira (proyecto: CHATBOT-VACACIONES-UTN)

## Gestión segura de credenciales
- El token de GitHub se almacena como secreto en Google Colab
- Se accede mediante `userdata.get('GITHUB_TOKEN')`
- No se expone en ningún archivo ni historial de commits

## Vinculación Colab → GitHub
- Clone autenticado vía token desde Colab
- Commits realizados con identidad configurada por integrante
- Push directo a rama main del repositorio remoto

## Integrantes
- Integrante 1: braianmartinez (braianmartinez96@gmail.com)
- Integrante 2: bramart96 (bramart96@gmail.com)
