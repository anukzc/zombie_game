# Author: Anuk Centellas
# Date: 3/4/2023
# Description: Zombie Game for Zombies in America Honors Seminar Version 2

import random
cont = True

"""
good_input validates the user input that matches requirements, and if not, asks again
parameter: prompt as string, requirement as string that's either "digit" or "single"
return a good input
"""
def goodInput(prompt, req):
    askAgain = True
    while askAgain == True:
        userInput = input(prompt)
        if req == "single":
            if len(userInput) == 1 and (userInput == "x" or userInput == "y" or userInput == "z"):
                askAgain = False
            else:
                print("Please type x, y, or z")
        elif req == "digit":
            if userInput.isdigit() == True and (userInput == "0" or userInput == "1" or userInput == "2" or userInput == "3" or userInput == "4" or userInput == "5"):
                askAgain = False
            else:
                print("Please type a number to indicate your choice.")
    return(userInput)

# function to keep track of how many zombies are left
def zombiesLeft(killed, zombies):
    zombies = zombies - killed
    # if there are less than 0 zombies, reset zombies to 0
    if zombies < 0:
        zombies = 0
        cont = False
        killed = "all of the"
    print("You killed " + str(killed) + " zombies!")
    print("Zombies Left: " + str(zombies))
    return(zombies)

# function to keep track of losing health from attacking zombies
def healthDown(hp, health):
    health = health - hp
    # if health is less than 0, reset it to 0
    if health < 0:
        health = 0
    print("Health: " + str(health))
    return(health)
    
#function to keep track of increasing health from eating food
# def healthUp(eat, health):
#     #only lets user eat if eating won't make their health go over 100
#     if health + (eat*10) <= 100:
#         health = health + (eat*10)
#     else:
#         print("Your health is not low enough to eat that much")
#     print("Health: " + str(health))
#     return(health)

