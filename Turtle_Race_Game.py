# IMPORTING THE REQUIRED MODULE'S

import turtle
from random import randint
import time

# FIXING THE BACKGROUND

wn = turtle.Screen()
wn.bgcolor('light green')
wn.title('TURTLE RACE')

# ********** NAME OF THE GAME **********

name_of_the_game = turtle.Turtle()
name_of_the_game.speed(0)
name_of_the_game.shape('turtle')
name_of_the_game.color('black')
name_of_the_game.penup()
name_of_the_game.left(90)
name_of_the_game.fd(350)
name_of_the_game.pendown()
name_of_the_game.write('TURTLE  RACE', align='center', font=('simple', 30, 'bold'))
name_of_the_game.hideturtle()

# ********** REQUIRED OBJECTS ***********

# --> AREA REQUIRED FOR THE RACE

# position fixing
my_area_turtle = turtle.Turtle()
my_area_turtle.speed(0)
my_area_turtle.shape('turtle')
my_area_turtle.color('white')
my_area_turtle.up()
my_area_turtle.left(90)
my_area_turtle.fd(300)
my_area_turtle.right(90)
my_area_turtle.fd(300)
my_area_turtle.right(90)
my_area_turtle.down()


# finishing_line using my_area_turtle
def finishing_line(length, angle):
    for i in range(4):
        my_area_turtle.fd(length)
        my_area_turtle.right(angle)


for k in range(30):
    my_area_turtle.begin_fill()
    my_area_turtle.fillcolor('black')
    finishing_line(20, 90)
    my_area_turtle.fd(20)
    finishing_line(20, 90)
    my_area_turtle.end_fill()

# BOUNDRIES
my_area_turtle.fd(20)
my_area_turtle.right(90)
my_area_turtle.fd(20)
my_area_turtle.pensize(15)
my_area_turtle.fd(700)
my_area_turtle.right(90)
my_area_turtle.pencolor('black')
my_area_turtle.fd(610)
my_area_turtle.right(90)
my_area_turtle.pencolor('white')
my_area_turtle.fd(700)
my_area_turtle.hideturtle()
time.sleep(1)

# ********** TOO MANY TURTLE'S **********

# --> Turtle: 1
turtle_1 = turtle.Turtle()
turtle_1.shape('turtle')
turtle_1.speed(0)
turtle_1.pensize(3)
turtle_1.color('red')
turtle_1.up()
turtle_1.back(445)
turtle_1.down()

# --> Turtle: 2
turtle_2 = turtle.Turtle()
turtle_2.shape('turtle')
turtle_2.speed(0)
turtle_2.pensize(3)
turtle_2.color('forest green')
turtle_2.up()
turtle_2.goto(-445, 100)
turtle_2.down()

# --> Turtle: 3
turtle_3 = turtle.Turtle()
turtle_3.shape('turtle')
turtle_3.speed(0)
turtle_3.pensize(3)
turtle_3.color('blue')
turtle_3.up()
turtle_3.goto(-445, 200)
turtle_3.down()

# --> Turtle: 4
turtle_4 = turtle.Turtle()
turtle_4.shape('turtle')
turtle_4.speed(0)
turtle_4.pensize(3)
turtle_4.color('yellow')
turtle_4.up()
turtle_4.goto(-445, -100)
turtle_4.down()

# --> Turtle: 5
turtle_5 = turtle.Turtle()
turtle_5.shape('turtle')
turtle_5.speed(0)
turtle_5.pensize(3)
turtle_5.color('purple')
turtle_5.up()
turtle_5.goto(-445, -200)
turtle_5.down()
time.sleep(1)
# *********** LET'S BEGIN THE RACE >>>>>>>

for i in range(68):
    turtle_1.fd(randint(1, 20))
    turtle_2.fd(randint(1, 20))
    turtle_3.fd(randint(1, 20))
    turtle_4.fd(randint(1, 20))
    turtle_5.fd(randint(1, 20))

wn.exitonclick()



