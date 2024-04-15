def rec_func(list_):
    total_sum = 0
    for item in list_:
        if isinstance(item, list):
            total_sum += rec_func(item)
        else:
            total_sum += item
    return total_sum

list_ = [[[ [1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]