import operaciones
import pytest

def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2,0)==2
