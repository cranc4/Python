# Найдите сумму цифр трехзначного числа.

num = int(input("Введите трехзначное число: "))
summ = 0
while num > 0:
    n = num % 10
    summ += n
    num = num // 10

print(f"Сумма равна {summ}")