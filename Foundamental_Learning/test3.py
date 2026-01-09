import time

def timemaster(function):
    print('kaishi')
    start = time.time()
    function()
    stop = time.time()
    print('jieshu')
    print(f'yongshi{stop - start}miao')

def i():

    print('hello')

timemaster(i)