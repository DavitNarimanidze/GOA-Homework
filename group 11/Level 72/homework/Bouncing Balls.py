def bouncing_ball(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    
    count = 0
    
    
    while h > window:

        count += 1
        h *= bounce

        if h > window:
            count += 1
    
    return count