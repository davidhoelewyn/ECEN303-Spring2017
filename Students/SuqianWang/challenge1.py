import random
import matplotlib.pyplot as plt
import numpy

def coinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    if (random.random() < p):
        return 1 # 1 denote Head
    else:
        return 0 # 0 denote Tail
       
    # Estimate empirical probability
    # You may want to use a `for` loop
sumH = 0
for i in range(0, 1000):
    if (coinflip(0.5) == 1):
        sumH = sumH + 1

empiricalp = sumH / 1000
print ('The empirical probability of Heads: ', empiricalp)
    
    # Geometric Random Variable:
    # You may want to use a 'while' loop to flip a coin      
    # until head occurs 
def geometric(p=0.5):
    numtrails = 0
    while (coinflip(p) == 0):
        numtrails = numtrails + 1
    numtrails = numtrails + 1 # numtrails include the last trail that is a Head
    return numtrails  

print ('The number of tials until first Head: ', geometric(0.5)) 
    # For repeating the above process for 10000 times,
    # you may want to use an outer 'for' loop for    
    
    # Compute the histogram (possibly using for loops)
    # Plot the histogram
my_list = []
for i in range(0, 10000):
    my_list.append(geometric(0.5))

# print(my_list)
plt.hist(my_list, bins='auto')
plt.title("number of trails until first head")
plt.show()