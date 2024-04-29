import subprocess
import base64

def decode_qr_code(image_path):
    # Ejecutar el comando zbarimg para leer el código QR
    result = subprocess.run(['zbarimg', '--raw', image_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    # Decodificar el resultado si se encontró un código QR
    if result.returncode == 0:
        qr_code = result.stdout.strip()
        
        # Suponiendo que el contenido está codificado en base64 varias veces
        try:
            # Intenta decodificar base64 hasta que el contenido ya no esté codificado
            while True:
                qr_code = base64.b64decode(qr_code)
                # Intenta convertir a string para ver si es legible
                try:
                    decoded_str = qr_code.decode('utf-8')
                    # Si el resultado es una cadena imprimible, mostramos el resultado
                    if decoded_str.isprintable():
                        print(decoded_str)
                        break
                except UnicodeDecodeError:
                    continue
        except base64.binascii.Error as e:
            print("Error en la decodificación de Base64:", e)
    else:
        print("No se pudo leer el código QR.")

# Reemplaza 'path_to_image.png' con la ruta a tu imagen del código QR
decode_qr_code('/Users/juanlu_navarro/Documents/Carrera Juan/programacion/el-qr/flag.png')