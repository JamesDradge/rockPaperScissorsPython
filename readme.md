Trying to create my own rock paper scissors game in python without looking at any examples

Got pretty much all the logic down for the computer generation, player input, win count etc. The only thing I needed to look up was a method to determine a winner using maths, was able to use:

rock = 1
paper = 2
scissors = 3

(playerChoice - computerChoice) % 3

if % == 0 its a tie
if % == 1 player wins
if % == 2 computer wins

I'm still not fully sure how the formula works/how I would have ever figured it out on my own, but seems more efficient than lots of different if statements comparing strings