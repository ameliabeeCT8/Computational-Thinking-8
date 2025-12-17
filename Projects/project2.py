harrypotter_points = 0
scottpilgrim_points = 0
scream_points = 0
it_points = 0
starwars_points = 0
snowhite_points = 0
spiderman_points = 0

print ("What movie are you quiz")
input ()
answer1 = input ("Pick 1. A owl, B cat, C ghost, D clowns, E snake, F bird, G spider")
if answer1 == "A":
    harrypotter_points += 5
elif answer1 == "B":
    scottpilgrim_points += 1
elif answer1 == "C":
    scream_points += 5
elif answer1 == "D":
    it_points += 5
elif answer1 == "E":
    starwars_points += 1
elif answer1 == "F":
    snowhite_points += 1
elif answer1 == "G":
    spiderman_points += 5
input ()
answer2 = input ("Which genre is your favorite? A superhero, B fantasy, C horror, D comedy")
if answer2 == "A":
    starwars_points += 1
    spiderman_points += 5
elif answer2 == "B":
    harrypotter_points += 1
    snowhite_points += 5
elif answer2 == "C":
    scream_points += 3
    it_points += 5
elif answer2 == "D":
    scottpilgrim_points += 3
input ()
answer3 = input ("What are your hobbies? A reading, B drawing, C sports, D film, E gaming")
if answer3 == "A" or answer3 == "B":
    harrypotter_points += 5
    snowhite_points += 3
elif answer3 == "C":
    spiderman_points += 1
elif answer3 == "D":
    it_points += 1
    scream_points += 5
elif answer3 == "E":
    scottpilgrim_points += 5
    starwars_points += 1
input ()
answer4 = input ("What's your favorite color? A pink, B blue, C red, D green")
if answer4 == "A":
    scottpilgrim_points += 1
    snowhite_points += 3
elif answer4 == "B":
    starwars_points += 1
    it_points += 3
elif answer4 == "C":
    spiderman_points += 5
    scream_points += 1
elif answer4 == "D":
    harrypotter_points += 1
input ()
answer5 = input ("Whats your favorite food? A pasta, B burgers, C pizza, D fruit")
if answer5 == "A":
    harrypotter_points += 1
    it_points += 1
elif answer5 == "B":
    spiderman_points += 1
    starwars_points += 1
elif answer5 == "C":
    scream_points += 5
    scottpilgrim_points += 1
elif answer5 == "D":
    snowhite_points += 3
input ()
print ("thats everything! press enter to see your movie.")
input ()
if scottpilgrim_points>scream_points and scottpilgrim_points>snowhite_points and scottpilgrim_points>spiderman_points and scottpilgrim_points>harrypotter_points and scottpilgrim_points>it_points and scottpilgrim_points>starwars_points:
    print ("you got SCOTT PILGRIM!!! You are fun, colorful and very cool!")
elif scream_points>scottpilgrim_points and scream_points>snowhite_points and scream_points>spiderman_points and scream_points>harrypotter_points and scream_points>it_points and scream_points>starwars_points:
    print ("you got SCREAM!! You are funny but also kind of scary and probably love movies!")
elif snowhite_points>scottpilgrim_points and snowhite_points>scream_points and snowhite_points>spiderman_points and snowhite_points>harrypotter_points and snowhite_points>it_points and snowhite_points>starwars_points:
    print ("you got SNOW WHITE!!! You are pretty and sweet, and probably love animals!!")
elif spiderman_points>scottpilgrim_points and spiderman_points>scream_points and spiderman_points>snowhite_points and spiderman_points>harrypotter_points and spiderman_points>it_points and spiderman_points>starwars_points:
    print ("you got SPIDERMAN!!! you are very fun and cool! do you like spiders???")
elif harrypotter_points>scottpilgrim_points and harrypotter_points>scream_points and harrypotter_points>snowhite_points and harrypotter_points>spiderman_points and harrypotter_points>it_points and harrypotter_points>starwars_points:
    print ("you got HARRY POTTER!! you love to be cozy and are very magical!! you probably like reading")
elif it_points>scottpilgrim_points and it_points>scream_points and it_points>snowhite_points and it_points>harrypotter_points and it_points>spiderman_points and it_points>starwars_points:
    print ("you got IT!!! you are scary but also kind of funny-like a clown!!")
elif starwars_points>scottpilgrim_points and starwars_points>scream_points and starwars_points>snowhite_points and starwars_points>harrypotter_points and starwars_points>spiderman_points and starwars_points>it_points:
    print ("you got STAR WARS!! you are very cool and probably love space!!")
else:
    print ("you got a tie! i will print your points.")
    print (f"scott pilgrim:{scottpilgrim_points} scream:{scream_points} snow white:{snowhite_points} spiderman:{spiderman_points} harry potter:{harrypotter_points} it:{it_points} star wars:{starwars_points}")
input ()
print ("thank you for doing my quiz!!!!")
print ("I hope you had fun and were happy with your result :3")