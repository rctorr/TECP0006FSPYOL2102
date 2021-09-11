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