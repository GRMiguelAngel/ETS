from calculator import divide, sum_numbers, substract, multiply

def test_divide():
    assert divide(4, 2) == 2
def test_float_divide():
    assert divide(8, 5) == 1.6

def test_num_numbers():
    assert sum_numbers(2, 2) == 4

def test_substract_nums():
    assert substract(5, 1) == 4

def test_multiply():
    assert multiply(5, 7) == 35