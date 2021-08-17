import random
game = True
winCount = 0
lossCount = 0
tieCount = 0
print('ROCK, PAPER, SCISSORS')
print(str(winCount) +' Wins ' + str(lossCount) + ' Losses ' + str(tieCount) + ' Ties')

while game:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    computerChoice = random.randint(1, 3)

#     if computerChoice == 1:
#         computerChoice = 'rock'
#     elif computerChoice == 2:
#         computerChoice = 'paper'
#     else:
#         computerChoice = 'scissors'

    playerChoice = input()
    if playerChoice == 'r':
        playerChoice = 1
    elif playerChoice == 'p':
        playerChoice = 2
    elif playerChoice == 's':
        playerChoice == 3
    else:
        print('Invalid input. Please enter (r)ock (p)aper (s)cissors or (q)uit')

    if computerChoice == 1:
        print('The computer chose rock.')
    elif computerChoice == 2:
        print('The computer chose paper.')
    elif computerChoice == 3:
        print('The computer chose scissors.')

    if playerChoice in range(1,3):
        if playerChoice > computerChoice:
            print('Player win!')
        elif playerChoice < computerChoice:
            print('Computer win!')
        elif playerChoice == computerChoice:
            print('Its a tie!')
        else:
            print('Something went wrong, please try again')


#     print(computerChoice)
#     print(playerChoice)