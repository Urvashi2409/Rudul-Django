import turtle
turtle.speed(10)
turtle.bgcolor("black")
turtle.pensize(5)
colors = ["violet", "purple", "green", "yellow", "blue", "orange", "brown", "pink", "white"]
for i in range(100):
    turtle.color(colors[i%len(colors)])
    turtle.forward(200)
    turtle.left(250)

turtle.done()