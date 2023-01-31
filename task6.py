"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
"""
ticket = int(input('enter the ticket number\n'))
numLeft = ticket // 1000
numRight = ticket % 1000

sumleft = 0
while numLeft > 0:
    result = numLeft % 10
    sumleft += result
    numLeft = numLeft // 10

sumRight = 0
while numRight > 0:
    result = numRight % 10
    sumRight += result
    numRight = numRight // 10

if sumleft == sumRight:
    print('YOU HAVE A LUCKY TICKET')
else:
    print('loser')
