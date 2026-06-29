import random


spot_1 = 0
spot_2 = 0
spot_3 = 0
spot_4 = 0
spot_5 = 0
spot_6 = 0
spot_7 = 0
spot_8 = 0
spot_9 = 0

one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "

print(" ")
print(f" {one} | {two} | {three} ")
print("--- --- ---")
print(f" {four} | {five} | {six} ")
print("--- --- ---")
print(f" {seven} | {eight} | {nine} ")

# Makes functions to shotrten the code  
def Player_Move():
# Makes the variables global so they can be used in the function    
    global spot_1
    global spot_2
    global spot_3
    global spot_4
    global spot_5
    global spot_6
    global spot_7
    global spot_8
    global spot_9

    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

# Number import
    move = int(input("Enter your spot: "))

# Makes sure the spot is not already taken
    if move == 1:
        if spot_1 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_1 = 3
            one = "X"

    if move == 2:
        if spot_2 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_2 = 3
            two = "X"

    if move == 3:
        if spot_3 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_3 = 3
            three = "X"

    if move == 4:
        if spot_4 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_4 = 3
            four = "X"

    if move == 5:
        if spot_5 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_5 = 3
            five = "X"

    if move == 6:
        if spot_6 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_6 = 3
            six= "X"
    if move == 7:
        if spot_7 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_7 = 3
            seven = "X"

    if move == 8:
        if spot_8 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_8 = 3
            eight = "X"        

    if move == 9:
        if spot_9 != 0:
            move = int(input("Spot already taken. Please choose another spot: "))
        else:
            spot_9 = 3
            nine = "X"
# Prints the board after the player makes a move.
    print(" ")
    print("Player's Move: ")
    print(f" {one} | {two} | {three} ")
    print("--- --- ---")
    print(f" {four} | {five} | {six} ")
    print("--- --- ---")
    print(f" {seven} | {eight} | {nine} ")

def Bot_Move():

# Makes the variables global so they can be used in the function    
    global spot_1
    global spot_2
    global spot_3
    global spot_4
    global spot_5
    global spot_6
    global spot_7
    global spot_8
    global spot_9

    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

# Generates a random number between 1 and 9 and repeates it till it finds a spot    
    while True:
        number = random.randint(1, 9)

# Makes sure the spot is not already taken
        if number == 1:
            if spot_1 == 0:
                spot_1 = 5
                one = "O"
                break
            else:
                pass

        if number == 2:
            if spot_2 == 0:
                spot_2 = 5
                two = "O"
                break
            else:
                pass

        if number == 3:
            if spot_3 == 0:
                spot_3 = 5
                three = "O"
                break
            else:
                pass

        if number == 4:
            if spot_4 == 0:
                spot_4 = 5
                four = "O"
                break
            else:
                pass

        if number == 5:
            if spot_5 == 0:
                spot_5 = 5
                five = "O"
                break
            else:
                pass

        if number == 6:
            if spot_6 == 0:
                spot_6 = 5
                six = "O"
                break
            else:
                pass
        if number == 7:
            if spot_7 == 0:
                spot_7 = 5
                seven = "O"
                break
            else:
                pass
                
        if number == 8:
            if spot_8 == 0:
                spot_8 = 5
                eight = "O"
                break
            else:
                pass

        if number == 9:
            if spot_9 == 0:
                spot_9 = 5
                nine = "O"
                break
            else:
                pass
  
# Prints the board after the bot makes a move.  
    print(" ")
    print("Bot's Move: ")
    print(f" {one} | {two} | {three} ")
    print("--- --- ---")
    print(f" {four} | {five} | {six} ")
    print("--- --- ---")
    print(f" {seven} | {eight} | {nine} ")

def Check_Winner():
    
    global spot_1
    global spot_2
    global spot_3
    global spot_4
    global spot_5
    global spot_6
    global spot_7
    global spot_8
    global spot_9

# Check if the player has won
    if spot_1 + spot_2 + spot_3 == 9:
        print("You Win!")
        exit()
    if spot_4 + spot_5 + spot_6 == 9:
        print("You Win!")
        exit()
    if spot_7 + spot_8 + spot_9 == 9:
        print("You Win!")
        exit()
    if spot_1 + spot_4 + spot_7 == 9:
        print("You Win!")
        exit()
    if spot_2 + spot_5 + spot_8 == 9:
        print("You Win!")
        exit()
    if spot_3 + spot_6 + spot_9 == 9:
        print("You Win!")
        exit()
    if spot_1 + spot_5 + spot_9 == 9:
        print("You Win!")
        exit()
    if spot_3 + spot_5 + spot_7 == 9:
        print("You Win!")
        exit()
#Checking if Bot wins
    if spot_1 + spot_2 + spot_3 == 15:
        print("Bot Wins!")
        exit()
    if spot_4 + spot_5 + spot_6 == 15:
        print("Bot Wins!")
        exit()
    if spot_7 + spot_8 + spot_9 == 15:
        print("Bot Wins!")
        exit()
    if spot_1 + spot_4 + spot_7 == 15:
        print("Bot Wins!")
        exit()
    if spot_2 + spot_5 + spot_8 == 15:
        print("Bot Wins!")
        exit()
    if spot_3 + spot_6 + spot_9 == 15:
        print("Bot Wins!")
        exit()
    if spot_1 + spot_5 + spot_9 == 15:
        print("Bot Wins!")
        exit()
    if spot_3 + spot_5 + spot_7 == 15:
        print("Bot Wins!")
        exit()
    if spot_1 + spot_2 + spot_3 + spot_4 + spot_5 + spot_6 + spot_7 + spot_8 + spot_9 == 35:
        print("It's a Tie!")
        exit()

Player_Move()
Check_Winner()
Bot_Move()
Check_Winner()
Player_Move()
Check_Winner()
Bot_Move()
Check_Winner()
Player_Move()
Check_Winner()
Bot_Move()
Check_Winner()
Player_Move()
Check_Winner()
Bot_Move()
Check_Winner()
Player_Move()
Check_Winner()