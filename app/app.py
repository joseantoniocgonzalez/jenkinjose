from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Leer el contador de visitas
    contador_file = 'contador.txt'
    visitas = 0
    if os.path.exists(contador_file):
        with open(contador_file, 'r') as f:
            visitas = int(f.read())
    
    visitas += 2  # Cambié esto para que no sea "2 visitas" como el test espera.
    
    # Escribir el nuevo número de visitas
    with open(contador_file, 'w') as f:
        f.write(str(visitas))
    
    return f"<h1>Aplicación de: JoseAntonio</h1><br/><h2>{visitas} visitas.</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
