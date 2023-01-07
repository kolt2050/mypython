# Напишите функцию sum_range(start, end), которая суммирует все целые числа
# от значения start до величины end включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
print("сумирование чисел в диапазоне")
def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for n in range(start, end+1):
        s = s + n
    return s

print(sum_range(2, 12))
print(sum_range(-4, 4))
print(sum_range(3, 2))

# Более короткий способ
print("Более короткий способ сумирования чисел в диапазоне")
def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

# Тесты
print(sum_range(2, 12))
print(sum_range(-4, 4))
print(sum_range(3, 2))

# Примеры видимости переменных
print("Примеры видимости переменных")
def func1():
    param = 4
    def inner():
        param += 1
    return param

def func2():
    param = 4
    def inner(var):
        var += 1
    inner(param)
    return param

def func3():
    param = 4
    def inner(var):
        var += 1
        return var
    param = inner(param)
    return param

print(func1())
print(func2())
print(func3())

# Функция с множественными параметроми
print("Функция с множественными параметроми")
def fruits(*args):
    for arg in args:
        print(arg)
fruits('Mango', 'Apple', 'Guava', 'Banana')

# print("Функция с множественными параметроми")
# def numbers(arg1, *args):
#     print(“First number: “, arg1)
#     for arg in args:
#         print(“Next
#         number: “, arg)
#
#         numbers(‘one’, ‘two’, ‘three’, ‘four’, ‘five’)

print("Факториал")
def factorial(n):
    proizvedenie = 1
    for i in range(2, n+1):
        proizvedenie=proizvedenie*i
    print(proizvedenie)

factorial(3)

print("Факториал рекурсией")
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

print(fac(5))

print("Факториал math")
import math
print(math.factorial(4))

