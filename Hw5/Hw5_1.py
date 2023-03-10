# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
        
    return a * degree(a, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", degree(a, b))

# -------------------- 2 вариант

def pow_num(a, b):
    if b == 0:
        return 1
    if b < 0:
        return pow_num(a, b + 1) * 1 / a
    return pow_num(a, b - 1) * a


print(pow_num(int(input()), int(input())))