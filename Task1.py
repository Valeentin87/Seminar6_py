# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
system_coord = {
    '1': 'x>0 , y>0',
    '2': "x<0 , y>0",
    '3': 'x<0 , y<0',
    '4': 'x>0 , y>0'
}
print((lambda num, col: col[num]) (input('введите номер четверти '), system_coord))