from random import randint


def lab1():
    numberNull = "0;"
    for i in range(5):
        print(numberNull * (i + 1))


def lab2():
    print(' ' + '*' + ' ' + ' ' + ' ' + ' ' + ' ' + '*' + ' ')
    print(' ' + ' ' + '*' + ' ' + '*' + ' ' + '*' + ' ' + ' ')
    print(' ' + ' ' + ' ' + '*' + ' ' + '*' + ' ' + ' ' + ' ')


def lab3():
    x = 1.7
    answer = (x + 1)*(x + 1) + 3 * (x + 1)
    print("%10.2f" % answer)


def lab4():
    a = int(input("Введите а = "))
    a2 = a * a
    a4 = a2 * a2
    a6 = a2 * a2 * a2
    a15 = a6 * a6 * a2 * a
    print("a4 =", a4, "a6 =", a6, "a15 =", a15)


def lab5():
    depInBank = int(input("Введите сумму вклада в банке"))
    yearPercent = int(input("Введите годовой процент"))
    stonks = depInBank * (1 + yearPercent / 100) ** 5
    print("%10.2f" % stonks, '$')


def lab6():
    heightOfMain = 647
    lenghtOfMain = 170
    squareLow = 30
    fullHeight = heightOfMain // squareLow
    fullLenght = lenghtOfMain // squareLow
    aswr = fullHeight * fullLenght
    print(aswr)


def lab7():
    print("Введите 4 числа")
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    a4 = int(input())
    max = 0
    min = 0
    if a1 % 2 == 0:
        max = a1
        min = a1
    if a2 % 2 == 0:
        if a2 > max: max = a2
        if a2 < min: min = a2
    if a3 % 2 == 0:
        if a3 > max: max = a3
        if a3 < min: min = a3
    if a4 % 2 == 0:
        if a4 > max: max = a4
        if a4 < min: min = a4
    if max == 0 & min == 0:
        print("Not Found")
    else:
        print("Max is", max, "; Min is", min)


def lab8():
    print("Введите дату")
    mounth = int(input("Месяц: "))
    day = int(input("День: "))
    year = int(input("Год: "))
    if (mounth == 1) | (mounth == 3) | (mounth == 5) | (mounth == 7) | (mounth == 8) | (mounth == 10) | (mounth == 12):
        if (day <= 31) & (day > 0):
            print(mounth, day, year, "- yes")
        else:
            print(mounth, day, year, "- no")
    elif (mounth == 4) | (mounth == 6) | (mounth == 9) | (mounth == 11):
        if (day <= 30) & (day > 0):
            print(mounth, day, year, "- yes")
        else:
            print(mounth, day, year, "- no")
    elif mounth == 2:
        if(day <= 28) & (day > 0):
            print(mounth, day, year, "- yes")
        else:
            print(mounth, day, year, "- no")
    else: print(mounth, day, year, "- no")


def lab9():
    numberFive = input("Введите пятизначное число = ")
    for i in range(len(numberFive)):
        if i % 2 != 0:
           numberFive = numberFive[:i] + "0" + numberFive[i+1:]
    print(numberFive)


def lab10():
    x1 = int(input("Введите x угла первого прямоугольника "))
    y1 = int(input("Введите y угла первого прямоугольника "))
    fx1 = int(input("Введите нижнюю сторону первого треугольника "))
    fy1 = int(input("Введите левую сторону первого треугольника "))

    x2 = int(input("Введите x второго прямоугольника "))
    y2 = int(input("Введите y второго прямоуголника "))
    fx2 = int(input("Введите верхнюю сторону второго треугольника "))
    fy2 = int(input("Введите левую сторону второго треугольника "))

    hy1 = fy1 + y1
    hx1 = fx1 + x1
    hy2 = fy2 + y2
    hx2 = fx2 + x2

    if (x2 >= x1) & (y2 >= y1) & (hy1 >= hy2) & (hx1 >= hx2):
        print("а) Все точки первого прямоугольника принадлежать второму")
    else:
        print("а) Точки первого прямоугольника не принадлежать второму")

    if (x2 == x1) & (y2 == y1) & (hy1 == hy2) & (hx1 == hx2):
        print("б) Прямоугольники одинаковы")
    else:
        print("б) Прямоугольники не одинаковы")
    if (((hx2 >= x1) & (hx1 >= hx2)) | ((x2 >= x1) & (hx1 >= x2))) & (
            ((hy2 >= y1) & (hy1 >= hy2)) | ((y2 >= y1) & (hy1 >= y2))):
        print("в) Эти прямоугольники пересекаются")
    else:
        print("в) Эти прямоугольники не пересекаются")


