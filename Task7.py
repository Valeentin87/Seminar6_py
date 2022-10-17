# Напишите программу, которая найдёт произведение пар чисел списка. \
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
N = int(input('введите число элементов в списке N = '))
lst = [random.randint(0, 20) for i in range(N)]
if len(lst)%2 == 0:
    res_lst = [lst[i]*lst[i-(2*i+1)] for i in range(int(len(lst)/2))]
else:
    res_lst = [lst[i] * lst[i - (2 * i + 1)] for i in range(int(len(lst) / 2+1))]
print(f' произведение сответствующих элементов списка {lst} равно {res_lst}')