if __name__ == '__main__':
# entire game loop
    playAgain = True
    while playAgain == True:
        print("When asked a question, enter the number that is in parentheses next to the answer you want to choose.\n")
        print("Welcome to the zombie apocalypse! You are on a remote island with 100 zombies, you have 100 health, 2 cans of food, and your goal is to safely escape the island. The zombies won't attack you unless you attack them, but you cannot leave the island until there are no more zombies. Each can of food can heal you 10 points. You must now make some critical choices... PS, the zombies' favorite number is zero...")
        zombies = 100
        health = 100
        friends = 0
        cans = 2
        humansTotal = 0
        ammo = 1
        killed = 0
        hp = 0
        # weapon selection
        print("\nYou wake up in a collapsing shed in the woods with three weapons, but you only have the capacity to take one.")
        w = int(goodInput("Choose your weapon, knife (1) (which can also be used as a tool), axe (2) (which can kill more zombies), or rifle (3) (which lets you attack from a distance). If you choose the rifle, you start with 1 ammo, which can kill multiple zombies, and can find more later: ", "digit"))
        if w == 4 or w == 5 or w == 0:
            w = int(goodInput("Choose your weapon, knife (1) (which can also be used as a tool), axe (2) (which can kill more zombies), or rifle (3) (which lets you attack from a distance) If you choose the rifle, you start with 1 ammo, which can kill multiple zombies, and can find more later: ", "digit"))
        if w == 1:
            weapon = "knife"
        elif w == 2:
            weapon = "axe"
        elif w == 3:
            weapon = "rifle"
        print("Your weapon: " + weapon)

        # general game loop
        print("\nYou hear zombies in the woods around you, so you must decide what to do next: ")
        while cont == True:
            # first checks if you've won the game
            if zombies == 0:
                print("You have succeeded and can now escape the island!")
                break
            if health == 0:
                print("Your health got to 0 and you died :(")
                break
            # if user chose rifle, add option to look for ammo
            if w == 3:
                choice1 = int(goodInput("\nWould you like to fight the zombies (1), look for food (2), look for other humans (3), eat food (4), or look for ammo (5) (one ammo gives you one chance to fight the zombies and will kill multiple)? ", "digit"))
            else:
                choice1 = int(goodInput("\nWould you like to fight the zombies (1), look for food (2), look for other humans (3), or eat food (4)? ", "digit"))
            # if user enters 5 (ammo) but didn't pick the rifle
            if choice1 == 5 and w != 3:
                while choice1 == 5:
                    choice1 = int(goodInput("Would you like to fight the zombies (1), look for food (2), look for other humans (3), or eat food (4)? ", "digit"))
        
        # if the user chose to fight zombies
            if choice1 == 1:
                # knife
                if w == 1:
                    # if user has less than 5 friends they die
                    if friends < 5:
                        print("You do not have a strong enough weapon or enough friends and the zombies overpower you and kill you :( ")
                        break
                    # if user has 5 or more friends they kill some zombies
                    else:
                        killed = random.randint(12, 22) + int(killed/4)
                        zombies = zombiesLeft(killed, zombies)
                        hp = random.randint(15, 25) + int(hp/3)
                        health = healthDown(hp, health)
                # axe
                elif w == 2:
                    # if user has less than 3 friends they die
                    if friends < 3:
                        print("You do not have a strong enough weapon or enough friends and the zombies overpower you and kill you :( ")
                        break
                    # if user has 3 or more friends they kill some zombies
                    else:
                        killed = random.randint(17, 27) + int(killed/4)
                        zombies = zombiesLeft(killed, zombies)
                        hp = random.randint(20, 30) + int(hp/3)
                        health = healthDown(hp, health)
                # rifle, always able to kill some zombies
                elif w == 3:
                    if ammo > 0:
                        ammo -= 1
                        killed = random.randint(7, 17) + int(killed/4)
                        zombies = zombiesLeft(killed, zombies)
                        hp = random.randint(10, 20) + int(hp/3)
                        health = healthDown(hp, health) 
                        print("Ammo: " + str(ammo))
                    elif ammo == 0 and friends < 6:
                        print("You don't have any ammo! The zombies see that you tried to attack them and kill you :(")
                        break
                    elif ammo == 0 and friends > 6:
                        print("Even though you don't have ammo, your friends are able to fight off the zombies and save you from being killed")
                        killed = random.randint(5, 15) + killed
                        zombies = zombiesLeft(killed, zombies)
                        hp = random.randint(30, 40)
                        health = healthDown(hp, health)
            # if user chose to find food
            elif choice1 == 2:
                # if user has 4 or more cans, they don't find more
                if cans >= 4:
                    print("You don't find any more food :( You have " + str(cans) + " cans of food.")
                else:
                    container = random.randint(2,4)
                    print("You find 1 single can of food and a container with " + str(container) + " more in it.")
                    cans += 1
                    # if user chose knife, they are able to open the container and get more food
                    if w == 1:
                        cans += container
                        print("Since you have the knife, you are able to open the container without breaking the cans! You now have " + str(cans) + " cans.")
                    # if user chose axe or rifle, they are not able to open the container
                    else:
                        print("Your weapon will break the cans, so you cannot open the container and can only take the single can. You now have " + str(cans) + " cans.")                
                    
            # if user chose to find other humans
            elif choice1 == 3:
                humans = random.randint(1, 5)
                humansTotal += humans
                if humansTotal > 20:
                    print("There are no more humans on the island.")
                else:
                    print("You come across " + str(humans) + " humans in the woods.")
                    humansChoice = int(goodInput("Do you want to attack the humans (1), or befriend them (2)? ", "digit"))
                    # incase user types 3 or 4 or 5
                    while humansChoice == 3 or humansChoice == 4 or humansChoice == 5: 
                        humansChoice = int(goodInput("Do you want to attack the humans (1), or befriend them (2)? ", "digit"))
                    # if user chose to attack the humans
                    if humansChoice == 1:
                        # if user has knife
                        if w == 1:
                            # if user has 5 or more friends, they kill the humans
                            if friends >= 5:
                                print("Your weapon/team is strong enough and you are able to kill the humans and find " + str(int(friends/4)) + " cans of food!")
                                cans += int(friends/4)
                            # if user has less than 5 friends, they die
                            else:
                                print("You are not strong enough to take on the humans and they kill you.")
                                break
                        # axe
                        elif w == 2:
                            # 3 or more friends, kill humans
                            if friends >= 3:
                                print("Your weapon/team is strong enough and you are able to kill the humans and find " + str(int(friends/4)) + " cans of food!")
                                cans += int(friends/4)
                            # less than 3 friends, die
                            else:
                                print("You are not strong enough to take on the humans and they kill you.")
                                break
                        # rifle
                        elif w == 3:
                            # always kill huamans
                            print("You kill the humans from a distance and find " + str(friends + 1) + " cans of food in their supplies.")
                            cans += friends + 1
                    # if user chose to befriend humans
                    elif humansChoice == 2:
                        print("You become friends with the new humans and now have " + str(friends + humans) + " friends!")
                        friends += humans
            # if user chose to eat food
            elif choice1 == 4:
                eat = input("How many cans of food would you like to eat? Your health is currently " + str(health) + " and you have " + str(cans) + " cans of food. ")
                # if user does not type in a number
                while eat.isdigit() == False:
                    eat = input("Please enter a number: ")
                # if user types more cans than they have
                while (int(eat) > cans):
                    eat = input("You don't have that many cans, please enter a different number: ")
                    # if user does not type in a number
                    while eat.isdigit() == False:
                        eat = input("Please enter a number: ")
                eat = int(eat)
                # only lets user eat if eating won't make their health go over 100
                if health + (eat*10) <= 100:
                    health = health + (eat*10)
                    cans -= eat
                else:
                    print("Your health is not low enough to eat that much.")
                print("Health: " + str(health))
            # if user chooses to find ammo
            elif choice1 == 5 and w == 3:
                # if user has 3 or more ammo and has killed 15 or less zombies, they don't find more
                if ammo >= 3 and killed <= 15:
                    print("You don't find any more ammo :(")
                else:
                    ammoFound = random.randint(1,3)
                    ammo += ammoFound
                    print("You find " + str(ammoFound) + " ammo. You now have " + str(ammo) + " ammo.")
            # if user enters 0
            elif choice1 == 0:
                print("You have chosen to take a risk and try to cure the zombies!")
                if zombies >= 70:
                    print("Your motives are trusted and you are able to cure the zombies! You can all escape the island!")
                    break
                elif zombies < 70:
                    print("You have already killed too many zombies, so your motives are not trusted and you cannot cure them. The only way to escape now is to kill them all.")
        # after general loop ends      
        again = int(goodInput("Do you want to play again? yes (1) no (2) ", "digit"))
        while again == 3 or again == 4 or again == 5 or again == 0:
            again = int(goodInput("Do you want to play again? yes (1) no (2) ", "digit"))
        # if user chose not to play again, entire game loop ends
        if again == 2:
            print("Thank you for playing!")
            playAgain = False