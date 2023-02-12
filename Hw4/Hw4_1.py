# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

from random import randint

list_1 = [randint(1, 21) for _ in range(int(input()))]
list_2 = [randint(1, 21) for _ in range(int(input()))]
print(*list_1)
print(*list_2)

list_3 = list(set(list_1) & set(list_2))
print(*list_3)
list_3.sort()
if list_3 == []:
    print("Нет общих чисел")

# -------------------- 2 вариант

    n, m = input().split()
first = [int(i) for i in input().split()]
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second)))