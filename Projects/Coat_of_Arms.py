# Section 1 - Your code
from utils import *
set_background("moon")

s1 = create_sprite("china", 100, 100)
s2 = create_sprite("malkmus", -100, -100)
s3 = create_sprite("kitten", -250, 250)
s4 = create_sprite("artist", 200, -100)
s5 = create_sprite("fish", -50, 100)

message1 = create_sprite("alien",-200,200)
message1.color("purple")
message1.write("Amelia",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("hi",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()