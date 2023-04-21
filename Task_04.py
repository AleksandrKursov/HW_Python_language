# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
print()
numberOfCranes = int(input('Enter the number of cranes created: '))
if numberOfCranes % 6 == 0:
    # numberOfCranes = petiaCreated + serezhaCreated + (petiaCreated + serezhaCreated)*2 = petiaCreated*6
    petiaCreated = serezhaCreated = numberOfCranes // 6
    kateCreated = (petiaCreated + serezhaCreated)*2
    print(f'Petia created {petiaCreated} cranes, Kate created {kateCreated} cranes, Serezha created {serezhaCreated} cranes')
    print()
else:
    print('The entered number of cranes does not conform to the conditions of the task')
    print()
