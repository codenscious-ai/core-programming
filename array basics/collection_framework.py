# jULY 21 2022

from collections import defaultdict

def def_value():
    return None

d = defaultdict(def_value)


d[1] = "Hi"

print("Key 1 is present in the dictionary")
print(d[1])

print("Key 2 is present in the dictionary")
print(d[2])

