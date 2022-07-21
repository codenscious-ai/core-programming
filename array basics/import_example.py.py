# 18 20 July 2022
from tupple_sum import TuppleSum as TS


x = [3, 1, 2, 8, 4, 6, 7]

tupples = TS(x)

print(tupples.a)

# print(tupples.by_exhaustive_search(sum = 10))
# print(tupples.by_sorting(sum = 10))
print(tupples.by_dictionary(sum = 10))
print(tupples.a)