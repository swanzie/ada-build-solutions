#rock paper scissors v4 - change choose_rps() to use a list
import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    options = ['rock', 'paper', 'scissors']
    r = random.randint(0,2)
    return options[r]
   
def rps(player1, player2):
  """
  input: player1 and player2 -> 'rock', 'paper', 'scissors'
  output: "Player 1 is the winner", "Player 2 is the winner", "it's a tie"
  """
  #tie
  if player1 == player2:
    print ("it's a tie")
  #if player1 is rock
  elif player1 == 'rock': 
    if player2 == 'paper':
      print("player2 is the winner")
    else:
      print("player 1 is the winner")
  #if player1 is paper
  elif player1 == 'paper':
    if player2 == 'rock':
      print("player1 is the winner")
    else:
      print("player2 is the winner")
  #if player1 is scissors
  elif player1 == 'scissors':
    if player2 == 'rock':
      print("player2 is the winner")
    else:
      print("player1 is the winner")

def play_again():
  n = random.randint(0,1)
  if n == 0:
    return False
  return True

play = True

print("Welcome to Rock, Paper, Scissors!\n")
print("---\n")

#number of times playing the game
r = random.randint(1, 10)
print(f"we are playing {r} times\n")
for i in range(r):
    player1 = choose_rps()
    print("Player1 chose", player1)
    player2 = choose_rps()
    print(f"Player2 chose {player2}\n")
    rps(player1, player2)
    print("\n---\n")

    play = play_again()
print("Thank you for playing!")  