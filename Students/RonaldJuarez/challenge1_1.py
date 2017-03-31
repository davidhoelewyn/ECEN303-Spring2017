import random;

def biasedcoinflip(p = 0.5):
	
	# Create method for biased coin flip
    # Return 1 for heads, with probability p
    # and 0 for tails
	
	result = 0;
	flip = random.uniform(0,1);
	
	if flip <= p:
		result = 1;
	else:
		result = 0;
	
	print result;
	
biasedcoinflip();