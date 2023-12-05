import os
import sys

def gameover():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# this is used to reset the whole program, pretty much just puts the user all the way to the beginning, naming their cat.

import time
def delayedprint(text, delay = 2.5):
    print(text)
    time.sleep(delay)

def verydelayedprint(text, delay = 5):
    print(text)
    time.sleep(delay)
    
# since the game is mainly reading, this gives the user some, or a lot of time to read.
print("Welcome to cat game. It's a game about taking care a of a cat you make. Try not to mess up. A single mistake could lead to your demise. Not the cat though.")
cat_name = input("Please enter the name of the cat you wanna take care of: ")
delayedprint(f"'{cat_name}', huh? Very interesting... but alright.")

# cat_name is the name of the cat. pretty important if you ask me. used for when the game is talking about the owner's cat

cat_breed = input(f"now, what kinda cat is {cat_name}? here is a solid choice, ragdoll. or just type the breed you want: ")

if cat_breed.lower() == "dog":
    delayedprint("This is more of a cat game, y'know? This wasn't really made for dogs...")
    delayedprint("Get outta here.")
    verydelayedprint("GAME OVER! - Wrong animal")
    gameover()
else:
    delayedprint("Alright, lets see here...")
    delayedprint(f"A {cat_breed}. Alright man. Solid choice.")

# cat_breed is the cat's breed. shows up occasionally. small easter egg, 'dog'. does cause the user to restart from the beginning.
    
cat_age = int(input(f"So, {cat_name} is a {cat_breed}. How old are they in years? "))

if cat_age > 9:
    delayedprint("That cat is probably older than you in cat years.")
elif cat_age > 6:
    delayedprint("That's a mature cat, in age of course, Maybe they still aren't acting mature.")
elif cat_age > 2:
    delayedprint("That's a young cat.")
else:
    print("That's probably a pretty young cat. Still a baby practically...")
    
# cat_age is uncommonly used. it's just to see how young/old the cat is. some small flavor text added.
    
delayedprint(f"Alright, your the new, possibly proud owner of '{cat_name}', a {cat_age} year old {cat_breed}.")
worthiness = int(input("Now, type 1 if you're ready. Or 2 if you're not. "))
if worthiness == 1:
    delayedprint("Good, i always believed in you.")
    delayedprint("Lets begin.")
elif worthiness == 2:
    delayedprint("Unfortunate. Well, it was nice having you here.")
    verydelayedprint("GAME OVER - Skill issue")
    gameover()
else:
    delayedprint("uh... alright. you aren't that good at following directions.")
    verydelayedprint("GAME OVER - what are you even doing")
    gameover()

# worthiness... this is more of a joke kinda thing, but it's still funny. if the user isn't ready to start, game restarts. or if they put the wrong thing, game restarts.

task_list = [ "Feeding", "Playing", "Petting" ]
feedtask = task_list[0]
playtask = task_list[1]
pettask = task_list[2]
delayedprint(f"Now you gotta take care of them, heres all of the ones you need to do, {task_list}.")
delayedprint(f"Let's start with playing with your cat, {cat_name}.")
delayedprint(f"{cat_name} seems to be sitting on the floor, staring at you. You do have some toys, hopefully you choose one they like.")

# this shows the user all the tasks they have to do. pretty easy. also just shoves the user immediately into the tasks.

condition = True
while condition:
    playtask = int(input("Hmm... maybe you can find the right one if you can solve this! 3 + 3 = "))
    
    if playtask == 6:
        print("Hey! They enjoy it! Maybe a little too much, but they're playing.")
        break  # Exit the loop since the user provided the correct answer
    else:
        print("That wasn't right. Try again!")

#some simple math. the while condition thing makes a loop, so if the user gets 3+3 wrong, they can try again. 

playtask = int(input("Alright, they seem to be enjoying playing, you could throw them another toy so they won't get bored, but they seem very invested... You wanna try? 1 for yes, 2 for no. "))

if playtask == 1:
        delayedprint(f"Uh... you accidently throw the toy right at {cat_name}! They look a little angry...")
        delayedprint("I think they might've taken it as a sign of aggression...?")
        delayedprint("Uh oh. I think they're getting ready to jump a-")
        verydelayedprint("GAME OVER! - Death by a thousand scratches")
        gameover()
elif playtask == 2:
    delayedprint("Eh... they're probably fine with just that toy. Maybe.")
else:
    print("Instead of deciding anything, you stare at your cat. They take note of your presense.")
    delayedprint("You stare at them, their eyes dilating, looking more as dark marbles...")
    verydelayedprint("You're lost in the void. Are you even standing right now? Were you looking at something?")
    delayedprint("No. You weren't.")
    delayedprint("GAME OVER! - Lost in the sauce")
    gameover()

# ignoring the wall of text, this is just similar to the worthiness thing. except with play task. only 1 right answer, other 2 lead to death for the user.
# and by death i mean they restart.

delayedprint(f"Good job! You've successfully played with {cat_name}. You're so good, you did it first try! (hopefully)")
verydelayedprint("I'd say that your cat looks pretty hungry. We- You, should take care of that.")
delayedprint("Due to reasons outside of your control, you have to go shopping.")
verydelayedprint("...")
delayedprint("At the store, you can see some regular cat food, and some gourmet cat food.")
delayedprint("Obviously, that gourmet food is gonna cost a lot. About... $20. The regular costs about $11.")

condition = True
while condition:
    feedtask = int(input(f"You have 30 dollars. You aren't sure if {cat_name} is a picky eater. How much cash would you have after buying either the gourmet or regular option? $"))
    if feedtask == 10:
        print("With a heavy heart, you spend 20 bucks on the gourmet food. It's small... but it looks quite nice.")
        delayedprint(f"Back home, you serve it to {cat_name}. They gallop over, and devour it. I guess they didn't really... care about taste.")
        break
    elif feedtask == 19:
        print("You decide to get the regular food. It looks basic, but it'll probably last for a while. Apparently its for all ages so...")
        delayedprint(f"After realizing you saved 20 dollars, you serve up the food to {cat_name}.")
        verydelayedprint("...")
        print("They eat it. They don't look sad. Or happy. But hey, they're fed at least.")
        break
    else:
        print("You stand there. You walk along the aisle, searching for a deal. It's all the same. One or the other...")
