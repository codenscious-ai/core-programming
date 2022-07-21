# 1 July 2022s

# a = [8, -3, -2, -1, 4, -7]

# largest = a[0]
# index_of_largest = 0
# for i in range(1, len(a)):
#     if a[i] > largest: 
#         largest = a[i]
#         index_of_largest = i

# if index_of_largest == 0: second_largest = a[1]
    
# else: second_largest = a[0]
    

# for i in range(1, len(a)):
#     if a[i] > second_largest and i != index_of_largest:
#         second_largest = a[i]

# print(second_largest)
        


a = [8, 8, -3, -2, -1, 4, -7]

start = 0
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        start = i
        break

if a[start + 1] > a[start]:
    largest = a[start + 1]
    second_largest = a[start]
else:
    largest = a[start]
    second_largest = a[start + 1]

for i in range(len(a)):
    
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    elif a[i] > second_largest and a[i] < largest:
        second_largest = a[i]
    
print(second_largest)

