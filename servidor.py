from flask import Flask, request
import serial

# Cambia 'COM3' por el puerto serial donde está conectado tu Arduino
arduino = serial.Serial('COM3', 9600)

app = Flask(__name__)

@app.route('/motor', methods=['POST'])
def motor():
    state = request.json.get('state')  # 'ON' o 'OFF'
    arduino.write((state + '\n').encode())
    return 'Motor ' + state

@app.route('/speed', methods=['POST'])
def speed():
    value = request.json.get('value')  # 0 a 255
    arduino.write((f"SPD:{value}\n").encode())
    return f"Velocidad {value}"

@app.route('/direction', methods=['POST'])
def direction():
    dir = request.json.get('direction')  # 'F' o 'R'
    arduino.write((f"DIR:{dir}\n").encode())
    return f"Dirección {dir}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
