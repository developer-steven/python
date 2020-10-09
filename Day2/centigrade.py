"""
用Python的turtle模块绘制国旗
Version: 0.1
Author: Steven
Date: 2020-10-09
"""
w = float(input('请输入华氏温度: '))
c = (w - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (w, c))
print(f'{w:.1f}华氏度 = {c:.1f}摄氏度')