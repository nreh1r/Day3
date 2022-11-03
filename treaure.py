print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
choice_1 = input("Do you want to go \"left\" or \"right\"? ")

if choice_1.lower() == "right":
    print("Game Over.")
elif choice_1.lower() == "left":
    choice_2 = input(
        "You arrive at a lake.\n Do you want to 'swim' or 'wait' for a boat? ")
    if choice_2.lower() == "swim":
        print("Game Over.")
    elif choice_2.lower() == "wait":
        choice_3 = input(
            "You arrive on an island with three doors, Red, Yellow, and Blue.\n Which door do you choose? ")
        if choice_3.lower() == "red":
            print("Game Over.")
        elif choice_3.lower() == "yellow":
            print("You Win!")
        elif choice_3.lower() == "blue":
            print("Game Over.")
