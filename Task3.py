# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
float_number = (input('введите вещественное число '))
ls = [int(float_number[i]) for i in range(len(float_number)) if float_number[i] != '.']
print(sum(ls))