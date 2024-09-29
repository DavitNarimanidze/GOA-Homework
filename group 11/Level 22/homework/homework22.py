#1
# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5
#8kyu 
# def litres(time):
#     return int(time*0.5)


#2
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0


# def paperwork(n, m):
#     if n < 0:
#         return 0
#     elif m < 0:
#         return 0 
#     else:
#         return (n*m)
#8kyu


#3
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


# def grow(arr):
#     name = 1
#     for i in arr:
#         name = name * i
#     return name
#8kyu


#4
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.


# def fake_bin(x):
#     string = ""
#     for i in x:
#         if int(i) >=5:
#             string += "1"
#         else:
#             string += "0"
#     return string
#8kyu



#5
# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).


# def count_by(x, n):
#     listn = []
#     for i in range(1,n+1):
#         listn.append(i*x)
#     return listn
#8kyu