def reverse_numbers(numbers):
    return numbers[::-1]

def test_reverse_list():
    assert reverse_numbers([1, 2, 3]) == [3, 2, 1]