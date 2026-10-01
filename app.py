def find_max(numbers):
    if len(numbers)==0:return []
    if not numbers:return None
    max_num = float('-inf')

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num