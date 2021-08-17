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
    if computerChoice == 1:
        computerChoice = 'rock'
    elif computerChoice == 2:
        computerChoice = 'paper'
    else:
        computerChoice = 'scissors'
    playerChoice = input()
    print(computerChoice)
    print(playerChoice)