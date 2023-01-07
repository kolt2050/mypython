marks = [4, 5, 3, 4, 5, 22, 1, 6]
july = [True, 24, "hello", 20, 33, 66, 12, [5, 6, 4]]
print(july)
print(type(july))
print(len(july))

print(sorted(marks))
print(sorted(marks, reverse=True))
print(marks[-1])
print(marks[1:4])
print(marks[1:-1])
print(marks[2:])
print(marks[:2])
print(marks[:])
print(marks[::2])
marks[2] = 100
print(marks)
marks[2:5] = 25, 25
print(marks)
del marks[2]
print(marks)
a = marks[::-1] #перевернуть список
print(a)

l = [3, 6, 7, 8]
l[3] = l
print(l)

# показать под каким номером стоит тот или иной элемент
a = [3, 6, 9, 12, 15, 18]
b = [1, 1 ,1]
n = ['index of %i is '%(i) + str(a.index(i)) for i in a]
print( ('\n').join(str(l) for l in n) )

print(a.index(6)) # вывести позицию элемента

a.append(46)  # Вот так делать нельзя a = a.append(46)  иначе пропадут все элементы списка
# Добавлять можно только по одному значению
print(a)
# del a[2] # Удалить элемент
a[2:3] = [] # Удалить второй элемент срезом
print(a)
a.append(33)	 #Добавляет элемент в конец списка
a.extend(b)	     #Расширяет список list, добавляя в конец все элементы списка L
print(a)
a.insert(4, 55)	#Вставляет на i-ый элемент значение x
print(a)
a.remove(15)	#Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
print(a)
res_a = a.pop(3)	#Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
print(res_a)
print(a.index(18, 2, 5))	#Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
a.count(1)	#Возвращает количество элементов со значением x
print(a.count(1))
a.sort(reverse=True)	#Сортирует список на основе функции
a.reverse()	#Разворачивает список
print(a)
# с = a.copy()	#Поверхностная копия списка
# print(c)

if 33 in a[2:5]:
    print("входит в диапазон")

#считать первое и последнее значение, удалить первое и последнее значение, вставить из переменных
print("----------------------> Поменять первый и последний элемент местами<-")
my_list = [11, 3, 6, 8, 2, 6, 55, 99]
first = my_list[0]
last = my_list[-1]
my_list.pop(0)
my_list.pop(-1)
my_list.reverse()
my_list.append(last)
my_list.reverse()
my_list.append(first)
print(my_list)

print("----------------------> Вариант2 Поменять первый и последний элемент местами<-")
lst = [11, 3, 6, 8, 2, 6, 55, 99]
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change([1, 2, 3, 4, 5]))

# почистить количество двухзначних чисел в списке
print("---------------------->почистить количество двухзначних чисел в списке<-")
number = [1, 11, 25, 80, 100]
for i in reversed(number):
    if len(str(i)) == 2:
        number.remove(i)
print(number)

print("---------------------->удалить все значения кроме двузначных<-")
number = [1, 11, 25, 80, 100]
number = [i for i in number if not i // 100 and i > 10]
print(number)

#замена 20 на 200
print("---------------------->замена 20 на 200 в первом вхождении<-")
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

#удалить пустые строки из списка строк.
print("---------------------->Вариант1 удалить пустые строки из списка строк<-")
list1 = [5, 10, "", 20, "", 50, 20]
for i in list1:
    if i == "":
        list1.remove(i)
print(list1)

print("---------------------->Вариант2 удалить пустые строки из списка строк<-")
list1 = [5, 10, "", 20, "", 50, 20]
resList = list(filter(None, list1))
print(resList)

print("---------------------->Ищем рыбок в аквариуме содержащие начальные буквы<-")
creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))

print("---------------------->Аналог предыдущего варианта<-")
creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
def names_vowels(x):
  return x[0].lower() in 'aeiou'
filtered_names = filter(names_vowels, creature_names)
print(list(filtered_names))

print("---------------------->Уберем пустые значения из списка<-") #https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-ru
aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
filtered_tanks = filter(None, aquarium_tanks)
print(list(filtered_tanks))

print("----------------------> в список квадратов этих чисел<-")
aList = [1, 2, 3, 4, 5, 6, 7]
aList = [x * x for x in aList]
print(aList)

print("----------------------> удалить все вхождения числа 20<-")
list1 = [5, 10, "", 20, "", "abc", 50, 20]
for i in list1:
    if i == 20:
        list1.remove(i)
print(list1)

print("----------------------> аналог предыдущего задания через функцию<-")
list1 = [5, 10, "", 20, "", "abc", 50, 20]
def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]
resList = removeValue(list1, 20)
print(resList)

print("----------------------> Функция создает список<-")
def func(*var_list):
    return list(var_list)
print(func(1, 3, 5, -10, "abc"))

print("----------------------> Произвольный список чисел, находит в цикле 88 из них и удаляет его<-")
list1 = [5, 10, 88, 20, 30, 50, 20]
for i in list1:
    if i == 88:
        list1.remove(i)
print(list1)

print("----------------------> Произвольный список чисел, находит максимальное число из них и удаляет его<-")
list1 = [5, 10, 88, 20, 30, 50, 20]
list1.sort()
del list1[-1]
print(list1)


print("----------------------> Произвольный список чисел, находит самое большое из них, а затем делит его на длину списка<-")
list1 = [5, 10, 88, 20, 30, 50, 20]
dlina = max(list1)/len(list1)
print(dlina)

print("----------------------> Тоже самое но с помощью функции<-")
def useless(lst):
    return max(lst)/len(lst)
print(useless([5, 10, 88, 20, 30, 50, 20]))