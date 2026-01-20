# Section 1 - Your code
from utils import *
set_background("bluesky")

s1 = create_sprite("unicorn", 200, -100)
s2 = create_sprite("alien", 50, -50)
s2 = create_sprite("malkmus", -10, -1)
s2 = create_sprite("kitten", 50, -100)
s2 = create_sprite("praise", -150,-50)

message1 = create_sprite("cardinal",-200,200)
message1.color("purple")
message1.write("heavemmmmmn...",font = ("Bubble", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()