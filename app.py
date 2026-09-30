def divide(a, b):
    if b==0: raise ZeroDivisionError("zero division error") 
    return a / b

def find_max(numbers):
    max_num = -10**8

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num
