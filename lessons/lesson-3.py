
# -*- coding: utf-8 -*-

########################################################

# Задача 1: Квадратное уравнение

import math  # Для вычисления корня из положительного числа

def count_quad_equation(a, b, c): # Функция для вычисления корня из отрицательного числа уравнения y^2 +12y + 20 = 0

    discriminant = b**2 - 4*a*c
    print("Дискриминант: {}".format(discriminant))


    if discriminant < 0:
        return "Нет корней"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        return (-b + math.sqrt(discriminant)) / (2*a), (-b - math.sqrt(discriminant)) / (2*a)
    
# результат функции
print("-----------------------------------------------")
print("Ответ: {}".format(count_quad_equation(1, -4, 20)))
print("-----------------------------------------------")
print("Ответ: {}".format(count_quad_equation(1, 17, 72)))
print("-----------------------------------------------")
print("Ответ: {}".format(count_quad_equation(1, 7, 44)))
print("-----------------------------------------------")
print("Ответ: {}".format(count_quad_equation(1, 9, 8)))
print("-----------------------------------------------")
print("Ответ: {}".format(count_quad_equation(1, 2, 63)))
print("-----------------------------------------------")
print("Ответ: {}".format(count_quad_equation(1, 4, -5)))
print("-----------------------------------------------")

########################################################

# Задача 2: Обраный порядок списка

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# результат
print(f"Исходный порядок списка: {my_list}")

my_list.reverse()

# результат
print(f"Обратный порядок списка: {my_list}")
print("-----------------------------------------------")

########################################################

# Задача 3: Функция для обмена первого и последнего элемента списка

def reverse_list_new(my_list):

    new_list = my_list.copy()
    if len(new_list) >= 2:
        new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

# результат функции
my_list_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_changed = reverse_list_new(my_list_original)

print("Исходный список:", my_list_original)
print("Изменённый список:", my_list_changed)
print("-----------------------------------------------")

########################################################

# Задача 4: Функция для поиска бесполезного числа в списке

def unuseful_number_list(listing):
    
    max_value = max(listing)  # Здесь находим максимальное значение 

    for number in listing:
        if number > 0 and max_value == number:
            return number / 2

    return "Нет бесполезного числа"

# результат функции
listing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unuseful_number_result = unuseful_number_list(listing)

print("Бесполезное число:", unuseful_number_result)
print("-----------------------------------------------")

########################################################

# Задача 5: Не решена

########################################################

# Доп. задача 1: Функция для поиска подстроки в строке

def search_substr(subst, string):
    if subst in string:
        return "Есть контакт!"
    else:
        return "Мимо!"

# результат функции
print(search_substr("hello", "hello world"))
print("-----------------------------------------------")

########################################################

# Доп. задача 2: Функция для поиска 3 наиболее часто встречаемых символов в строке

from collections import Counter

def find_top_3_chars(text):

    text_without_spaces = text.replace(" ", "")
    
    counter_text = Counter(text_without_spaces)
    
    most_common = counter_text.most_common(3)
    
    return most_common

# результат функции
text = "hello world!"
result = find_top_3_chars(text)

print("Строка:", text)
print("3 наиболее часто встречаемых символа:", result)
print("-----------------------------------------------")

########################################################

# Доп. задача 3: не решена