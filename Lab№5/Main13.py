def main():
    courseOfDollar = int(input("Введите курс доллара"))
    for dollars in range(1, 100):
        weight = 3.5
        roubles = dollars * courseOfDollar
        weight = weight * dollars
        dollarsStr = str(dollars)
        roublesStr = str(roubles)
        weightStr = str(weight)
        print(dollarsStr + "$; " + roublesStr + "Р; " + weightStr + "КГ")

if __name__ == '__main__':
    main()

