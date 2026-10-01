def find_max(numbers):
    max_num = float('-inf')

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num