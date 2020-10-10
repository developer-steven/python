"""
用Python的turtle模块绘制国旗
Version: 0.1
Author: Steven
Date: 2020-10-10
"""
def get_sum(num):
    """get the sum from 1 to num"""
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

def main():
    """主函数"""
    sum = get_sum(100)
    print('从1到100的和为%d'%sum)

if __name__ == '__main__':
    main()