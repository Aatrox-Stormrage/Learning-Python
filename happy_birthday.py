import tkinter as tk
import random
import threading
import time
import sys  # 用于退出程序

def show_warm_tip():
    # 创建窗口
    window = tk.Tk()
    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # 随机窗口位置(确保窗口完全显示在屏幕内)
    window_width = 250
    window_height = 60
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    # 设置窗口标题和大小位置
    window.title('小A生日快乐！！！')
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')
    # 提示文字列表(已添加新内容)
    tips = [
        '终会再见', '保持微笑', '元气满满', '平安喜乐', '保持好心情', '好好爱自己', '生日快乐',
        '梦想成真', '万事如意', '金榜题名', '顺顺利利', '早点休息', '愿所有烦恼都消失', '别熬夜', '今天过得开心嘛', 'offer都来'
    ]
    tip = random.choice(tips)
    # 多样的背景颜色
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)
    # 创建标签并显示文字
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()
    # 窗口置顶显示
    window.attributes('-topmost', True)
    # 绑定空格键, 触发时退出所有窗口并终止程序
    def on_space(event):
        window.destroy()
        for t in threads:
            if t.is_alive():
                t._stop()  # 这里通过关闭窗口的方式终止线程(tkinter窗口关闭后线程的mainloop会结束)
        sys.exit()  # 退出程序
    window.bind('<space>', on_space)
    window.mainloop()

# 创建线程列表
threads = []
# 窗口数量(根据屏幕大小可调整)
for i in range(300):
    t = threading.Thread(target=show_warm_tip)
    threads.append(t)
    time.sleep(0.005)  # 快速弹出窗口
    threads[i].start()