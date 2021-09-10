from flask import Flask
from flask import render_template
from flask import request
import productos

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/panel/')
def panel(msg=""):
    pass

@app.route('/producto/alta/', methods=['GET', 'POST'])
def producto_alta():
    pass

@app.route('/productos/')
def productos_lista():
    pass

@app.route('/producto/modificar/<int:id_>/', methods=['GET', 'POST'])
def producto_modificar(id_):
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

