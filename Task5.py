# Реализуйте алгоритм перемешивания списка.
import random
N = int(input('введите число элементов в последовательности '))
lst = [random.randint(0,20) for i in range(N)]
print(lst)
res_lst = [ lst[i-(2*i+1)] for i in range(N)]
print(res_lst)
