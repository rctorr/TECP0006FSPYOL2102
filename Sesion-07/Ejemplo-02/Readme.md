
## Rutas y parámetros

### OBJETIVO

- Crear páginas con múltiples rutas
- Incluir argumentos en las rutas

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

**RUTAS**

Al usar flask es posible crear páginas con varias rutas con comportamiento independiente, para esto utilizaremos el decorador @app.route sobre distintos métodos

Escribe o copia y pega el siguiente código en el archivo `mi-app.py`:

```
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
```

Después de iniciar el servidor local de desarrollo con `python mi-app.py` nos indica que nos podemos conectar a la URL o Link http://127.0.0.1:5000/, esta URL está conformada por varias partes:

- `http://` <- indica el protocolo a usar, por ejemplo http, https, ftp, sftp, rtp, etc.
- `127.0.0.1` <- indica el nombre o la dirección ip del servidor que contiene la página a consultar, por ejemplo google.com.mx o www.google.com.mx.
- `:5000` <- indica el puerto o canal de comunicación con el servidor, este puerto por omisión es el 80 o 445 para el protocolo https://
- `/` <- indica el documento o página a consultar, por omisión es `/` que indica el documento o página inicial

Entonces, tras ejecutar el servidor local, al entrar el link http://127.0.0.1:5000/ sucedenn los siguientes pasos:

1. Se toma sólo la página a consultar, en este caso es `/`
2. Se busca si existe una ruta (`@app.route('/')`) que coincida con la página solicitada.
3. Se ejecuta la función asociada (`index()`).
4. La función prepara los datos a usar por la plantilla, en este caso el valor de la variable `titulo`.
5. Crea una respuesta (`response`) en HTML construida a partir de los datos y la plantilla (`templates/extender.html`).
6. Regresa la el contenido de la respuesta al navegador

Adicionalmente, también se tiene la página o url http://127.0.0.1:5000/acerca-de/

**PARÁMETROS**

Además de tener múltiples rutas es posible crear páginas que acepten argumentos por medio de la URL, por ejmplo:

- http://127.0.0.01:5000/hola/pluto/

Genera la página que dirá:

`Hola Pluto como estás!`

- http://127.0.0.01:5000/hola/rctorr/

Genera la página que dirá:

`Hola Rctorr como estás!`

Para eso al momento de crear una ruta se define una variable y el tipo de dato que uno espera, vamos a agregar el siguiente código a programa de `mi-app.py`

```
@app.route('/hola/<str:nombre>/')
def hola(nombre):
    return f"<h1>Hola {nombre} como estás!</h1>"
```
