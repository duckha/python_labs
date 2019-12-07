def main():
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

if __name__ == '__main__':
    main()
