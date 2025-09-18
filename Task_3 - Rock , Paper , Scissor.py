import random

def get_user_choice():
    print("\nChoose one: rock, paper, or scissors")
    choice = input("Your choice: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please type rock, paper, or scissors.")
        choice = input("Your choice: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return winner

def main():
    print("==== Welcome to Rock-Paper-Scissors ====")
    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

if __name__ == "__main__":
    main()      