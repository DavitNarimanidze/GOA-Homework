def sum_two_smallest_numbers(numbers):
    minimum1 = min(numbers)
    numbers.remove(minimum1)
    minimum2 = min(numbers)
    
    return minimum1 + minimum2