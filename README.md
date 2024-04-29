# el-qr

# Sistema de Entrada con Código QR para la Universidad

## Descripción
En la entrada de la universidad se ha implantado un nuevo sistema para facilitar el acceso a las clases. Este sistema utiliza códigos QR para verificar la entrada de los estudiantes a las aulas. José Antonio, el encargado del sistema, distribuye varios códigos QR para que los alumnos puedan probar la compatibilidad con sus teléfonos.

## ¿Cómo utilizar?

### Leer el Código QR
- Utiliza cualquier lector de códigos QR para escanear y leer la información.
- Alternativamente, puedes utilizar la línea de comandos para leer el código QR si tienes dificultades con lectores convencionales.

### Pasos para leer desde la consola
1. Asegúrate de tener `zbar-tools` instalado en tu sistema. En sistemas basados en Debian, puedes instalarlo con:
   ```sh
   sudo apt-get install zbar-tools


2. Utiliza el comando `zbarimg` para leer el código QR desde tu terminal. Si estás en un sistema operativo basado en Unix, como Linux o macOS, el comando es:
   ```bash
   zbarimg --raw path_to_your_qr_code.png


