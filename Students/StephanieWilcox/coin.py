#!/usr/bin/python

import random
from proj import flipResults
from proj import geometric

p = 0.34
trials = 1000
probability = [1-p, p]
[x,numHeads,emProb] = flipResults(trials, p)
y, totflips = geometric(trials, p)

print(numHeads)
print("Probability of 'Heads' = %.2f" % (p))
print("Total number of trials until 'Heads' = %d"%(x))
print("Empiral Probability = %.2f" % (emProb))
