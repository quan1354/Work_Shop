import random

lower_num, higher_num = 1, 10
random_number = random.randint(lower_num, higher_num)
print(f"Gessing Number between {lower_num} To {higher_num}")

gameRound = 10 - 1
gameActive = True

while gameActive:
    try:
        number = int(input("Enter Your Number Guess>"))
    except ValueError as e:
        print(e)

    if gameRound <=0:
        print("Your Round is End, You Lost the game")
        gameActive = False

    if number < random_number:
        print("Your Guess is Lower than Target")
    elif number > random_number:
        print("Your Guess is Larger than Target")
    else:
        print("Your Guess is correctly, You win this game")
        gameActive = False
    
    gameRound -=1