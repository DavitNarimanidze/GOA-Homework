def name_in_str(strng : str, name : str) -> bool:
    str1_lower = strng.lower()
    str2_lower = name.lower()
    i, j = 0, 0
    
    while i < len(str1_lower) and j < len(str2_lower):
        if str1_lower[i] == str2_lower[j]:
            j += 1
        i += 1
        
    return j == len(str2_lower)
    
    