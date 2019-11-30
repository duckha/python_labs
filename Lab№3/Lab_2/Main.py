class Human:
    year_of_birth = 0

    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    age = 2019 - year_of_birth


class Student(Human):
    year_of_birth = 0
    year_of_study = 0
    end_of_study = 0

    def __init__(self, name, year_of_birth):
        super().__init__(name, year_of_birth)

    def getCourse(self, course):
        return self.year_of_study + course - 1

    def makeStartAndEnd(self):
        if self.age >= 17 & self.age <= 27:
            self.year_of_study = 2019
            count = int(input("Сколько нужно учиться"))
            self.end_of_study = self.year_of_study + count - 1
        else:
            self.year_of_study = -1

    def makeStudent(self):
        if (self.year_of_birth < 1992) | (self.year_of_birth > 2002):
            print(f"Имя {self.name}; Возраст не подходит")
        else:
            print("Привет, ", self.name)
            self.makeStartAndEnd()
            print(f"Год Поступление {self.year_of_study}; Имя {self.name}; Год окончания учёбы {self.end_of_study}")
            print('Какой курс вам нужен?')
            print(s.getCourse(int(input())))


s = Student("Ivan", 2002)
s.makeStudent()

s1 = Student("Oleg", 1998)
s1.makeStudent()

s2 = Student("B", 1970)
s2.makeStudent()

