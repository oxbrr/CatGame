import os
import sys

def gameover():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# this is used to reset the whole program, pretty much just puts the user all the way to the beginning, naming their cat.
import time
def delayedprint(text, delay = 2):
    print(text)
    time.sleep(delay)
    
# since the game is mainly reading, giving the user a few seconds to finish reading is nice. I Love Reading So Much...
    
cat_name = input("welcome to cat game, please enter the name of the cat you wanna take care of: ")
delayedprint(f"'{cat_name}', huh? Very interesting... but alright.")

cat_breed = input(f"now, what kinda cat is {cat_name}? here is a solid choice, ragdoll. or just type the breed you want: ")

if cat_breed.lower() == "dog":
    print("This is more of a cat game, y'know? This wasn't really made for dogs...")
    delayedprint("Get outta here.")
    gameover()
    
else:
    print("Alright, lets see here...")
    delayedprint(f"A {cat_breed}. Alright man. Solid choice.")
    
cat_age = int(input(f"So, {cat_name} is a {cat_breed}. How old are they in years? "))

# this is just a quick side note, no relation to the code or anything. by default, inputs are taken as string. i can write int(, float(, or boolean() on the input to specify what data type it is.

if cat_age > 10:
    print("That cat is probably older than you in cat years.")
elif cat_age > 6:
    print("That's a mature cat, in age of course, Maybe they still aren't acting mature.")
elif cat_age > 2:
    print("That's a young cat.")
else:
    print("That's probably a pretty young cat. Still a baby practically...")
    
print(f"Alright, your the new, possibly proud owner of '{cat_name}', a {cat_age} year old {cat_breed}.")
worthiness = int(input("Now, type 1 if you're ready. Or 2 if you're not. "))
if worthiness == 1:
    print("Good, i always believed in you.")
    print("Lets begin.")
elif worthiness == 2:
    print("Unfortunate. Well, it was nice having you here.")
    print("GAME OVER - Skill issue")
else:
    print("uh... alright. you aren't that good at following directions.")
    print("GAME OVER - what are you even doing")

task_list = [ "Feeding", "Playing", "Petting" ]
feedtask = task_list[0]
playtask = task_list[1]
pettask = task_list[2]
delayedprint(f"Now you gotta take care of them, heres all of the ones you need to do, {task_list}.")
delayedprint(f"Let's start with playing with your cat, {cat_name}.")
delayedprint(f"{cat_name} seems to be sitting on the floor, staring at you. You do have some toys, hopefully you choose one they like.")

playtask = int()