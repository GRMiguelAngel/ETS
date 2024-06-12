from square import Square       # Importo la clase "Square"

square1 = Square(5)     # Creo un objeto de la clase "Triangle"
def test_calc_area():
    assert Square.calc_area(square1) == 25      # Compruebo que el resultado esté correcto

def test_calc_perimeter():
    assert Square.calc_perimeter(square1) == 20     # Compruebo que el resultado esté correcto
