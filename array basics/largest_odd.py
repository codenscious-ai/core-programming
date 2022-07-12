from zipfile import LargeZipFile


a = [-3, -2, -1, 4, -7, 8]

largest_odd = None

for i in range(len(a)):
    
    # update largest odd when fisrt odd number is found in array 
    if largest_odd == None and a[i] %2 != 0:
        largest_odd = a[i] 
        
    # update largest odd when a[i] is odd and greater than largest odd            
    elif a[i] % 2 != 0 and a[i] > largest_odd:
        largest_odd = a[i]


print(largest_odd)