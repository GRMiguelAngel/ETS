from triangle import Triangle       # Importo la clase "Triangle"

triangle1 = Triangle(5)     # Creo un objeto de la clase "Triangle"

def test_calc_area():
    assert Triangle.calc_area(triangle1) == 2.1650635094610964      # Compruebo que el resultado esté correcto
def test_calc_perimeter():
    assert Triangle.calc_perimeter(triangle1) == 15     # Compruebo que el resultado esté correcto
