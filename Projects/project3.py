import turtle, time, random
from utils import *

# Section 1 - Variables
x1 = -200
y1 = -90
x2 = 100
y2 = 0
x3 = 0
y3 = 50
x4 = -100
y4 = 150


# Section 2 - Setup
set_background("moon")
t1 = create_sprite("kitten",x1,y1)
t2 = create_sprite("alien",x2,y2)
t3 = create_sprite("fish",x3,y3)
t4 = create_sprite("fox",x4,y4)


# Section 3 - Racing
# The alien is the fastest sprite because its point goes += 15 and for all the other sprites
# the += is a lower number.
for i in range(30):
    x1 += 10
    x2 += 15
    x3 += 5
    x4 += 8

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("kitten wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("alien wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("fish wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("fox wins!")


turtle.exitonclick()