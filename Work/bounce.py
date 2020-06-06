# bounce.py
#
# Exercise 1.5

height = 100
bounce_factor = 3/5

for x in range(10):
    height = height * bounce_factor
    print(x + 1, '  ', round(height, 4))
