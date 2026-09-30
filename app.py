def divide(a, b):
    if b==0: raise ZeroDivisionError("zero division error") 
    return a / b

def find_max(numbers):
    if len(numbers)==0:return None
    max_num = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num
