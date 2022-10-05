# x = "программирование"
# y = x[-1]
# print(x.index(y) + 1)
#
# print(len(x))


# name_1 = "Антон"
# name_2 = "Вова"
# name_3 = "Богдан"
# bratva = [name_1, name_2, name_3]
# print(bratva)
# print(bratva[0])
# print(bratva[0][2:])


# path = "C:/Python3/python.exe"
# print("Имя файла:", path[11:])
# print("Расширение:", path[-3:])
# print("Имя каталога:", path[3:10])
# print("Полный путь к каталогу:", path[0:10])

# path = "C:/Python3/python.exe"
# temp = path.split("/")
# print(temp)
# print("Имя файла:", temp[-1])
# print("Расширение:", temp[-1][-3:])
# print("Имя каталога:", temp[1])
# print("Полный путь к каталогу:", temp[0] + "/" + temp[1])

# chapter_1 = input("Глава 1: ")
# page_1 = input("Страница: ")
# chapter_2 = input("Глава 2: ")
# page_2 = input("Страница: ")
# chapter_3 = input("Глава 3: ")
# page_3 = input("Страница: ")
# print(chapter_1.ljust(15), page_1.rjust(15))
# print(chapter_2.ljust(15), page_2.rjust(15))
# print(chapter_3.ljust(15), page_3.rjust(15))





x = "12'345'678"
# temp2 = temp[0] + temp[1] + temp[2]
# number = int(temp2)
# print(number)

temp = x.replace("'", "")
number = int(temp)
print(number)