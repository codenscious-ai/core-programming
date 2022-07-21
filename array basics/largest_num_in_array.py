# 29 June 2022

a = [-3, -2, -1, 4, -7, 8]


largest = a[0]
for i in range(1, len(a)):
    if a[i] > largest: 
        largest = a[i]

print(largest)        
