def f(x, y, z, n):
    if n == 1:
        # print(x, '->', z)
        pass

    else:
        print("f(",x, ", ", z, ", ", y, ", ", n - 1, ")")
        f(x, z, y, n - 1)
        
        print("f(",x, ", ", y, ", ", z, ", ", 1, ")")
        f(x, y, z, 1)
        
        print("f(",y, ", ", x, ", ", z, ", ", n - 1, ")")
        f(y, x, z, n - 1)

    return


f('a', 'b', 'c', 100)
