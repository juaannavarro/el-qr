import base64

# Inicializa la cadena codificada con la salida de tu script
encoded_str = "Vm0wd2VHUXhUblJWV0d4WFlURndVRlpzWkc5V1JteFZVMnhPYWxKc1NsWldSM1JQWVcxS1IxZHFRbUZTVjJoeVZtcEJlRmRIVmtsaVJtUlhaV3hhVVZaclpIcGxSbVJYVW01S2FGSnRhRzlVVm1oRFpWWmtWMVpzV214U2JWSllWVzAxVDJGR1NuTlhhemxYWWxoU00xVXhXbXRXTVhCSlkwZDRVMDFFVmpaV01uUnZVakZaZVZOcmJGSmlhelZoVm10Vk1WSkdXWGhYYkhCc1ZsUkdTbGxWV2xkVWJGcFZWbXRzVjFaRmEzaFdha3BIVmpGT2RWWnNTbWxTTW1ob1ZtMDFkMUpyTVVkalJtaHNVak5TV1ZacVFURlNNWEJHVjJ4a1ZXSlZjRWRaYWs1clZqRmFSbUV6YUZkV1JWcG9Xa1ZhVDJNeVNraGhSbEpUVm01Q2IxWXhXbE5TTVUxNVZtNU9WbUpHY0ZsWmJHaFRZMVpTVjFwRVRrNWlSbG93VkZaU1UyRkdXbkppUkZwYVZsWndNMVl3V21GU2JFNTFVMnhXYUUxc1NrbFhWRXA2WlVaYVYxcElUbFJpUjFKVVZGUkJkMDFSUFQwPQ=="

# Intenta decodificar Base64 múltiples veces
try:
    while True:
        # Decodificar la cadena
        decoded_bytes = base64.b64decode(encoded_str)
        # Intentar ver si el resultado decodificado puede ser Base64
        try:
            base64.b64decode(decoded_bytes)
        except base64.binascii.Error:
            # Si hay un error, es probable que no sea Base64, entonces imprime el resultado
            print(decoded_bytes.decode('utf-8'))
            break
        # Si no hay error, reasigna el resultado para otra ronda de decodificación
        encoded_str = decoded_bytes
except (base64.binascii.Error, UnicodeDecodeError) as e:
    print("Hubo un error al decodificar la cadena:", e)
