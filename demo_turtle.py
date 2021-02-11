import turtle
 
turtle.color('red','yellow')
turtle.shape('turtle')

def david(count=6):
    for step in range(count):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360/3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(360/count)

turtle.speed(1)
david()

turtle.hideturtle()
