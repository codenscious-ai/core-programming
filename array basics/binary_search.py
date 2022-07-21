# 21 July 2022

class Search:
    def __init__(self, arr):
        self.arr = arr

    def linear(self, num):
        for i in range(len(self.arr)):
            if num == self.arr[i]:
                return i
                
        return -1

    def binary(self, num):
        start, end = 0, len(self.arr) - 1
        
        while start < end:
            mid = int((start + end) / 2)
         
            if num > self.arr[mid]: 
                start = mid
            elif num < self.arr[mid]: 
                end = mid
            else:
                return mid

        return -1


a = [1, 4, 20, 25, 30, 32, 40, 90, 95, 100]
search = Search(a)
print(search.binary(27))







