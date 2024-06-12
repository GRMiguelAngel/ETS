from car import Coche       # Importo la clase "Coche" del documento "car.py"

coche1 = Coche("Citroën", "Berlingo", "negro", 1.5)     # Creo un objeto de la clase "Coche"

def test_acelerar():
    assert Coche.acelerar(coche1) == True       # Realizo el test para saber si el resultado está correcto

def test_frenar():
    assert Coche.frenar(coche1) == False        # Realizo el test para saber si el resultado está correcto