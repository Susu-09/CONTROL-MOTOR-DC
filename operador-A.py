import requests

# Cambia esta IP por la IP de la máquina donde corre servidor.py
SERVER_IP = "255.255.255.0"

while True:
    cmd = input("Escribe ON para encender o OFF para apagar (salir para terminar): ").strip().upper()
    if cmd == "SALIR":
        break
    if cmd in ["ON", "OFF"]:
        try:
            r = requests.post(f"http://{SERVER_IP}:5000/motor", json={"state": cmd})
            print(r.text)
        except Exception as e:
            print("Error:", e)
    else:
        print("Comando inválido")
