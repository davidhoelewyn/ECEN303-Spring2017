#Program written by David Hoelewyn
#Using predefined libraries random, matplotlib, and numpy

import random
import matplotlib.pyplot as mat
import numpy as np

#this function simulates the flipping of a coin with any specified p
def coinflip(p=0.5):
    HT = random.uniform(0,1)
    if (HT < p):
        heads = 1
    else:
        heads = 0
    return heads

#the code following simulates flipping the coin 1000 times, and calculating the
#probability of heads
sum = 0
b = 0
probability = 0.0
print("Coin Flip (1 is heads, 0 is tails): ", coinflip(), "\n")
for num in range(1, 1000):
    b = coinflip()
    sum = sum + b

probability = sum/1000
print("Empirical Probability of heads: ", probability, "\n")

#simulation of a geometric random variable
trialsTilHeads = 1
while (coinflip() != 1):
    trialsTilHeads = trialsTilHeads + 1

print("Trials until first heads: ", trialsTilHeads)

#Runs the geometric random variable experiment 10000 times and saves results
#in a 10000 by 1 vector
DataArray = np.zeros((10000, 1))
for num in range(0, 9999):
    trialsTilHeads = 1
    while (coinflip() != 1):
        trialsTilHeads = trialsTilHeads + 1
    DataArray[num, 0] = trialsTilHeads

#Creates the histogram
n, bins, patches = mat.hist(DataArray, 10, normed=1, facecolor='green', alpha=0.75)
mat.title("Histogram of Geometric Random Variable")
mat.xlabel("Times until heads")
mat.ylabel("Probability")
fig = mat.gcf()
mat.show()
