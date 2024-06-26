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

# cat_name is the name of the cat. pretty important if you ask me. used for when the game is talking about the owner's cat.

cat_breed = input(f"now, what kinda cat is {cat_name}? here is a solid choice, ragdoll. or just type the breed you want: ")
condition = True
while True:
    if cat_breed.lower() == "dog":
        delayedprint("This is more of a cat game, y'know? This wasn't really made for dogs...")
        delayedprint("Get outta here.")
        verydelayedprint("GAME OVER! - Wrong animal")
        gameover()
    elif cat_breed == int(1-100):
        print("brother, you've got to put letters. I don't even care if you put like, gibberish.")
    else:
        delayedprint("Alright, lets see here...")
        delayedprint(f"A {cat_breed}. Alright man. Solid choice.")
        break

# cat_breed is the cat's breed. shows up occasionally. small easter egg, 'dog'. does cause the user to restart from the beginning.
cat_age = int(input(f"So, {cat_name} is a {cat_breed}. How old are they in (human) years? "))
if cat_age > 9:
    delayedprint("That cat is probably older than you in cat years.")
elif cat_age > 6:
    delayedprint("That's a mature cat, in age of course, Maybe they still aren't acting mature.")
elif cat_age > 1:
    delayedprint("That's a young cat.")
else:
    print("That's a kitty.")
    
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
delayedprint(f"Now you gotta take care of them, heres all of the ones you need to do, {task_list[0]}.")
delayedprint(f"Let's start with playing with your cat, {cat_name}.")
delayedprint(f"{cat_name} seems to be sitting on the floor, staring at you. You do have some toys, hopefully you choose one they like.")

# this shows the user all the tasks they have to do. pretty easy. also just shoves the user immediately into the tasks.

condition = True
while condition:
    task_list[1] = int(input("Hmm... maybe you can find the right one if you can solve this! 3 + 3 = "))
    
    if task_list[1] == 6:
        delayedprint("Hey! They enjoy it! Maybe a little too much, but they're playing.")
        break  # Exit the loop since the user provided the correct answer
    else:
        delayedprint(f"You slide the toy around, {cat_name} is unfazed. I don't think thats right.")

#some simple math. the while condition thing makes a loop, so if the user gets 3+3 wrong, they can try again. 

task_list[1] = int(input("Alright, they seem to be enjoying playing, you could throw them another toy so they won't get bored, but they seem very invested & focused... You wanna try? 1 for yes, 2 for no. "))

if task_list[1] == 1:
        delayedprint(f"Uh... you accidently throw the toy right at {cat_name}! They look a little angry...")
        delayedprint("I think they might've taken it as a sign of aggression...?")
        delayedprint("Uh oh. I think they're getting ready to jump a-")
        verydelayedprint("GAME OVER! - Death by a thousand scratches")
        gameover()
elif task_list[1] == 2:
    delayedprint("...")
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
delayedprint("Due to reasons outside of your control (no cat food), you have to go shopping.")
verydelayedprint("...")
delayedprint("At the store, you can see some regular cat food, and some gourmet cat food.")
delayedprint("Obviously, that gourmet food is gonna cost a lot. About... $20. The regular costs about $11. That sales tax goes wild.")
money = int(30)
condition = True
while condition:
    task_list[0] = int(input(f"You have 30 dollars. You aren't sure if {cat_name} is a picky eater. How much cash would you have after buying either the gourmet or regular option? $"))
    if task_list[0] == 10:
        money = int(10)
        print("With a heavy heart, you spend 20 bucks on the gourmet food. It's small... but it looks quite nice.")
        delayedprint(f"Back home, you serve it to {cat_name}. They gallop over, and devour it. I guess they didn't really... care about taste.")
        break
    elif task_list[0] == 19:
        money = int(19)
        print("You decide to get the regular food. It looks basic, but it'll probably last for a while. Apparently its for all ages so...")
        delayedprint(f"After realizing you saved 20 dollars, you serve up the food to {cat_name}.")
        verydelayedprint("...")
        print("They eat it. They don't look sad. Or happy. But hey, they're fed at least.")
        break
    else:
        delayedprint("You stand there. You walk along the aisle, searching for a deal. It's all the same. Either the gourmet or the regular.")

# another large wall of text. The number of delayedprint & verydelayedprint commands are due to the fact that theres a lot of sentences to read.
# the money variable is something I thought of, only shows up once really.
# condition = True comes back, this time it makes the user find out how much they'll have after buying either the gourmet or regular cat food.
# its also a loop. since this one requires a little bit more thinking than 3 + 3

