import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    print("Welcome to Rock, Paper, Scissors!")
    print("Available choices: rock, paper, scissors")

    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        print(determine_winner(user_choice, computer_choice))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    rock_paper_scissors()
