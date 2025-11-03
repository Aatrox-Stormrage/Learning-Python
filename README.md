## Learning-Python
Personal Python Learning Record

## 1. CRAPS
  The basic flow of a single game is: 
    1. The shooter wagers to pass (win) and then makes an initial come-out roll with two six-sided dice.
        a. If the come-out roll is 7 or 11, that is a natural and the shooter has a pass (wins); the game is over.
        b. If the come-out roll is 2, 3, or 12, that is a crap and the shooter has a missout (loses); the game is over.
        c. If the come-out roll is any other number (4, 5, 6, 8, 9, or 10), that value becomes the shooter's point.
    2. If a point has been set, the shooter continues to roll until either:
        a. A subsequent roll matches the point and the shooter has a pass (wins); or
        b. A subsequent roll is 7 and the shooter has a missout (loses).
    3. Once a point is set and a missout occurs, the dice are passed to the person on the shooter's left, who becomes the new shooter.

```
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
```

## 2. Is prime
  Design a function to determine if a given positive integer greater than 1 is not a prime number. 
  A prime number is a positive integer (greater than 1) that can only be divided evenly by 1 and itself. 
  If a positive integer N greater than 1 is a prime number, that means there are no factors of it between 2 and N - 1.

```

def is_prime(num:int) -> bool:

    for i in range(2, num - 1):
        if num % i == 0:
            return False

    return True

num = int(input('num = '))

print(f'Is prime?\n{is_prime(num)}')

```

## 3. Recoed_down_up
  The decorator function itself can also be parameterized. In simple terms, decorators can also be customized through the parameters provided by the caller. We will explain this concept to you later when we use it.

```

import random
import time

# 时间记录函数record()
def record_time(func):

    def wrapper(*args, **kwargs):

        # 在执行被装饰的函数之前记录开始时间
        start = time.time()   # 执行在指定函数之前
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)   # 执行指定函数
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()   # 执行在指定函数之后
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值

        return result

    return wrapper

# 下载函数download()
@record_time
def download(filename):
    print(f'开始下载文件：{filename}')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成')

#  上传函数upload()
@record_time
def upload(filename):
    print(f'开始上传文件：{filename}')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成')

download('Python从入门到住院.pdf')
print('\n')
upload('我要成为原神糕手.pdf')

```
