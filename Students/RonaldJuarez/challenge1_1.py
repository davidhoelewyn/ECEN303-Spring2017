import random

HEAD = 1
TAIL = 0 

############################# PART 1 ################################

prob = 0.7;
iterations = 1000;

def biasedcoinflip(p = 0.5):
	
	# Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails
	# Author: Ronald Juarez. ECEN303. Spring2017
	
	result = 0;
	flip = random.uniform(0,1);
	
	if flip <= p:
		result = 1;
	else:
		result = 0;
	
	return result;

# Flip a fair coin 1000 times, and 
# estimate the empirical probability of Heads.

heads= 0;

for i in range(iterations):
	result = biasedcoinflip(prob)
	if result==HEAD:
		heads+=1
		

print "Pr(heads): " + str(heads/float(iterations))
print "Pr(tails): " + str((iterations-heads)/float(iterations))



############################# PART 2 ################################