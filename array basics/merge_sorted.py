#12 July 2022

a = [3, 6, 8, 12, 45, 321]
b = [1, 3, 4, 9, 11]

class Merge:
    def __init__(self, list_1, list_2):
        self.a = list_1
        self.b = list_2
        self.c = [None] * (len(self.a) + len(self.b))

        i, j, k = 0, 0, 0

        while i < len(self.a) and j < len(self.b):
            if self.a[i] < self.b[j]:
                self.c[k] = self.a[i]
                i += 1
            else:
                self.c[k] = self.b[j]
                j += 1
            k += 1

        while i < len(a):
            self.c[k] = a[i]
            i += 1
            k += 1

        while j < len(b):
            self.c[k] = b[j]
            j += 1
            k += 1

        return self.c
        


















