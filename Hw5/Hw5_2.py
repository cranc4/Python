# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print("Сумма чисел равна:", sum(a, b))