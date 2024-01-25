from random import random

#random chooses a float between 0 and 1
# 50% = 0.5

p = random()
if p < 0.5:
    print('Tails')
else:
    print('Heads')