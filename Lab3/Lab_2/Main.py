class Human:
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
    def get_age(self):
        return 2019 - self.year_of_birth
    def set_name(self, name):
        self.name = name

class Student(Human):
    year = 0
    def __init__(self, name, year_of_birth, year):
        super().__init__(name, year_of_birth)
        self.set_year(year)
        self.course = 0

    def set_year(self, year):
        if 16 < self.get_age() < 28:
            self.year = year
            self.course = 1
            print(self.year)
        else:
            print("Не подходит")

    def next_year(self):
        if self.course & self.course < 5:
            self.course += 1
            print(f'В {self.year + self.course - 1} будет на {self.course}.')
        elif self.course == 5:
            print(f'Год выпуска: {self.year + 6}')
        

  
s = Student("Ivan", 2000, 2019)
s1 = Student("Oleg", 1997, 2017)
for i in range (7):
    s.next_year()
print('=' * 16)
for i in range (7):
    s1.next_year()

