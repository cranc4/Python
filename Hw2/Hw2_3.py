# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

n = int(input("Введите число: "))
k = 1
while k <= n:
    print(k)
    k = k * 2