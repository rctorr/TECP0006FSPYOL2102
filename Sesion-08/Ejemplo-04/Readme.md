
## Tests sobre clases y métodos

### OBJETIVO

- Crear test para métodos

#### REQUISITOS

1. Pytest
2. Python 3

#### DESARROLLO

Hasta el momento hemos visto ejemplos de test unicamente con funciones, pero cuando trabajamos usando el paradigma orientado a objetos también se puede realizar tests unitarios, en estos casos la unidad básica a testear son los métodos de clase y se realiza de una manera similar  a cuando se testean funciones.

Por ejemplo, si tenemos la siguiente definición de clase en `estudiante.py`:
```
import json

class EstudianteDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self,nombre):
        for estudiante in self.__data['estudiantes']:
            if estudiante ['nombre'] == nombre:
                return estudiante
```

La cual tiene métodos para conectarse a una base de datos json de estudiantes y devolver datos, si tenemos el siguiente json de prueba

```
{
    "estudiantes": [
        {
            "id": 1,
            "nombre": "Mario",
            "resultado": "aprobado"
        },
        {
            "id": 2,
            "nombre": "Luigi",
            "resultado": "reprobado"
        }
    ]
}
```

Podemos crear el siguiente test para el método get_data
```
from estudiante import EstudianteDB
import pytest

db = EstudianteDB()
db.connect('data.json')

def test_datos_luigi():
    luigi = db.get_data('Luigi')
    assert luigi['id'] == 2
    assert luigi['nombre'] == 'Luigi'
    assert luigi['resultado'] == 'reprobado'

def test_datos_mario():
    luigi = db.get_data('Mario')
    assert luigi['id'] == 1
    assert luigi['nombre'] == 'Mario'
    assert luigi['resultado'] == 'aprobado'
```

Al ejecutar este test, podemos ver que el método lo pasa
```
$ pytest -v test_estudiante.py 
============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 -- /home/rctorr/miniconda3/bin/python
cachedir: .pytest_cache
rootdir: /home/rctorr/Escritorio/TECP0006FSPYOL2102/Sesion-08/Ejemplo-05
plugins: anyio-3.1.0, xonsh-0.9.18
collected 2 items                                                              

test_estudiante.py::test_datos_luigi PASSED                              [ 50%]
test_estudiante.py::test_datos_mario PASSED                              [100%]

============================== 2 passed in 0.01s ===============================
```
