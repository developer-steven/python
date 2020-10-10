"""
九九乘法表
Version: 0.1
Author: Steven
Date: 2020-10-10
"""
def get_multi_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d*%d=%d'%(i,j,i*j),end='\t')
        print()

def main():
    """主函数"""
    get_multi_table()

if __name__ == '__main__':
    main()