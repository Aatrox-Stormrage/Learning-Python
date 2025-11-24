import tkinter as tk
import random
import threading
import time
import sys
from threading import Event

# 配置参数集中管理，方便后续调整
WINDOW_WIDTH = 250
WINDOW_HEIGHT = 60
NUM_WINDOWS = 300  # 窗口数量
POP_DELAY = 0.005  # 窗口弹出间隔时间
TIPS = (
    '终会再见', '保持微笑', '元气满满', '平安喜乐', '保持好心情', '好好爱自己', '生日快乐',
    '梦想成真', '万事如意', '金榜题名', '顺顺利利', '早点休息', '愿所有烦恼都消失', '别熬夜',
    '今天过得开心嘛', 'offer都来'
)
BG_COLORS = (
    'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow', 'plum', 'coral',
    'bisque', 'aquamarine', 'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
)

class BirthdayWisher:
    def __init__(self):
        self.stop_event = Event()  # 线程停止信号
        self.threads = []  # 线程列表

    def create_window(self):
        """创建单个祝福窗口"""
        if self.stop_event.is_set():
            return

        try:
            window = tk.Tk()
            # 获取屏幕尺寸并计算随机位置（确保窗口完全显示）
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x = random.randrange(0, screen_width - WINDOW_WIDTH)
            y = random.randrange(0, screen_height - WINDOW_HEIGHT)

            # 窗口基本设置
            window.title('小A生日快乐！！！')
            window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}')
            window.attributes('-topmost', True)  # 窗口置顶

            # 随机选择提示语和背景色
            tip = random.choice(TIPS)
            bg_color = random.choice(BG_COLORS)

            # 创建标签
            tk.Label(
                window,
                text=tip,
                bg=bg_color,
                font=('微软雅黑', 16),
                width=30,
                height=3
            ).pack()

            # 绑定空格键退出事件
            def on_space(event):
                self.stop_event.set()  # 触发所有线程停止
                window.destroy()

            window.bind('<space>', on_space)

            # 定期检查退出信号
            def check_stop():
                if self.stop_event.is_set():
                    window.destroy()
                    return
                window.after(100, check_stop)  # 每100ms检查一次

            check_stop()
            window.mainloop()

        except Exception as e:
            if not self.stop_event.is_set():
                print(f"窗口创建出错: {e}")

    def start(self):
        """启动所有窗口线程"""
        for _ in range(NUM_WINDOWS):
            if self.stop_event.is_set():
                break
            t = threading.Thread(target=self.create_window)
            self.threads.append(t)
            t.start()
            time.sleep(POP_DELAY)

        # 等待所有线程结束
        for t in self.threads:
            if t.is_alive():
                t.join()
        sys.exit()

if __name__ == "__main__":
    wisher = BirthdayWisher()
    wisher.start()