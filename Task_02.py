# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print()
number = int(input('Enter a three-digit number: '))
if number > 99 and number < 1000:
    sum = 0
    while number != 0:
        temp = number % 10
        sum += temp
        number = number // 10
    print(f'The sum of the digits of a three-digit number: {sum}')
    print()
else:
    print('You entered a non-three-digit number')
    print()
