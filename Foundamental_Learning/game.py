"""用python设计第一个游戏"""

count = 3

import random
answer = random.randint(1, 10)

while count > 0:
    temp = input("不妨猜一下小甲鱼心里想的的哪个数字")
    guess = int(temp)

    if guess == answer:
        print("你是小甲鱼心里的蛔虫嘛？！")
        print("哼，猜中了也没奖励！")
        break
    else:
        count = count - 1
        if guess < answer:
            print("小啦")
        else:
            print("大啦")

print(answer)
print("游戏结束，不玩啦^_^")

