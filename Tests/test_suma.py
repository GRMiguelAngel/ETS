from suma import sum_numbers

def test_num_numbers():
    assert sum_numbers(2,2) == 4

# @pytest.mark.parametrize(
#     "input_x, input_y, expected",
#     [
#         (5,1,6)
#         (6,sum_numbers(4,2),12)
#         (sum_numbers(19,1),15,35)
#         (-7,10,sum(-7,10))
#     ]
# )

# def test_sum_numbers_params(input_x, input_y):
#     assert sum_numbers(input_x, input_y) ==