import turtle

screen = turtle.Screen()
screen.setup(400, 400)

turtle = turtle.Turtle()

def square(x, y, length):
    # x: x 座標
    # y: y 座標
    # length: 邊的長度
    
    turtle.penup()
    turtle.goto(x, y)           # 將 turtle 移到指定的位置
    turtle.setheading(0)        # 將 turtle 朝向特定的角度
    turtle.pendown()

    # 畫一個正方形
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

square(50, 50, 100)
square(-50, -50, 50)
square(-50, 50, 30)

screen.exitonclick()