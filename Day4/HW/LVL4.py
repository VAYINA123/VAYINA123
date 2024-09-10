from turtle import *

speed(200)
color ('gray')

penup()
goto(-350,-200)
pendown()

width(4)

# painting foundation

forward(750)
left(90)
forward(300)
left(90)

forward(750)
left(90)
forward(300)

penup()
goto(30,100)
pendown()

# painting a tower

left(180)
forward(100)
right(45)
forward(80)
left(135)
forward(150)

left(135)
forward(80)
right(45)
forward(100)

penup()
goto(12.5,260)
pendown()

# painting flag log

color("brown")
right(180)
forward(100)

# painting a flag

color (0,0,0)
right(90)
forward(200)
right(135)
forward(30)
left(90)
forward(30)
right(135)
forward(200)

penup()
goto(50.5,359)
pendown()

# writing down goa on flag

color("gray")
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(15)
left(90)
forward(10)

penup()
goto(120,320)
pendown()

color("green")
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(150.5,320)
pendown()

color("gray")
left(55)
forward(50)
right(145)
forward(40)

penup()
goto(179,335)
pendown()
right(90)
forward(20)
exitonclick()