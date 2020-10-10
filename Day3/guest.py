"""
猜数游戏
Version: 0.1
Author: Steven
Date: 2020-10-10
"""
import random

def guest_num():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        vaule = int(input('Please input your number:'))
        if vaule < answer:
            print('大一点')
        elif vaule > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')

def main():
    """主函数"""
    guest_num()

if __name__ == '__main__':
    main()