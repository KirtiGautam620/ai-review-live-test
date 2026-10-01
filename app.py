def find_max(numbers):
    if not numbers:return None
    max_num = float('-inf')

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

password = "FakePassword1235!"