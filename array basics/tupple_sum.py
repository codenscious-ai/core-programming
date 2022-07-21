# 18 - 21 jULY 2022

class TuppleSum:

    def __init__(self, a):
        self.a = a
        self.n = len(a)

    def by_exhaustive_search(self, sum):
        b = []

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.a[i] + self.a[j] == sum:
                    b.append((self.a[i], self.a[j]))
                    break
        return b

    def by_sorting(self, sum):
        a = self.a.copy()

        a.sort()
        b = []

        i, j = 0, self.n - 1

        while i < j:
            if a[i] + a[j] < sum:
                i += 1
            elif a[i] + a[j] > sum:
                j -= 1
            else:
                b.append((a[i], a[j]))
                i += 1
                j -= 1

        return b


    def by_dictionary(self, sum):
        # init a dictionary 
        d = {}

        # to hold the list of touples
        b = []

        for i in range(self.n):
            d[self.a[i]] = True

        for i in range(self.n):
            key = sum - self.a[i]
            if key in d and d[key] == True:
                b.append((self.a[i], key))
                d[self.a[i]] = False

        return b




