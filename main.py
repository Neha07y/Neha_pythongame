git branch -m main main.py
git fetch origin
git branch -u origin/main.py main.py
git remote set-head origin -a
import random

def play_my_game(initial_coins=100):
 

  coins = initial_coins

  while coins > 0:
    print(f"You have {coins} coins.")
    bet = int(input("Enter your bet (0 to quit): "))

    if bet == 0:
      print("You have chosen to quit.")
      break

    if bet > coins:
      print("You cannot bet more coins than you have.")
      continue

    # Generate a random outcome (True for win, False for loss)
    outcome = random.choice([True, False]) 

    if outcome:
      print("You win!")
      coins += bet 
    else:
      print("You lose.")
      coins -= bet

  return coins
if _name_ == "_main_":
  final_coins = play_my_game()
  print(f"You ended the game with {final_coins} coins.")
