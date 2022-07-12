height = [2, 4, 6, 8]
cost = [4, 6, 3, 6]

min_cost = float('inf')

h = -1

# for i <- 0 to n - 1:
    # find sum for making all buildings equl to ith building
    # if sum is less than min_cost, update min_cost

n = len(height)

for j in range(n):
    sum = 0
    for i in range(n):
        sum = sum + cost[i] * abs(height[i] - height[j])
    if sum < min_cost: 
        min_cost = sum
        h = j


print(sum, h)