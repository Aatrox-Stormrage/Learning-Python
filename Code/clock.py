import time

class clock:

    def __init__(self, hour, minute, second):
        self.hour = hour = 0
        self.min = minute = 0
        self.sec = second = 0

    def run(self):   # 走字函数
        self.sec += 1

        if self.sec == 60:
            self.min += 1
            self.sec = 0

            if self.min == 60:
                self.hour += 1
                self.min = 0

                if self.hour == 24:
                    self.hour = 0

    def show(self):
            """显示时间"""
            return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

# 创建时钟对象
clock = clock(23, 59, 58)

while True:
    # 给时钟对象发消息读取时间
    print(clock.show())

    # 休眠1秒钟
    time.sleep(1)

    # 给时钟对象发消息使其走字
    clock.run()