def lab11():
    courseOfDollar = int(input("Введите курс доллара"))
    for dollars in range(1, 100):
        weight = 3.5
        roubles = dollars * courseOfDollar
        weight = weight * dollars
        dollarsStr = str(dollars)
        roublesStr = str(roubles)
        weightStr = str(weight)
        print(dollarsStr + "$; " + roublesStr + "Р; " + weightStr + "КГ")


def lab12():
    for i in range(100):
        mainStr = ''
        for j in range(100):
            if i == j:
                mainStr += '0'
            else:
                mainStr += '1'
        print(mainStr)


def lab13():
    countOfTwo = 0
    while True:
        usersInput = int(input("Введите число = "))
        if usersInput == 0:
            break
        if usersInput % 2 == 0:
            countOfTwo += 1
    print(countOfTwo)


def lab14():
    countOfGames = int(input("Введите количество игр, которые вы хотите сыграть: "))
    computersVariants = ["Камень", "Ножницы", "Бумага"]
    computersWins = 0
    stones = 0
    scissors = 0
    papers = 0
    usersWins = 0
    for i in range(countOfGames):
        usersStep = input("Камень? Ножницы? Бумага? - ")
        computersStep = computersVariants[randint(0, 2)]
        print("Компьютер выбрал " + computersStep)

        if computersStep == "Камень":
            if usersStep == "Камень":
                print("Ничья")
                stones += 2
            elif usersStep == "Ножницы":
                print("Компьютер победил")
                computersWins += 1
                stones += 1
                scissors += 1
            elif usersStep == "Бумага":
                print("Вы победили")
                usersWins += 1
                stones += 1
                papers += 1

        if computersStep == "Ножницы":
            if usersStep == "Камень":
                print("Вы победили")
                usersWins += 1
                scissors += 1
                stones += 1
            elif usersStep == "Ножницы":
                print("Ничья")
                scissors += 2
            elif usersStep == "Бумага":
                print("Компьютер победил")
                computersWins += 1
                scissors += 1
                papers += 1

        if computersStep == "Бумага":
            if usersStep == "Камень":
                print("Компьютер победил")
                computersWins += 1
                papers += 1
                stones += 1
            elif usersStep == "Ножницы":
                print("Вы победили")
                usersWins += 1
                papers += 1
                scissors += 1
            elif usersStep == "Бумага":
                print("Ничья")
                papers += 2

    print("Компьютер: " + str(computersWins) + "; Вы: " + str(usersWins) + "; Камни: " + str(
        stones) + "; Ножницы: " + str(scissors) + "; Бумага: " + str(papers))


print("Выбери нужную лабу")
print("1. - Вывод 0;")
print("2. - Вывод W из *")
print("3. - Вывод по формуле")
print("4. - Вывод степеней")
print("5. - Годовая прибыль")
print("6. - Количество квадратов в прямоугольнике")
print("7. - Вывод максимально и минимального чётных чисел")
print("8. - Проверка даты")
print("9. - Обнуление чётных позиций")
print("10. - Прямоугольники")
print("11. - Расчёт конфет за доллары и в рублях")
print("12. - Вывод квадрата с диагональю 0")
print("13. - Подсчёт чётных чисел")
print("14. - Камень, ножницы, бумага")

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
if usersChoose == "12": lab12()
if usersChoose == "13": lab13()
if usersChoose == "
