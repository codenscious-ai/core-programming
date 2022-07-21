# 11 July 2022

# n = int(input())



for n in range (2, 97):

    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break


    if prime == True: print(n, end = '...')

