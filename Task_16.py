# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

# P.S Наверное задача предпологала решение через метод .count(), но я не сообразил сразу, записал последним такое решение.

# Первый вариант, согласно условиям задачи "A[1..N]", список чисел по порядку от 1 до числа N,
# но в таком случае число X всегда будет встречаться один раз, поэтому смысл не ясен:

N = int(input("Enter a count element in list: "))
list_A = []
for i in range(1, N+1):
    list_A.append(i)
print(*list_A)
X = int(input("Enter the number you are looking for: "))
count = 0
for i in range(len(list_A)):
    if X == list_A[i]:
        count += 1
print(f"Number {X} met in the list -> {count} time")

# Второй вариант, первое решение с использованием list comprehension:

list_A = [i for i in range(1, int(input("Enter a count element in list: "))+1)]
print(*list_A)
X = int(input("Enter the number you are looking for: "))
list_A = [X for i in range(len(list_A)) if (X == list_A[i])]
print(f"Number {X} met in the list -> {len(list_A)} time")

# Третий вариант с вводом чисел в список, чтобы создать повторения, тогда и считать сколько раз
# встречается некоторое число X в массиве A[1..N] имеет смысл:

list_A = [int(input(f"Enter {i+1} element into the list: ")) for i in range(int(input("Enter a count elements in list: ")))]
print(*list_A)
X = int(input("Enter the number you are looking for: "))
list_A = [X for i in range(len(list_A)) if (X == list_A[i])]
print(f"Number {X} met in the list -> {len(list_A)} time")

# Решение через .count():

list_A = [int(input(f"Enter {i+1} element into the list: ")) for i in range(int(input("Enter a count elements in list: ")))]
print(*list_A)
print("Number of repetitions ->", list_A.count(int(input("Enter the number you are looking for: "))))