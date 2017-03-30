#!/usr/bin/python
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

#first part coinflip for bias when p = 0.5
def coinflip (p): #this works for a bias coin also
	flip = random.random();
	if flip <= p:
		return 0;
	if flip  > p:
		return 1;

si = coinflip(0.5);
print ("Fair coin flip (1 for Heads and 0 for Tails): "+str(si)); # to show its 0 or 1

#---------------------------------------------------
#part two recursion of coinflip function
sumHeads = 0;
flips = 0;
for i in range(0,1000):
	flip1 = coinflip(0.5);
	flips += 1; 
	if flip1 == 1:
		sumHeads += 1;


Probabilty = sumHeads/float(1000);
print ("Number of Heads out of 1000 trials: "+str(sumHeads)); #prints number of heads
print ("Empirical Probabilty: "+str(Probabilty)); #prints emprirical probabilty of Heads

#----------------------------------------------------
#parth three gemoetric distribution using coinflip function
#defined a geometric function so i can use it fro the histogram
def geometric(p):
	heads1 = 0;
	iteration = 0;
	while (heads1 == 0):
		heads1 = coinflip(p);
		iteration += 1;
	return iteration

per = geometric(0.5);
print ("Number of Trials to reach Heads: "+str(per));#prints the number of trials until heads occurs

#-----------------------------------------------------
#part four: I created a list of the different values of trials using a for loop that uses the geometric distribution function I defined in the last problem


ListResults = []

for i in range(0,10000):
    x = geometric(0.5)
    ListResults.append(x)


his = np.histogram(ListResults, bins = range(15))
fig , ax = plt.subplots()
offset = 1 
plt.bar(his[1][1:],his[0])
ax.set_xticks(his[1][1:] + offset)
ax.set_xticklabels(range(1,15))


plt.title("Fair Coin Trials: Heads")
plt.xlabel("Trials")
plt.ylabel("Frequency")
fig.tight_layout()
plt.show()
