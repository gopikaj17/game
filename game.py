import random

user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

while True:
    print("\n--- Rock, Paper, Scissors Game ---")
    
    user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user_choice == 'exit':
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    outcome = {
        ('rock', 'paper'): 'Computer wins!',
        ('paper', 'rock'): 'You win!',
        ('scissors', 'paper'): 'You win!',
        ('paper', 'scissors'): 'Computer wins!',
        ('scissors', 'rock'): 'Computer wins!',
        ('rock', 'scissors'): 'You win!',
    }

    result = outcome.get((user_choice, computer_choice), "It's a tie!")
    print(result)

    user_score += result.count('You')
    computer_score += result.count('Computer')

    print(f"\nScore - You: {user_score} | Computer: {computer_score}")
