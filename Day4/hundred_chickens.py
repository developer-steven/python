"""
<<百钱百鸡>>问题
Version: 0.1
Author: Steven
Date: 2020-10-11
"""
def get_all_chickens():
    """穷举法，也称为暴力搜索法"""
    for i in range(20):
        for j in range(33):
            z = 100 - i - j
            if 100 == i * 5 + j * 3 + z / 3:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (i, j, z))

def main():
    """主函数"""
    get_all_chickens()

if __name__ == '__main__':
    main()