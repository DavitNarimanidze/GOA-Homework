def variance(numbers): 
    n = len(numbers)
    m = sum(numbers) / n
    
    sum_squared_diff = sum((x - m) ** 2 for x in numbers)
        
    variance = sum_squared_diff / n
    
    return variance