import turtle, time, random
from utils import *

# Section 1 - setup

#The objective of this game is to keep the cat fed and on high health by pressing the keys
#and to not let the health go down or you will lose the game.

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
#when the "W" key is pressed it "pets" the cat and adds +1 onto its health points.

def feed_cat ():
    global food
    food += 1
    fish  = create_sprite("fish", 0, -55)
    time.sleep(0.5)
    fish.hideturtle()

window.onkeypress(feed_cat, "space")
#when the "space" key is pressed a fish appears in the cats mouth for 0.5 seconds and 
#adds 1 to the food points.

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