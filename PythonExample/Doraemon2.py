# 导包
import turtle as t
# 定义画笔宽度
t.pensize(5)

# 脸
# 绘制图形的填充颜色为"blue"
t.fillcolor("blue")
# 画半径为200的圆
t.circle(200)
# 绘制图形的填充颜色为"白色"
t.fillcolor("white")
# 画半径为160的圆
t.circle(160)

# 鼻子
# 将画笔移动到坐标为(0,200)的位置
t.goto(0,200)
# 画半径为20的圆
t.circle(20)

# 眼睛
# t.goto(-45,250)
# t.circle(45)
# t.goto(-20,250)
# t.fillcolor("black")
# t.circle(15)
# t.goto(45,250)
# t.goto(20,250)

#smile
# t.goto(0,50)
# t.circle(150,extent = -75)
# print(t.pos())
# t.circle(150,extent = 75)
# t.left(15)
# t.forward(150)