delayedprint(f"You've got ${money} left.")
verydelayedprint(f"Good job! You've fed {cat_name}.")
delayedprint(f"For your final task, you've got to pet {cat_name}. Probably one of the most dangerous tasks for a new cat owner.")
print(f"{cat_name} seems to be sun bathing near a window.")
fluffycat = (input(f"Wait, is {cat_name} fluffy? Yes or No? "))
condition = True
while condition:
    if fluffycat.lower() == "yes":
        delayedprint("Oh. Uh...")
        delayedprint(f"{cat_name}'s fur makes them look like a soft pillow or blanket. Or they're just slightly chubby, I dunno.")
        break
    elif fluffycat.lower() == "no":
        delayedprint("Right. They're not fluffy.")
        delayedprint(f"{cat_name} looks sleak & shiny. Probably still squishy anyway. You also wouldn't get as much cat hair everywhere...")
        break
    else:
        delayedprint("You can't really see if they are fluffy or not. Maybe take a closer look?")

# more delayed prints, and a new variable:
# fluffycat. this just changes the text to show that the user's cat is fluffy or not. only affects the next part of code after all this above.
# condition = true comes back again, just to make a loop, since it's just easy to make and fits the context here.

print("Anyway, it's time to interrupt their photosynthesis, and pet them.")
task_list[2] = int(input(f"To find out where {cat_name} likes to be pet, you gotta take a guess... what was does 3 * 3 = "))
if task_list[2] == 9:
    print("You let them sniff your hand...")
    delayedprint("They seem to approve of your bravery. They relax a little.")
else:
    delayedprint("You start petting them immediately.")
    delayedprint("In the moment, it seemed like a good idea.")
    verydelayedprint("It was not.")
    delayedprint("You're pretty sure you saw your hand get disconnected from your arm immediately. At least before you went into shock.")
    verydelayedprint("GAME OVER! - Hand privilege removed")
    gameover()

# another math question, this time its just 3*3. I would put some text if someone put 6, but im too lazy for that.
# and its also leads to a game over if done improperly.

if fluffycat == "yes":
    print(f"You pet that fluffy cat, by petting it's head slowly but lovingly. {cat_name} starts purring loudly. They enjoy it!")
else:
    print(f"You pet that smooth cat ambidextrously. {cat_name} starts purring loudly, they like it!")

# heres where fluffycat comes into play, just a quick sentence telling the user how they pet their cat.

print(f"Soon enough, {cat_name} starts to trust you more. They lay on their back.")
delayedprint("Your final challenge. Rub their belly without getting mauled or having your fingers bitten off. (good luck)")

task_list[2] = int(input("(hint, PEMDAS) What does 6*3(3-1)=?: "))
if task_list[2] == 36:
    delayedprint("You pet them without any fear in mind. You knew the risks.")
    print("Yet the cat allows you. You are worthy.")
else:
    print("...")
    verydelayedprint("You rub their belly. It's soft & warm... but something feels off.")
    delayedprint(f"Fear strikes you, as you look up at {cat_name}")
    print("In an instant, they jump up, their claws are out, and their mouth is open.")
    delayedprint("They chomp right onto your arm, taking a comically large chunk out of it.")
    verydelayedprint("GAME OVER! - Actual skill issue")
    gameover()

# the grand challenge, math. its pemdas. 3-1 = 2. 6*3 = 18, 18*2 = 36.
# why is this the hardest? rubbing a cat's belly is one of, if not the hardest thing you can do to a cat you've just got.
# it's their weakspot, since pretty much most of their organs are there.

verydelayedprint("...")
print(f"Great job. You've succesfully taken care of {cat_name}, a {cat_age} year old {cat_breed}. You have a total of ${money} left.")
verydelayedprint("Thank you for playing, my first coded game.")
print("The game will restart if you want to.")
condition = True
while True:
    end = int(input("Type 1 to restart. Type 2 to see your cat information."))
    if end == 1:
        delayedprint(f"Thank you again. Even if {cat_name} won't be on this game soon, doesn't mean you'll forget about them. Probably.")
        verydelayedprint("GAME OVER! - Certified Cat Owner")
        gameover()
    elif end == 2:
        print("That's fair.")
        if fluffycat == "yes":
            delayedprint(f"Your cat's name is {cat_name}. They are a fluffy {cat_breed}, and is {cat_age} year(s) old.")
        else:
            delayedprint(f"Your cat's name is {cat_name}. They are a smooth {cat_breed}, and is {cat_age} year(s) old.")
            
# and there we go, the end of cat game. it gives the user the choice of resetting, or seeing some last information about their cat.
# still, the game ends anyway, since its a loop, and theres only 2 options.
