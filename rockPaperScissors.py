import random, sys
winCount = 0
lossCount = 0
tieCount = 0


while True:
    print()
    print('ROCK, PAPER, SCISSORS')
    print(str(winCount) +' Wins ' + str(lossCount) + ' Losses ' + str(tieCount) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    computerChoice = random.randint(1, 3)

    playerChoice = input()
    if playerChoice == 'r':
        playerChoice = 1
        print('You chose rock.')
    elif playerChoice == 'p':
        playerChoice = 2
        print('You chose paper.')
    elif playerChoice == 's':
        playerChoice = 3
        print('You chose scissors.')
    elif playerChoice == 'q':
        sys.exit
        break
    else:
        print('Invalid input. Please enter (r)ock (p)aper (s)cissors or (q)uit')

    if computerChoice == 1:
        print('The computer chose rock.')
    elif computerChoice == 2:
        print('The computer chose paper.')
    elif computerChoice == 3:
        print('The computer chose scissors.')

    if playerChoice in range(1,4):
        if (playerChoice - computerChoice) % 3 == 1:
            #print(str(playerChoice) + ' - ' + str(computerChoice) + ' % 3 = 1')
            print('Player win!')
            winCount = winCount + 1
        elif (playerChoice - computerChoice) % 3 == 2:
            #print(str(playerChoice) + ' - ' + str(computerChoice) + ' % 3 = 2')
            print('Computer win!')
            lossCount = lossCount + 1
        elif (playerChoice - computerChoice) % 3 == 0:
            #print(str(playerChoice) + ' - ' + str(computerChoice) + ' % 3 = 0')
            print('Its a tie!')
            tieCount = tieCount + 1
        else:
            print('Something went wrong, please try again')


