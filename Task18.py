# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
a = []
N = int(input('Введите количество элементов в массиве: '))
for i in range(N):
    a.append(int(input('Введите элемент массива: ')))
print(a)
X = int(input('Введите желаемое число: '))
closest = a[0]
for i in range(N):
    if 0 < abs(X - a[i]) < abs(X - closest):
        closest = a[i]
print(closest)