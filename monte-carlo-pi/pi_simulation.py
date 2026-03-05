import random

inside = 0
total = 100000

for i in range(total):
    x = random.random()
    y = random.random()

    if x*x + y*y <= 1:
        inside += 1

pi = 4 * inside / total
print("Estimated π:", pi)