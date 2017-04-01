# Austin Pursley
# ECEN 303, Challenge 1
# March 23, 2017
import random
import numpy

# Part 1
def coinflip(p=0.5):
    """
    Method that simulates a coin flip with probability p.
    :param p: Probability for the coin flip, defaulted to 0.5.
    :return: 1 or 0, where 1 is heads and 0 is tails.
    """
    # x is a random number between 0 and 1.
    x = random.random()
    # If x is less than the probability it is 1, otherwise it is 0.
    if  x <= p:
        # 1 is heads
        h_or_t = 1
    else:
        #0 is tails
        h_or_t = 0
    return h_or_t

#1000 coin flips
head_count = 0.0
tails_count = 0.0
for i in range(0, 1000):
    x = coinflip()
    if x == 1:
        head_count += 1
    else:
        tails_count += 1
# The empirical probablity of heads, calculated from the number of heads
# divided by the total number of coin flips.
empir_prob_heads = head_count / (head_count + tails_count)
print('The empiracal probability of heads is %.3f \n' %empir_prob_heads)

# Part 2
def flip_until_heads(p=0.5):
    """
    Simulation for probability experiment where you see how many times you flip
    a coin before getting heads.
    :param p: probability for coin flip
    :return: Number of flips to get heads.
    """
    heads = False
    #Variable that keeps track of the number of flips
    flip_num = 0
    #While loop that stops when value a heads appears.
    while heads == 0:
        heads = coinflip(p)
        flip_num += 1
    return flip_num

# Test method
z = flip_until_heads()
print('Method Test: The number of times flipped until heads is %d \n' % z)
# Do 10,000 trails of flip_until_heads, returning values into list.
flip_num_list = [0]
for i in range(0, 10000):
    x = flip_until_heads()
    flip_num_list.append(x)
# Plot a histogram using list from the 10,000 trails.
import matplotlib.pyplot as plt
plt.hist(flip_num_list, 15)
plt.title("Number of Flips for 10,0000 'Flips Until Heads' Trail Simulations")
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.show()