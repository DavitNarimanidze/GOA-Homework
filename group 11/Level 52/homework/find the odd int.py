def find_it(seq):
    count = {}
    
    for num in seq:
        count[num] = count.get(num,0) + 1
        
    for num,count in count.items():
        if count %2!=0:
            return num
    