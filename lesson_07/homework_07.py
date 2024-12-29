# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while multiplier <= 9:
        result = number * multiplier

        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summ_of_two_numbers(number_1, number_2):
        return number_1 + number_2

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(arr: list):
    return sum(arr) / len(arr)
print(average([1,2,3,4,5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def back_string(any_string: str):
    result_string = any_string[::-1]
    return result_string
print(back_string("asdf"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(any_list: list):
    longest = ""
    for i in any_list:
        if len(longest)<len(i):
            longest = i
    return longest
print(long_word(["asd", "asdf", "asdfg", "as", "longest-word11"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    finder = str1.find(str2)
    return finder

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 - задача з домашки 6.4 - сума парних елементів списку
num_list = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 100, 111, 120, 145, 170]
def sum_list(numbers_list: list):
    summ_even = 0
    for i in numbers_list:
        if i % 2 == 0:
            summ_even = summ_even + i
    print(summ_even)
    return summ_even
sum_list(num_list)

# task 8 - задача з домашки 6.3 - повернення нового списку тільки з рядками
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
def only_str_elements(any_list: list):
    list_string = []
    for i in lst1:
        if isinstance(i, str):
            list_string.append(i)
    return list_string
print(only_str_elements(lst1))

# task 9
# task 10 задачі з 5-ї домашки я і так реалізував через функції, не буду сюди дублювати, бо там багато вхідних даних
# ось посилання на домашку: https://github.com/Dchumakwork/Hillel-edu/tree/main/lesson_05
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
