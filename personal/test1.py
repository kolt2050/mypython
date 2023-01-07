import re

from bs4 import BeautifulSoup

with open("scrap_tutorial/lesson1/blank/index.html", encoding='utf-8') as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

#получить только первое вхождение h1
# page_h1 = soup.find("h1")
# print(page_h1)

#получить все вхождения h1
# page_all_h1 = soup.find_all("h1")
# # print(page_all_h1)
# # и перебрать в цикле
# for item in page_all_h1:
#     print(item.text)

# # Получить имя пользователя. На выходе получаем объект soup и можем применить к нему методы
# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip()) # strip  обрезает пустрые строки до и после

# # Поиск вглубь
# user_name = soup.find("div", class_="user__name").find("span").text
# print(user_name)

# # Задание атрибутов для фильтрации поиска с помощью словаря
# user_name = soup.find("div", {"class": "user__name"}).find("span").text
# print(user_name)

# # find_all
# user_all_name = soup.find(class_="user__info").find_all("span")
# print(user_all_name)
#
# for item in user_all_name:
#     print(item.text)
#
# print(user_all_name[0].text)

# # Распарсим ссылки на соцсети пользователя
# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# # social_links = soup.find(class_="social__networks").find_all("a")  #  одно и тоже
# print(social_links)
#
# # Забрать все ссылки на странице и вытащить ссылки
# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     # item_url = item.get("href")
#     item_url = item["href"]  # можно вот так обратиться к элементу
#     print(f"{item_text}: {item_url}")

# Дум-дерево .find_parent() .find_parents()
# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents()
# print(post_divs)

# .next_element .previous_element  Допустим нужно получить название статьи
# next_el = soup.find(class_="post__title").next_element.next_element # если бы был бы один элемент, то он бы вернул перевод строки, тосесть пустоту
# print(next_el.text)
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# .find_next_sibling() .find_previous_sibling()  ищет блоки после и перед указанным
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)
# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)

# регулярное выражение используя re.compile()
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text.text)

# Собрать все блоки в которых содержится слово "Одежда"
# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_clothes)