```python
import random

def guess_the_number(p):
    n = random.randrange(1, 101)
    attempt = 1
    while p != n:
        if p > n:
            p = int(input("Your guess was too high! Choose another number between 1 and 100: "))
        else:
            p = int(input("Your guess was too low! Choose another number between 1 and 100: "))
        attempt += 1
    print("Well done! It took you", attempt, "attempts to guess the number correctly!")

p = int(input("Enter a number between 1 and 100: "))
guess_the_number(p)