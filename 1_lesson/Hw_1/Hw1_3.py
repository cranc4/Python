# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# num = int(input("Введите шестизначное число: "))
# summ1 = 0
# summ2 = 0
# for i in range(6):
#     while num > 0:
#         if num > 1000:
#             n = num % 10
#             summ1 += n
#             num = num // 10
#         else:
#             n = num % 10
#             summ2 += n
#             num = num // 10
# if summ1 == summ2:
#     print("Билет счастливый")
# else:
#     print("Билет не счастливый")

#    2 решение

ticket_num = input()
sum_first = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
sum_last = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])

print(f"The ticket is lucky: {sum_first==sum_last}")