# 22 July 2022

class Sort:
    def __init__(self, arr):
        self.arr = arr

    def bubble(self):
        arr = self.arr.copy()
        n = len(arr) - 1

        for j in range(n):
            for i in range(n - j):
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp   
        
        return arr

    def selection(self):
        arr = self.arr.copy()
        n = len(arr)

        sorted_till = -1

        while sorted_till < n - 1:
            index_of_smallest = sorted_till + 1
            for i in range(index_of_smallest + 1, n):
                if arr[i] < arr[index_of_smallest]:
                    index_of_smallest = i

            temp = arr[index_of_smallest]
            arr[index_of_smallest] = arr[sorted_till + 1]
            arr[sorted_till + 1] = temp

            sorted_till += 1

        return arr




    def insertion(self):
        pass

    def merge(self):
        pass

    def quick(self):
        pass

    def radix(self):
        pass

a = [13, 3, 6, 0, -1, 50, 20, 31]

s = Sort(arr = a)
sorted_arr = s.selection()

print(sorted_arr)
