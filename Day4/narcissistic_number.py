"""
找出所有水仙花数
Version: 0.1
Author: Steven
Date: 2020-10-11
"""
def get_narcissistic_number():
    """get all Narcissistic number"""
    for i in range(100,1000):
        low = i % 10
        mid = i // 10 % 10
        high = i // 100
        if i == high**3 + mid**3 + low**3:
            print(i)

def main():
    """主函数"""
    get_narcissistic_number()

if __name__ == '__main__':
    main()