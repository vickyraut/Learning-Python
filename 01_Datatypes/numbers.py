from decimal import Decimal
x = 23
y = 3
z = 4

print(x + y)

print(40 + 2.23)  # Don't use diffetrent datatypes

# use this
print(40 + int(2.23))

print(y % 2)

print(z ** 5)

print(x < y < z)

import math

print(math.floor(3.5))
print(math.floor(-3.5))

print(math.trunc(2.8))
print(math.trunc(-2.8))

import random

print(random.random())
print(random.randint(1, 10))

print((0.1 + 0.1 + 0.1 - 0.3))  # Not right way to handle precision


print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
