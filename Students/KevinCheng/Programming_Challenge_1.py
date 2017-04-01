import random
import matplotlib.pyplot as plt
import numpy as np

#Part 1 : method to flip coin with probability p
def coinflip (p):
	outcome = random.randint(0,1);
	if outcome <= p:
		return 0;
	else:
		return 1;

trial = coinflip(0.5);

print ("Flipping a fair coin where H = 1 and T = 0 results in :: "+str(trial));

#tossing fair coin 1000 times
head_count = 0;
tail_count = 0;
for i in range(1000):

    toss_1000 = coinflip(0.5)

    if toss_1000 == 1:
     head_count += 1

    else:
     tail_count += 1
print("\nOutcome of flipping fair coin 1000 times");
print("Number of heads %d" % head_count);
print("Number of tails %d" % tail_count);

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Part 2 : Geometric Distribution
iteration = 0;
geo_toss = 0;
while geo_toss == 0:
    geo_toss = coinflip(0.5)
    iteration += 1

print("\nAmount of iterations until first heads %d" %iteration)

#flipping fair coin 10,000 times for geometric distribution case
x = 0;  #this is to check for the amount of times it will loop

flip_list = [0]
#this is not working
for j in range(10000):

    geo_toss = 0;
    iteration = 0;
    x += 1;
    while geo_toss == 0:
        geo_toss = coinflip(0.5)
        iteration += 1
        flip_list.insert(j, iteration)


print("\nAmount of iterations until first heads repeating 10,000 times:")
#print("\nAmount of loops: %d" %x)   #This is for debugging to see how many times the forloop will run

print(flip_list)

plt.hist(flip_list, bins=[0,1,2,3,4,5,6,7,8,9])
plt.show()
