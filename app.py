import random

player_score = 0
computer_score = 0

rounds = 3

choices = ['rock', 'paper', 'scissors']

outcomes = ['win', 'lose', 'draw']

player_choice = ''
computer_choice = ''
outcome = ''
message = ''

# Set up the game loop by iterating over the number of rounds
for round in range(rounds):
    # Get the player's choice
    player_choice = input('Enter your choice (rock, paper, scissors): ')
    # Validate the player's choice
    while player_choice not in choices:
        player_choice = input('Invalid choice. Enter your choice (rock, paper, scissors): ')
    
    # Get the computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the outcome of the game
    if player_choice == computer_choice:
        outcome = 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        outcome = 'win'
    else:
        outcome = 'lose'
    
    # Update the player's score and the computer's score based on the outcome
    if outcome == 'win':
        player_score += 1
    elif outcome == 'lose':
        computer_score += 1
    
    # Display the outcome of the game to the player
    if outcome == 'draw':
        message = 'It\'s a draw!'
    elif outcome == 'win':
        message = 'You win!'
    else:
        message = 'You lose!'
    
    print(f'Player: {player_choice}, Computer: {computer_choice}, Outcome: {message}')
print(f'Player score: {player_score}, Computer score: {computer_score}')    
    