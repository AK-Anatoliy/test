# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 10:
    print(a, b)
    a, b = b, a + b

# WHY? Will be not the same if write in two line
print('WHY?')

a, b = 0, 1
while a < 10:
    print(a, b)
    a = b
    b = a + b
