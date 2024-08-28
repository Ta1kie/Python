import random

rock =  """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

player_choice = int(input('Choose 0 for Rock, 1 for Paper or 2 for Scissors\n'))
print(game_images[player_choice])
opponent_choice = random.randint(0, 2)
print(f'Computer chose: ')
print(game_images[opponent_choice])

if player_choice >= 3 or player_choice < 0:
    print('You typed an invalid number. You lose!')
elif opponent_choice == 0 and opponent_choice == 2:
    print('You win!')
elif opponent_choice == 0 and player_choice ==2:
    print('You lose')
elif opponent_choice > player_choice:
    print('You lose!')
elif player_choice > opponent_choice:
    print('You win!')
elif opponent_choice == player_choice:
    print('It is a draw!')
