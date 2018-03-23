import turtle

screen = turtle.Screen()
screen.setup(400, 400)

t = turtle.Turtle()

# 畫兩個正方形
t.penup()
t.goto(50, 50)
t.pendown()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.goto(-50, -50)
# 設定頭朝哪一個方向
t.setheading(180)
t.pendown()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

screen.exitonclick()