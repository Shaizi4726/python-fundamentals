import random


def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    print("Welcome to the Number Guessing Game!")

    while True:
        attempts = 1
        number_to_guess = random.randint(1, 100)

        guessed_number = int_input(
            "I have selected a number between 1 and 100. Can you guess it? ")

        while guessed_number != number_to_guess:
            attempts += 1
            if guessed_number < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

            guessed_number = int_input("Try again: ")

        print(
            f"🎉 Correct! You got it in {attempts} attempt(s).")

        play_again = ""

        while play_again not in ["yes", "no"]:
            play_again = input(
                "Do you want to play again? (yes/no): ").strip().lower()

        if play_again == "yes":
            print("Great! Let's play again!")
        elif play_again == "no":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
