"""

Project: CRAPS
Author: Aatrox
Date: 2025.11.1

"""

import random

money = 1000
flag0 = 1

while flag0:
    print(f'你的总资金为：{money}元')
    debt = int(input('请下注：'))

    if debt == 0:
        print('下注不得为0！\n')
        continue

    money = money - debt
    first_point = random.randrange(1, 6) + random.randrange(1, 6)
    print(f'玩家摇出了：{first_point}')

    if first_point == 7 or first_point == 11:
        money = money + debt * 2
        print('你赢了！\n')

    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('你输了！\n')

    else:
        print('游戏继续。\n')
        flag1 = 1

        while flag1:
            current_point = random.randrange(1, 6) + random.randrange(1, 6)
            print(f'玩家摇出了：{current_point}')

            if current_point == first_point:
                money = money + debt * 2
                print('你赢了！\n')
                break

            elif current_point == 7:
                print('你输了！\n')
                break

            else:
                print('游戏继续。\n')

    if money <= 0:
        flag0 = 0

print('你破产了，游戏结束！')

