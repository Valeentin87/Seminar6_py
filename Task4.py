# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. \
# Найдите произведение элементов на указанных позициях. \
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
N = int(input('введите число элементов в последовательности '))
lst = [random.randint(-N, N) for i in range(N)]
print(lst)
if N%2==0:
    result_numbers = N/2
else:
    result_numbers = N//2 +1
res_lst = [lst[i]*lst[i-(i*2+1)] for i in range(result_numbers)]
print(res_lst)


