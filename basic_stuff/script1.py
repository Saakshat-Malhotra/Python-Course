import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

n = int(input(f"Enter a number between {start} and {end}: "))

if n > end or n < start:
    print(f"Enter the number between {start} and {end} only")
else:
    x = random.randint(start, end)
    print("Random generated number is", x)
    if x == n:
        print("You're a Genius")
    else:
        print("Try again")