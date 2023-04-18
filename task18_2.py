# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

# abs() преобразовывает в целое положительное число, abs(-20) -> 20

from random import randint
myList = [randint(1, 10)
          for i in range(int(input("Введите количество элементов: ")))]
X = int(input("Введите искомый элемент для сравнения: "))
print(myList)
min_difference = abs(X - myList[0])
new_i = 0
for i in range(len(myList)):
    difference = abs(X - myList[i])
    if difference < min_difference:
        min_difference = difference
        new_i = i
print(f"Ближе всего к числу {X} находится: {myList[new_i]}")
