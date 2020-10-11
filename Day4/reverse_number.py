"""
反转数字，12345变为54321
Version: 0.1
Author: Steven
Date: 2020-10-11
"""
def get_reverse_number(num):
    if isinstance(num,int):
        reversed_number = 0
        while num > 0:
            reversed_number = reversed_number * 10 + num % 10
            num //= 10
        print(reversed_number)
    else:
        print('Please input an integer')

def main():
    """主函数"""
    get_reverse_number(12345)

if __name__ == '__main__':
    main()