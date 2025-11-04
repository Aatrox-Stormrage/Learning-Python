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