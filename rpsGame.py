import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s wins, %s losses, %s ties'%(wins, losses, ties))
    while True: # The player input loop
        print("Enter your move: (r)ock, (p)aper or (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Type on of r, p, s or q")
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove ='r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSCORS')

    if playerMove == computerMove:
        print("This is a tie")
        ties = ties + 1  
    elif (playerMove =='r' and computerMove =='s') or (playerMove == 'p' and computerMove =='r') or(playerMove == 's' and computerMove =='p'):
        print('You win!')
        wins = wins + 1
    elif (playerMove == 's' and computerMove == 'r') or (playerMove == 'r' and computerMove == 'p') or (playerMove == 'p' and computerMove == 's'):
        print('Damn! You lose!')
        losses = losses + 1