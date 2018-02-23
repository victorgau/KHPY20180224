import turtle

screen = turtle.Screen()
screen.setup(400, 400)

turtle = turtle.Turtle()

# 畫兩個正方形
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.goto(-50, -50)
# 設定頭朝哪一個方向
turtle.setheading(180)
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

screen.exitonclick()