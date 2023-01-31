"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
sum = int(input('Enter the total number of cranes\n'))
if sum%4 == 0:
    sergey = sum / 4
    kat = sum / 2
    print('Petya and Seryozha made ', int(sergey), " crane, Katya made ", int(kat), 'crane ')
else:
    print('Invalid number entered')


