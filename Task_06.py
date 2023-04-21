# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
print()
number = int(input('Enter a six-digit ticket number: '))
if number > 99999 and number < 1000000:
#-------Optimized solution:
    sum_1 = 0                               
    sum_2 = 0
    while number != 0:
        if number > 999:
            sum_2 += number % 10
        else:
            sum_1 += number % 10
        number //= 10
    if sum_1 == sum_2:
        print('Yes, it is a lucky ticket!!!')
        print()
    else:
        print('No... it is not a lucky ticket')
        print()
else:
    print('You entered a non-six-digit ticket number')
    print()
    
# ------First solution:
    # sum_1 = 0
    # sum_2 = 0
    # while number > 999:
    #     sum_2 += number % 10
    #     number //= 10
    # while number != 0:
    #     sum_1 += number % 10
    #     number //= 10
    # if sum_1 == sum_2:
    #     print('Yes!')
    # else:
    #     print('No...')