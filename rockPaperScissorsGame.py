import random,sys
print(' ROCK, PAPER, SCISSORS ')

wins=0
losses=0
ties=0

while True:
    print('%s wins, %s loss, %s ties' % (wins,losses,ties))

    while True:
      print(' Enter Your Move: (r)ock (p)aper (s)cissors ')
      playerMove= input()

      if playerMove == 'q':
        sys.exit()
      if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
        break
      print(' Type One Of r,p,s or q ') 

# Display What Player Choose:

if playerMove == 'r':
      print('Rock Versus... ')
elif playerMove == 'p':
      print('Paper Versus... ')      
elif playerMove == 's':
      print('Scissors Versus... ') 

# Display What The Computer Choose:

randomNumber = random.randint(1,3)
if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')

elif randomNumber == 2:
    computerMove = 's'
    print('PAPER')

elif randomNumber == 3:
    computerMove= 's'
    print('SCISSORS')

if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1