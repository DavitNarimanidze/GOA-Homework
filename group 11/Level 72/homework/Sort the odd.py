def sort_array(source_array):
    odd_numbers = sorted([x for x in source_array if x % 2 != 0])
    

    odd_iter = iter(odd_numbers)
    

    sorted_arr = [next(odd_iter) if x % 2 != 0 else x for x in source_array]
    
    return sorted_arr