
# Programming Challenge 1

This [Python](https://www.python.org) challenge will use the `random` module to generate pseudo random numbers.
Remember to import this module whenever needed.

```python
import random
```

Part 1: Write a method to simulate the flipping of a fair coin. Let us denote Heads as `1` and Tails as `0`. 
The method should return `1` with probability `p = 0.5`, and it should return `0` with probability `1-p`.

```python
sdef coinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    #
```

Flip a fair coin 1000 times, and estimate the empirical probability of Heads.

```python
    # Estimate empirical probability
    # You may want to use a `for` loop
    #
```

Part 2: Simulation of a `Geometric distribution`: flip a fair coin until a Head occurs. 
Output the number of trials until first Heads.

```python
    # Geometric Random Variable:
    # You may want to use a ‘while’ loop to flip a coin      
    # until head occurs 
    #
```

Do this 10000 times, and plot the histogram of `number of trials until first head`. 

```python
    # For repeating the above process for 10000 times,
    # you may want to use an outer ‘for’ loop for    
    # 
```

A template for the entire challege is as follows.

```python

import random

def coinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    #
       
    #
    # Estimate empirical probability
    # You may want to use a `for` loop
    #
    
    # Geometric Random Variable:
    # You may want to use a ‘while’ loop to flip a coin      
    # until head occurs 
    #
    
    #
    # For repeating the above process for 10000 times,
    # you may want to use an outer ‘for’ loop for    
    # 
    
    # Compute the histogram (possibly using for loops)
    # Plot the histogram
```

You may use modules as `matplotlib`, `numpy` to plot the histogram.

## Submission

Create a folder with your Github id in the `students` folder. Create a new file with name `challenge1.py` in your personal folder.
After completing this programming challenge, commit your work to our repository using Git and GitHub.
