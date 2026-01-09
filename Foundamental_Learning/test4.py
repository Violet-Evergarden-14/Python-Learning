def myfun():
    a, b = 0, 1
    def call(num):
        nonlocal a, b
        for i in range(num):
            a, b = b, a + b
            print(a)
    return call

f = myfun()

f(100)
