"""
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
Version: 0.1
Author: Steven
Date: 2020-10-11
"""
from random import randint

def shake():
    return randint(1, 6) + randint(1, 6)

def game_start():
    """初始资产为1000"""
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = None
        while True:
            is_shake = input('是否摇动骰子（Y/N）: ')
            if is_shake == 'Y' or is_shake == 'y':
                first = shake()
                break
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = None
            while True:
                is_shake = input('是否摇动骰子（Y/N）: ')
                if is_shake == 'Y' or is_shake == 'y':
                    current = shake()
                    break
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')

def main():
    """主函数"""
    game_start()

if __name__ == '__main__':
    main()