from estudiante import EstudianteDB

db = EstudianteDB()
db.connect('data.json')


def test_datos_luigi():
    luigi = db.get_data('Luigi')
    assert luigi['id'] == 2
    assert luigi['nombre'] == 'Luigi'
    assert luigi['resultado'] == 'reprobado'
    assert len(luigi.keys())  == 3

def test_datos_mario():
    estudiante = db.get_data('Mario')
    assert estudiante['id'] == 1
    assert estudiante['nombre'] == 'Mario'
    assert estudiante['resultado'] == 'aprobado'
    assert len(estudiante.keys())  == 3
