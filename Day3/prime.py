"""
判断一个整数是否为素数
Version: 0.1
Author: Steven
Date: 2020-10-10
"""
from math import sqrt
def is_prime():
    value = int(input('Please input an integer: '))
    isPrime = True
    if isinstance(value,int):
        end = int(sqrt(value))
        for i in range(2,end+1):
            if value % i == 0:
                isPrime = False
                break
        if isPrime and value != 1:
            print('%d是素数' % value)
        else:
            print('%d不是素数' % value)
    else:
        print('Please re-inter')

def main():
    """主函数"""
    is_prime()

if __name__ == '__main__':
    main()