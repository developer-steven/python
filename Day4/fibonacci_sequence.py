"""
生成斐波那契数列的前20个数
Version: 0.1
Author: Steven
Date: 2020-10-11
"""
def get_fibonacci_sequence(num):
    list_array = [1,1]
    while len(list_array) <= num:
        length = len(list_array)
        list_array.append(list_array[length-1] + list_array[length-2])
    if len(list_array) > num and num > 2:
        for i in list_array:
            print(i, end=',')

def main():
    """主函数"""
    get_fibonacci_sequence(20)

if __name__ == '__main__':
    main()