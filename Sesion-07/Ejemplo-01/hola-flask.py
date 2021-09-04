from flask import Flask

app = Flask(__name__)

# 1. URL o Link: mi.app.com/ (1.1.1.1/)
# 2. Función asociada a la ruta

@app.route('/')
def index():
    return "Hola Mundo de Flask!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
