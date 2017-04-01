# Challenge 01. ECEN 303. Spring 2017. Texas A&M University
# Author: Ronald Juarez
# Date: 04/01/2017

import random
import numpy as np
import matplotlib.pyplot as plt

HEAD = 1
TAIL = 0 

###################################### PART 1 ################################

prob = 0.5;
iterationsPart1 = 1000;
iterationsPart2 = 10000;
numberBins = 20;

def biasedcoinflip(p = 0.5):
	
	# Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails
	# Author: Ronald Juarez. ECEN303. Spring2017
	
	result = 0;
	flip = random.uniform(0,1);
	
	if flip <= p:
		result = HEAD;
	else:
		result = TAIL;
	
	return result;

# Flip a fair coin 1000 times, and 
# estimate the empirical probability of Heads.

heads= 0;

for i in range(iterationsPart1):
	result = biasedcoinflip(prob)
	if result==HEAD:
		heads += 1
		
print "\n\nPART 1: Flipping a coin" 
print "=======================\n"
print "Flipping a coin %d times" % iterationsPart1 
print "Empirical probability of heads: " + str(heads/float(iterationsPart1))



###################################### PART 2 ################################


# Geometric Random Variable:
# You may want to use a "while" loop to flip a coin      
# until head occurs 
#
	
def flipCoinUntilHead(p = 0.5):	
	count = 0
	isHead = False
	while not isHead:
		count += 1
		result = biasedcoinflip(p)
		if result == HEAD:
			isHead = True
	return count


result = flipCoinUntilHead(prob)
print "\nPART 2: Geometric Distribution"
print "==============================\n"
print "~Geom(p=%.2f) = %d flips until head occurs\n" % (prob, result)


# For repeating the above process for 10000 times,
# you may want to use an outer "for" loop for    
# 

arrayHist = np.zeros(iterationsPart2);
for i in range(iterationsPart2): 
	result = flipCoinUntilHead(prob);
	arrayHist[i] = result;
	
print "Performing %d times to generate geometric distribution. Plotting Histograms..." % iterationsPart2
plt.hist(arrayHist, numberBins , facecolor='green')
plt.xlabel('Number of trials until Heads occurs')
plt.ylabel('Frequency')
plt.title(r'Geometric Random Variable (p = %.2f)| n = %d iterations' % (prob,iterationsPart2))
plt.grid(True)
plt.show()

