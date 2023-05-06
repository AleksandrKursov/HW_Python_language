# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

# Если не усложнять задачу и не уточнять, какой из элементов списка с минимальной разницой нужно взять,
# то решение должно быть верным - выбирается элемент с мин разницой, который встретился первым.

from random import randint
list_A = [randint(1, 20) for i in range(int(input("Enter the number of items in the list: ")))]
print(list_A)
min_diff = max(list_A)
X = int(input("Enter the given number: "))
for i in range(len(list_A)):
    # if list_A[i] - X < min_diff and list_A[i] - X >= 0 or X - list_A[i] < min_diff and X - list_A[i] >= 0:
    if abs(list_A[i]-X) < min_diff:
        min_diff = abs(list_A[i] - X)
        min_index = i
nearest_number = list_A[min_index]
print(f"The nearest element to the given number {X} -> {nearest_number}")