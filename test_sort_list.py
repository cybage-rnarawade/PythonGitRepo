def test_sort_list():
    number_list = [3, 2, 6, 1, 5, 4]
    sorted_list = sorted(number_list)
    print("sorted_list",sorted_list)
    assert sorted_list==[1, 2, 3, 4, 5, 6]