# Написать программу, которая читает файл и выводит только те строки, которые соответствуют заданному пользователем критерию
kriteri = input('Введите критерий для фильтрации: ')
with open ('text1.txt', 'r') as file:
    for line in file:
        if kriteri in line:
            print(line, end=' ')
