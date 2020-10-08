"""
用Python的turtle模块绘制国旗
Version: 0.1
Author: Steven
Date: 2020-10-08
"""
import turtle

# 填充颜色
turtle.fillcolor("red")

# 开始画，类似起笔
turtle.begin_fill()

# 计时器，用于计录次数
count = 1

# 控制绘制次数
while count <= 5:
    # 画笔绘制的方向，向前移动指定的距离
    turtle.forward(100)
    # 向右转144度
    turtle.right(144)
    # 循环绘制
    count += 1
# 完成填充图片的绘制。
turtle.end_fill()
# 隐藏海龟
turtle.ht()
# 显示绘图窗口
turtle.mainloop()