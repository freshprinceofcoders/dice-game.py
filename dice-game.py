import random
dice = random.randint(1,6)
print("WELCOME TO THE DICE GAME!!!!!!!!")
print("only use yes")
print("Your number is...")
print(dice)
roll_again = input("Do you want to roll again? ")

while roll_again == "yes" or "y" or "YES" or "Y":
    print("Your number is...")
    print(random.randint(1,6))
    roll_again = input("Do you want to roll again? ")
    if roll_again == "yes":
        continue
    else:
        print("BYE!!!!!")
        exit()
    
    
    


