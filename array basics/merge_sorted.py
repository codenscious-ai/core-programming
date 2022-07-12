a = [3, 6, 8, 12, 45, 321]
b = [1, 3, 4, 9, 11]
len_c = len(a) + len(b)
c = [None] * len_c

i, j, k = 0, 0, 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c[k] = a[i]
        i += 1
    else:
        c[k] = b[j]
        j += 1
    k += 1

while i < len(a):
    c[k] = a[i]
    i += 1
    k += 1

while j < len(b):
    c[k] = b[j]
    j += 1
    k += 1

print(c)
