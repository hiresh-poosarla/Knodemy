import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
        
while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
