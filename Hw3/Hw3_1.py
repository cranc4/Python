# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X


# n = int(input("Введите размер списка: "))
# array = list(range(1, n+1))
# print(array)
# x = int(input("Введите число Х: "))
# print(array.count(x))

# -------------------- 2 вариант

list_nums = [int(input()) for _ in range(int(input()))]
print(list_nums.count(int(input())))