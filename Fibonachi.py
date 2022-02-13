# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 10:
    print(a, b)
    a, b = b, a + b

print(type(a), type(b))

# WHY? Will be not the same if write in two line
print('WHY?')

a, b = 0, 1
while a < 10:
    print(a, b)
    a = b
    b = a + b

'''
https://ru.stackoverflow.com/questions/
438740/%D1%87%D1%82%D0%BE-%D0%BE%D0%B7%D0%BD%
D0%B0%D1%87%D0%B0%D0%B5%D1%82-a-b-b-a-b
КОРТЕЖ
'''

print('And how it really working')

a, b = 0, 1
while a < 10:
    print(a, b)
    prev = a  # сохраняем предыдущее значение во временной переменной
    a = b  # сохраняем текущее значение
    b = prev + a  # вычисляем следующее значение как
