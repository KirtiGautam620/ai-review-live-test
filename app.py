def divide(a, b):
    if b==0: raise ZeroDivisionError("zero division error") 
    return a / b

def find_max(numbers):
    if len(numbers)==0:return
    max_num = numbers[0]
    for num in range(1,len(numbers)):
        if numbers[num] > max_num:
            max_num = numbers[num]

    return max_num
