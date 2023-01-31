"""
Задача 2: Найдите сумму цифр трехзначного числа.
"""
number = int(input('enter number\n'))
sum = 0
while number > 0:
    result = number % 10
    sum += result
    number = number // 10
print(sum)