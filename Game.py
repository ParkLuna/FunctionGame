def sum_numbers(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, (int, float)):  
            total += number
    return total
my_list = [8,2,3,0,7]
result = sum_numbers(my_list)
print(result)  
