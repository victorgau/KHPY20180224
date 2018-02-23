import turtle

# 產生繪圖用的 screen
screen = turtle.Screen()
# 設定 screen 大小
screen.setup(400, 400)

# 產生 turtle
turtle = turtle.Turtle()

# 控制 turtle 行進的方向，以產生圖形
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# 當 screen 被滑鼠點擊時，離開程式
screen.exitonclick()