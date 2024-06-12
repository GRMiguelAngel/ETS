from employee import Empleado

def test_aumentar_salario():
    empleado=Empleado('Carlos', 'Pérez', 3000)
    empleado.aumentar_salario()

    assert empleado.salario == 4000