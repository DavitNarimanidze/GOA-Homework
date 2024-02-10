from turtle import*

# lesson1 Homework: Paint House

# Step 1: draw a square
speed(30)
width(5)
color("orange")

forward(200)
left(90) 


forward(200)
left(90) 


forward(200)
left(90) 


forward(200)
left(90) 

#End Of Square

#Step 2: Drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 180)
pendown()

color("blue") 
begin_fill()
left(30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(180, 180)
pendown

color('blue')
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick()