# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = int(input("Введите размер списка: "))
# array = list(range(1, n+1))
# print(array)
# x = int(input("Введите число Х: "))
# if x > n:
#     answer = n
# else:
#     answer = x - 1
# print(answer)

# -------------------- 2 вариант

from random import randint

list_nums = [randint(1, 21) for _ in range(int(input()))]

print(list_nums)
num = int(input())
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num - right_num):
        right_num = i

print(right_num)
