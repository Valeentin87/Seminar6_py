# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_expression = 'Вотабв изабв абвэтих слабвов надо удалить слова имеющие АБВ'


def del_abv(some_text):
    some_text = list(filter(lambda x: 'абв' not in x, some_text.split()))
    return " ".join(some_text)


result = del_abv(my_expression)
print(result)