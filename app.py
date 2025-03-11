from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la ruta principal
@app.route('/')
def index():
    return '<h1>App de: JoseAntonio</h1><br/><h2>2 visitas.</h2>'

# Configuración para que Flask escuche en todas las interfaces (para acceso remoto)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
