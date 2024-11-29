import random

target = random.randint(1, 100)

while True:
    userchoice = input("Guess the target or quit!!: ")
    if userchoice.lower() == "quit":
        print("--game over--")
        break
    
    userchoice = int(userchoice)
    
    if userchoice == target:
        print("Success: Correct guess!!")
        print("--game over--")
        break
    elif userchoice < target:
        print("Your number was too small, take a bigger guess.")
    else:
        print("Your number was too big, take a smaller guess.")

