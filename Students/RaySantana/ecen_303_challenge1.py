from random import random
from numpy import zeros
from matplotlib import pyplot
import matplotlib.ticker as ticker

# Method simulating the flip a fair coin. Returns 1
# for heads and 0 for tails
def coinflip(p=0.5):
    coin = random()
    if (coin <= p):
        return 1
    else:
        return 0

# Estimate the empirical probability of heads by
# flipping a fair coin 1000 times
num_heads = 0
for num in range(0,1000):
    a = coinflip()
    if (a==1):
        num_heads += 1
print("Empirical probability of heads: ",(num_heads/1000))

# Method for simulating a geometric distribution
def geo_coin(p=0.5):
    firstHead = False
    trials = 0
    while(not firstHead):
        a = coinflip(p)
        if (a==1):
            firstHead = True
        else:
            trials += 1
    return trials

# Generate a histogram of the number of trials
# until the first head appears
trial_array = zeros(10000,dtype=int)
for i in range(0,10000):
    a = geo_coin()
    trial_array[i] = a
 
tick_spacing = 1
fig, ax = pyplot.subplots(1,1)
pyplot.hist(trial_array, bins=50)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
pyplot.axis('tight')
pyplot.title("Histogram for # of trials before heads")
pyplot.xlabel("# of trials before heads")
pyplot.ylabel("Frequency")
pyplot.show()

