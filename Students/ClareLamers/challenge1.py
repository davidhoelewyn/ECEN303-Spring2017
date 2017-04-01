import random
import numpy as np
import matplotlib.pyplot as mpl

#denote heads and tails
HEADS=1
TAILS=0

#initialize random number generator
random.seed()

#method for biased coin flip
def coinflip(p=0.5):
    #create random number from 0 to 1
    prob=random.random()
    #assign values
    if prob<=p:
        return TAILS
    return HEADS

#h=number of heads
#t=number of tails
h=0
t=0
#flip a coin 1000 times
for x in range(1000):
    #record number of heads
    if coinflip()==HEADS:
        h+=1
    #record number of tails
    else:
        t+=1
#Calculate empirical probability
print("Probability for heads:", h/1000)
print("Probability for tails:", t/1000)

#record flip outcomes
listheads=[]

#flip a coin 10000 times
for x in range(10000):
    x=1
    #flip coin until you get heads
    while coinflip()!=HEADS:
        #calculate number of flips it takes
        x=x+1
    listheads.append(x)

#create histogram
mpl.hist(listheads, normed=True, bins='auto')
mpl.ylabel('Frequency in Thousands')
mpl.xlabel('Number of Flips')
mpl.title('Number of Flips to Get Heads')
mpl.show()
