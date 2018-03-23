import turtle

screen = turtle.Screen()
screen.setup(400, 400)

t = turtle.Turtle()

def square(t, x, y, length):
    # x: x 座標
    # y: y 座標
    # length: 邊的長度
    
    t.penup()
    t.goto(x, y)           # 將 turtle 移到指定的位置
    t.setheading(0)        # 將 turtle 朝向特定的角度
    t.pendown()

    # 畫一個正方形
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)

square(t, 50, 50, 100)
square(t, -50, -50, 50)
square(t, -50, 50, 30)

screen.exitonclick()