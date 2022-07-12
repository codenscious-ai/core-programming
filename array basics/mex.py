# a = [0, 1, 2, 3]
# n = len(a)

# mex = 0
# while mex < n:
#     is_present = False
#     for i in range(len(a)):
#         if a[i] == mex:
#             is_present = True
#             mex += 1
#             break
    
#     if is_present == False: break

# print(mex)


a = [0, 1, 2, 13, 4]
n = len(a)
mex = n
is_present = [False] * n

for i in range(n):
    if a[i] < n: is_present[a[i]] = True

for i in range(n):
    if is_present[i] == False: 
        mex = i
        break

print(mex)









