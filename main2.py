# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# a - решка
# b - орел

# num = int(input("Введите количество монет: "))
# a = 0
# b = 0

# for i in range(0,num):
#     N=int(input("Введите результат 0 - решка, 1-орёл: "))
#     if N == 0:
#         a+=1
#     if N == 1:
#         b+=1
# if a < b: 
#     print("Наименьшее количество переворачиваний = ", a)
# else:
#     print ("Наименьшее количество переворачиваний = ", b)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# S = int(input('введите сумму чисел: '))
# P = int(input('введите произведение чисел: '))
# flag = False 
# for i in range(1,1000):
#     for j in range(1,1000):
#         if P % i == 0 and P % j == 0 and i + j == S:
#             print(i , j)



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

# N = int(input('Введите число N: '))
# number = 2
# print(number**0)
# print(number)
# while True:
#     number *= 2
#     print(number)
#     if N < number * 2:
#         break