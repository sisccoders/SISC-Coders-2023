import random

z = random.choice(["Head","Tails"])

user = input("Pick a Side, Head or Tails?: ")
while True:
    if user != 'Head' and user != 'Tails':
        print('Please type Head or Tails')
    else:
        break
if user:
    if z == user:
        print('You guessed correctly')
    else:
        print("You didn't guess correctly")