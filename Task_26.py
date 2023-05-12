# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# Вариант с отрицательными степенями:

def Exponentiation(a, b):
    if b > 0:
        if b == 0: return 1
        return a*Exponentiation(a, b - 1)
    else:
        if b == 0: return 1
        return 1/a*Exponentiation(a, b + 1)          
print("Answer is:", Exponentiation(int(input('Enter number A: ')), int(input('Enter exponentiation number B: '))))