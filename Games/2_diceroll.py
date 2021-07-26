# Simple dice rolling simulator if you happen to lose dice easily
import random
import time

time.sleep(0.5)
print('Rolling..')
time.sleep(1)
print('Rolling more..')
time.sleep(1)
dice = random.randint(1, 6)
print('The dice rolled a mighty', dice, '!')