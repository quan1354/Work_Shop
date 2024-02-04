from random import choice

def run_game ():
    target = choice(['Warrior', 'Archor', 'Wizard'])
    player = input("Enter your name>")
    print(f'Welcome to Hangman, {player}', end="\n")
    
    guessed_letters = set()
    attempts_remaining = 3

    while attempts_remaining > 0:
       # Display the current state of the word
        display_word = [char if char in guessed_letters else '_' for char in target]
        print("Word:", ' '.join(display_word))

        if '_' not in display_word:
            print("Congratulations! You win!")
            break

        user_guess = input("Enter a letter: ")

        # Input validation
        if not user_guess.isalpha() or len(user_guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if user_guess in guessed_letters:
            print(f"You already used {user_guess}. Please enter another letter.")
            continue

        guessed_letters.add(user_guess)

        if user_guess not in target:
            attempts_remaining -= 1
            print(f"Sorry, that was wrong... ({attempts_remaining} tries remaining)")
            if attempts_remaining == 0:
                print("No more tries remaining... You lose.")
                print(f"The word was: {target}")
                break

    return ''

if __name__ == '__main__':
    run_game()