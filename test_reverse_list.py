def test_reversed_function():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers)  # original list

    reversed_numbers = numbers[::-1]
    print(reversed_numbers)
    print("reversed list", numbers[::-1])  # reversed list

test_reversed_function()