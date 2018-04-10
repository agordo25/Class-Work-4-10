#streaks of heads

import random
simNum= 0 #track of simulations
countHeads=0 #tracks how many flips were heads

simNum<10
flip = random.randint(0,1)
if flip==1:
        countHeads= countHeads = countHeads+1
else:
            countHeads=0
print(flip)
print("Heads Streak -", countHeads)

print("Total flips: ", simNum)

#how many flips do you need to get 12 in a row
#how long does it take for the number of heads and tails flipped to be equal
#in a dice experiment find out the longest streak where each roll is 
