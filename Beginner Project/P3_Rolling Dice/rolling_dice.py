import random


def roll_dice(num_dice):
    # Check Parameter Valid
    if num_dice < 0:
        raise ValueError

    # Dice 1-6, then store in array
    roll = [random.randint(1,6) for _ in range(num_dice)]
    # roll = []
    # for i in range(num_dice):
    #     num = random.randint(1,6)
    #     roll.append(num)
    return roll

def main():
    while True:
        try:
            user_input = input("How Many Dice You Want To Roll >")
            if user_input.lower() == "exit":
                print("Thanks for your playing")
                break
            user_input = 2 if user_input.strip() == "" else int(user_input)
            result = roll_dice(user_input)
            # Unpacking elements, avoid print as a single object that including [] and quote around.
            print(*result, sep=",")
            sum_result = sum(result)
            print(f"The Total Sum of Dices is {sum_result}")
        except ValueError as e:
            print(e)

    return ""

if __name__ == '__main__':
    main()