"""
找出10000以内的完美数
Version: 0.1
Author: Steven
Date: 2020-10-11
"""
def get_perfect_number(num):
    for i in range(1,num + 1):
        factor_list = []
        for j in range(1,i):
            if i % j == 0:
                factor_list.append(j)
        if len(factor_list) > 0:
            sum = 0
            for x in factor_list:
                sum += x
            if i == sum:
                print(i,end=',')

def main():
    """主函数"""
    get_perfect_number(10000)

if __name__ == '__main__':
    main()