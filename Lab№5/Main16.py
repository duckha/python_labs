def main():
    d = {"ivan_egorov": "passy", "yuzer": "qwert", "boris": "1234", "waflee": "4321helloworld", "qwerty21": "0987"}
    login = input("Введите логин")
    password = d.get(login)
    b = any(map(str.isdigit, password))
    a = len(password) > 6
    if b & a:
        print(password, ": Пароль безопасен")
    else:
        print(password, ": Пароль не безопасен")

if __name__ == '__main__':
    main()
