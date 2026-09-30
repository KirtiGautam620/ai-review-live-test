def divide(a, b):
    if b==0: raise ZeroDivisionError("zero division error") 
    return a / b

def find_max(numbers):
    if len(numbers)==0:return
    max_num = numbers[0]
    for num in range(1,len(numbers)):
        if num > max_num:
            max_num = num

    return max_num
