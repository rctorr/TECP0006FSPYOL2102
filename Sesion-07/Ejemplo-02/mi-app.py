from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Página de inicio"
    return render_template('extender.html', titulo=titulo)

@app.route('/acerca-de/')
def acerca_de():
    return "<h1>Página hecha con Flask y con <3</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")