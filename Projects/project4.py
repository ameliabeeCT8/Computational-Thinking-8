import turtle, time, random
from utils import *

# Section 1 - setup
set_background("flowers")

food = 10
health = 10

sprite1 = create_sprite("kitten", 0, -50)

talker1 = create_sprite("alien", -250, 200)
talker1.write(f"food:{food}",font = ("Arial", 40, "normal"))

talker1.hideturtle()

talker2 = create_sprite("alien", -250, 150)
talker2.write (f"health:{health}",font = ("Arial", 40, "normal"))

talker2.hideturtle()

# Section 2 - controls
def pet_cat ():
    global health
    health += 1

window.onkeypress (pet_cat, "w")

def feed_cat ():
    global food
    food += 1
    fish  = create_sprite("fish", 0, -55)
    time.sleep(0.5)
    fish.hideturtle()

window.onkeypress(feed_cat, "space")

print (f"{health}")
print (f"{food}")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    if i % 100 == 0:
        food -= 1
    talker1.clear()
    talker1.write(f"food:{food}",font = ("Arial", 40, "normal"))
    talker2.clear()
    talker2.write (f"health:{health}",font = ("Arial", 40, "normal"))
    if food <= 5:
        health -= 1
    if health <= 0:
        sprite2 = create_sprite("sad", 0, 0)
        sprite2.write ("       death..", font = ("Arial", 40, "normal"))
 

    time.sleep(0.01)
    window.update()