from turtle import*

#building a fundation and walls
speed(200)

color('cyan')

width(6)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
#moving pen without making mess
penup()
goto(200,200)
pendown()
#building ruff
color('red')
right(135)
forward(140)

left(90)
forward(140)

penup()
goto(65,0)
pendown()
#building a door
color('magenta')
right(135)
forward(100)
right(90)
forward(65)
right(90)
forward(100)

penup()
goto(120,40)
pendown()
#making a handle for door
right(90)
width(3)
forward(10)

penup()
goto(1124,1235125)

exitonclick()