import random
import numpy as np


def lab1():
    s = input("Введите любую строку: ")
    if len(s) > 5:
        print(s[0], s[1], s[3], " ", s[len(s) - 3], s[len(s) - 2], s[len(s) - 1])
    else:
        for i in range(len(s)):
            print(s[0], " ")


def lab2():
    s = input("Введите любую строку: ")
    for i in range(len(s)):
        if i % 2 != 0:
            if s[i] != " ":
                if s[i] != "a":
                    s = s[:i] + "a" + s[i + 1:]
                else:
                    s = s[:i] + "b" + s[i + 1]
    print(s)


def lab3():
    print(' '.join(input("Введите любую строку: ").split()))


def lab4():
    list = {"Computer", "Net", "Qwer", "Ib"}
    print(sorted(list, key=len))


def lab5():
    servers = ("gmail.com", "mail.ru", "yandex.ru", "icloud.com")
    symbols = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    email = ''
    for i in range(10):
        email += random.choice(symbols)
    print(f'{email}@{random.choice(servers)}')


def lab6():
    list = ["manager", "ceo", "cleanner", "teamlead", "programmer"]
    while True:
        print(list)
        deleteChoose = input("Что вы хотите удалить")
        if deleteChoose == 'exit':
            break
        try:
            list.remove(deleteChoose)
        except ValueError:
            print("Такого элемента не существует")
    print(list)


def lab7():
    accepted = ("txt", "py", "doc", "docx")
    file = input("Введите навзание файла").split('.')
    if len(file) >= 2:
        fileExtension = file[-1].lower()
        if fileExtension in accepted:
            print("Файл разрешён")
        else:
            print("Файл запрещён")
    else:
        print("Имя файла не имеет расширения")


def lab8():
    books = ["Empire V", "100 лет одиночества", "Война и Мир"]
    while True:
        print(books)
        usersBook = input("Введите название книги, которую вы хотите добавить")
        if usersBook == 'exit':
            break
        else:
            books.append(usersBook)
    print(books)


def lab9():
    N = 5
    M = 5

    a = np.random.randint(0, 10, size=(N, M))
    K = int(input("Введите любое число"))
    print(a)

    for i in range(N):
            for j in range(M):
                if a[i][j] == K:
                    for g in range(M):
                        print(a[i][g]," ", end="")
                    print()
                    break




def lab10():
    d = {"ivan_egorov": "passy", "yuzer": "qwert", "boris": "1234", "waflee": "4321helloworld", "qwerty21": "0987"}
    login = input("Введите логин")
    password = d.get(login)
    b = any(map(str.isdigit, password))
    a = len(password) > 6
    if b & a:
        print(password, ": Пароль безопасен")
    else:
        print(password, ": Пароль не безопасен")


def lab11():
    groups = {"821": (
    "Egorov", "Bageev", "Abramson", "Adamson", "Adderiy", "Addington", "Adrian", "Bosworth", "Campbell", "Clifford",
    "Emerson", "Francis", "Gate", "Higgins"), "822": (
    "Egorov", "Bageev", "Abramson", "Adamson", "Adderiy", "Addington", "Adrian", "Bosworth", "Campbell", "Clifford"),
              "833": ("Egorov", "Bageev", "Abramson", "Adamson", "Adderiy"),
              "844": ("Egorov", "Bageev", "Abramson", "Adamson")}
    d1 = len(groups.get("821"))
    d2 = len(groups.get("822"))
    d3 = len(groups.get("833"))
    d4 = len(groups.get("844"))
    max = d1
    min = d1
    if d2 > max:
        max = d2
        if d3 > max:
            max = d3;
            if d4 > max:
                max = d4
    if d2 < min:
        min = d2
        if d3 < min:
            min = d3;
            if d4 < min:
                min = d4

    if max == d1:
        print(groups.get("821"))
    if max == d2:
        print(groups.get("822"))
    if max == d3:
        print(groups.get("833"))
    if max == d4:
        print(groups.get("844"))
    print()
    if min == d1:
        print(groups.get("821"))
    if min == d2:
        print(groups.get("822"))
    if min == d3:
        print(groups.get("833"))
    if min == d4:
        print(groups.get("844"))


print("Выбери нужную лабу")
print("1. - Вывод первых 3-х символов и 3-х последних")
print("2. - Замена чётных символов")
print("3. - Убирание лишних пробелов")
print("4. - Сортировка по длине строк")
print("5. - Генерация email")
print("6. - Удаление элемента из массива")
print("7. - Проверка файла")
print("8. - Добавление книг")
print("9. - Двумерный массив")
print("10. - Проверка пароля на безопасность")
print("11. - Вывод самых больштх и маленьких групп")

usersChoose = input()
if usersChoose == "1": lab1()
if usersChoose == "2": lab2()
if usersChoose == "3": lab3()
if usersChoose == "4": lab4()
if usersChoose == "5": lab5()
if usersChoose == "6": lab6()
if usersChoose == "7": lab7()
if usersChoose == "8": lab8()
if usersChoose == "9": lab9()
if usersChoose == "10": lab10()
if usersChoose == "11": lab11()
