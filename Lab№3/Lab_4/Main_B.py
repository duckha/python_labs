from abc import ABCMeta, abstractmethod
from random import randint


class State(metaclass=ABCMeta):

    @abstractmethod
    def do_something(self) -> None:
        pass


class Begin(State):
    def do_something(self) -> None:
        print(
            f"Приём в ВУЗ открыт.\nДокументы поданы.\nПроходной балл для 1 волны: {Admission.n1}, для волны 2: {Admission.n2}")


class Analyze_First_Wave(State):
    def do_something(self) -> None:
        print(f"Результат вступительных испытаний: {Admission.mark}.\nКонкурс 1 волна.")
        if Admission.mark > Admission.n1:
            print("Попадание в 1 волну.")


class Analyze_Second_Wave(State):
    def do_something(self) -> None:
        print(f"Конкурс 2 волна.")
        if Admission.mark >= Admission.n2:
            print("Попадание во 2 волну")
        else:
            print("Конкурс не пройден")


class Treatment(State):

    def do_something(self) -> None:
        print("Приказ о зачислении.")


class End(State):

    def do_something(self) -> None:
        print("Приём в ВУЗ закрыт.")


class Admission:
    mark = randint(60, 100)

    numbers1 = []
    for i in range(100):
        numbers1.append(randint(78, 85))

    numbers2 = []
    for i in range(100):
        numbers2.append(randint(70, 85))

    n1 = int(input("Введите проходной балл для первой волны"))
    n2 = int(input("Введите проходной балл для второй волны"))

    def __init__(self, state: State) -> None:
        self._state = state

    def change_state(self, state: State) -> None:
        self._state = state

    def do_something(self) -> None:
        self._state.do_something()


begin = Begin()
afw = Analyze_First_Wave()
asw = Analyze_Second_Wave()
treatment = Treatment()
end = End()

# first student
adm = Admission(begin)
adm.do_something()
adm.change_state(afw)
adm.do_something()

if adm.mark >= Admission.n1:
    adm.change_state(treatment)
    adm.do_something()
else:
    adm.change_state(asw)
    adm.do_something()
    if Admission.mark >= Admission.n2:
        adm.change_state(treatment)
        adm.do_something()
adm.change_state(end)
adm.do_something()

print("")

# second student
adm1 = Admission(begin)
adm1.do_something()
adm1.change_state(afw)
adm1.do_something()

if adm1.mark >= Admission.n1:
    adm1.change_state(treatment)
    adm1.do_something()
else:
    adm1.change_state(asw)
    adm1.do_something()
    if Admission.mark >= Admission.n2:
        adm1.change_state(treatment)
        adm1.do_something()
adm1.change_state(end)
adm1.do_something()
