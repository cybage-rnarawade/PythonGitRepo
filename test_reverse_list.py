def test_reversed_function():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers)  # original list

    reversed_numbers = numbers[::-1]
    print(reversed_numbers)
    print("reversed list", numbers[::-1])  # reversed list

    assert reversed_numbers == [9, 8, 7, 6, 5, 4, 3, 2, 1]

test_reversed_function()