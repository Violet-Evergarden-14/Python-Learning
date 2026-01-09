import random
s = random.randint(1,10)
m = 3

while m > 0:
    m -= 1
    t = int(input('请输入你的猜测：'))
    if t > s:
        print('大了，还有', m, '次机会')
    if t < s:
        print('小了，还有', m, '次机会')
    if t == s:
        print('答对了')
        break
else:
    print('错误，挑战结束')