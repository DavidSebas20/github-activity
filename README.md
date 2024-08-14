# GitHub User Activity CLI

## Descripción

Esta aplicación de línea de comandos (CLI) permite obtener y mostrar la actividad reciente de un usuario de GitHub utilizando la API pública de GitHub. El programa extrae eventos de la cuenta de GitHub del usuario especificado y muestra información sobre commits, problemas y creación de repositorios.

## Requisitos

- Python 3.x

## Instalación

1. **Clona o descarga el repositorio:**
```bash
   git clone https://github.com/DavidSebas20/github-activity.git
```

2. **Navega al directorio del proyecto:**

```bash
cd github-activity
```

3. **Ejecuta el script desde la línea de comandos proporcionando el nombre de usuario de GitHub como argumento:**

```bash
python github_activity.py <nombre_de_usuario>
```

## Ejemplo
```bash
python github_activity.py DavidSebas20
```
Salida esperada:
```bash
Subido 5 commits a DavidSebas20/taskt-tracker-cli
Subido 3 commits a DavidSebas20/redes-ruta-mas-corta
Creado el repositorio DavidSebas20/taskt-tracker-cli
```
