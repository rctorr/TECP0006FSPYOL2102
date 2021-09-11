
## Parametrización de test

### OBJETIVO

- Crear test con argumentos parametrizados

#### REQUISITOS

1. Pytest
2. Python 3

#### DESARROLLO

Para crear un conjunto de pruebas se puede utiliza la función `mark.parametrize()`, que recibe como argumentos una cadena con el nombre de los parámetros y una lista que tenga los parámetros en tuplas, así que en lugar de realizar sólo dos casos de pruebas, ahora podemos apliar el número de pruebas de forma muy sencilla:

```
import operaciones
import pytest

@pytest.mark.parametrize(
    'num1, num2, resultado',
    [
        (2,3,5),
        (2,0,2),
        ('Hola ', 'Mundo', 'Hola Mundo'),
        (3.1, 3.1, 6.2),
        (12.5, 1.2, 13.7)
    ]
)

def test_suma(num1, num2, resultado):
    assert operaciones.suma(num1, num2)==resultado 
```

El resultado al ejecutar
```
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/rctorr/Escritorio/TECP0006FSPYOL2102/Sesion-08/Ejemplo-04
plugins: anyio-3.1.0, xonsh-0.9.18
collected 5 items                                                              

test_operaciones_param.py .....                                          [100%]

============================== 5 passed in 0.02s ===============================
```
