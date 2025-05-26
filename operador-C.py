import requests

SERVER_IP = "192.168.1.52"

while True:
    dir = input("Introduce dirección F (forward) o R (reverse) o 'salir' para terminar: ").strip().upper()
    if dir == "SALIR":
        break
    if dir in ["F", "R"]:
        try:
            r = requests.post(f"http://{SERVER_IP}:5000/direction", json={"direction": dir})
            print(r.text)
        except Exception as e:
            print("Error:", e)
    else:
        print("Dirección inválida")
