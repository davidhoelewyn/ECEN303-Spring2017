#ECEN303 - Challenge 1
#Jisoo Kim 421005860
import random
import matplotlib.pyplot as plt
import numpy

# Part 1
Trials = []
def coinflip(p=0.5):
    if random.random() < p:
        return 1 #Head
    else :
        return 0 #Tail
count = 0
#1000 coin flips
for TrialIndex1 in range(0, 1000):
    Trials.append(coinflip(0.5))
#calculate probability
empirical_prob = 1.0 * sum(Trials) / len(Trials)
print 'Empirical Probability of Heads :',empirical_prob

# Part 2
# repeat coin flip until head
def coinflip_geo(p=0.5):
    Trials2 = []
    while (coinflip(p)):
        Trials2.append(0)
    Trials2.append(1)
    return len(Trials2)

n = coinflip_geo()
print '# of trials until first head is', n


# coin flip 10000 times
Trials3 = []
for TrialIndex2 in range(0,10000):
    Trials3.append(coinflip_geo())

#plot histogram
plt.title("Number of trials until first head")
plt.hist(Trials3, bins=range(min(Trials3), max(Trials3)))
plt.xlabel("# of Trials")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
