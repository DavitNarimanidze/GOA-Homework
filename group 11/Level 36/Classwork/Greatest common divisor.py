def mygcd(x, y):
    while y != 0:
        x ,y = y,x % y
    return x
#  7kyu 