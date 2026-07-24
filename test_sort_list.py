def sort_numbers(numbers):
    return sorted(numbers)

def test_sort_list():
    actual = sort_numbers([3, 2, 6, 1, 5, 4])
    expected = [1, 2, 3, 4, 5, 6]

    assert actual == expected