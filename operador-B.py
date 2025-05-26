import requests

SERVER_IP = "192.168.1.52"

while True:
    try:
        vel = input("Introduce velocidad (0-255) o 'salir' para terminar: ").strip()
        if vel.lower() == 'salir':
            break
        vel_int = int(vel)
        if 0 <= vel_int <= 255:
            r = requests.post(f"http://{SERVER_IP}:5000/speed", json={"value": vel_int})
            print(r.text)
        else:
            print("Introduce un valor entre 0 y 255")
    except ValueError:
        print("Valor inválido")
    except Exception as e:
        print("Error:", e)
