# 4 July 2022

terrorists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(terrorists)

# def target_of(k):
#     for i in range(k + 1, n):
#         if terrorists[i] != 0: return i

#     for i in range(k):
#         if terrorists[i] != 0: return i

#     return -1


# def next_killer(k):
#     for i in range(k + 1, n):
#         if terrorists[i] != 0: return i

#     for i in range(k):
#         if terrorists[i] != 0: return i

#     return -1



# total_killed, killer = 0, 0
# while total_killed < n - 1 :
    
#     terrorists[target_of(killer)] = 0
#     total_killed += 1
#     killer = next_killer(killer)


# for i in range(n):
#     if terrorists[i] != 0:
#         print(terrorists[i])
#         break 



terrorists = [True] * n 

n = len(terrorists)

def target_of(k):
    for i in range(k + 1, n):
        if terrorists[i] != 0: return i

    for i in range(k):
        if terrorists[i] != 0: return i

    return -1


def next_killer(k):
    for i in range(k + 1, n):
        if terrorists[i] != 0: return i

    for i in range(k):
        if terrorists[i] != 0: return i

    return -1



total_killed, killer = 0, 0
while total_killed < n - 1 :
    
    terrorists[target_of(killer)] = 0
    total_killed += 1
    killer = next_killer(killer)


for i in range(n):
    if terrorists[i] != 0:
        print(terrorists[i])
        break 


