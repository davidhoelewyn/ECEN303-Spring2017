#! / usr / bin / python
import random
from random import choice
from decimal import Decimal
import matplotlib
import numpy as np
import pylab as plt

def flipResults(trials, prob):
    totalflips = 0
    numheads = 0
    for num in range(1, trials):
        x = random.random();
        if x > prob:
            flip = 0
            totalflips = totalflips + 1
        else:
            flip = 1
            numheads = numheads + 1
            # break
    emprob = numheads / float(trials)
    return totalflips, numheads, emprob

def geometric(trials, prob):
    totalflips = 1
    numHeads = 0
    heads = []
    fig = plt.figure()
    for num in range(1, trials):
        x = random.random()
        if x > prob:
            flip = 0
            heads.append(float((pow((1 - prob), (totalflips - 1))) * prob))
            totalflips = totalflips + 1
            print(totalflips)
        else:
            flip = 1
            break

    if (totalflips == 1):
           bins = 1
           heads.append(Decimal(prob))
    else:
          bins = np.arange(1,totalflips,1)

    b = plt.bar(bins, heads)
    plt.xlabel('Number of Trials')
    plt.ylabel('Probabilty')
    plt.title('Histogram')
    plt.show()

    return heads, totalflips
