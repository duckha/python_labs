from random import randint
from PyQt5 import QtWidgets
from tkinter import *
import datetime

import interface

list_logs = ['']
users_steps = 0


def write_in_logs(message):
    now = str(datetime.datetime.now())
    if message != " ":
        list_logs.append(message + "; " + now)
    else:
        list_logs.append(message)
    logs = open('logs', 'w')
    for line in list_logs:
        logs.write(line + '\n')
    print(message)


def write_in_stats(user_steps, comp_steps, user_wins, comp_wins):
    stats_dict = {"Users steps: ": user_steps, "Computers steps: ": comp_steps,
                  "Users wins: ": user_wins, "Computers wins: ": comp_wins}
    stats = open('stats', 'w')
    for key in stats_dict:
        print(key, stats_dict[key])
        stats.write(str(key) + str(stats_dict[key]) + '\n')


class ExampleApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):  #  Make a links with interface
    users_steps = 0
    comp_steps = 0
    comp_wins = 0
    users_wins = 0
    is_game_enabled = True

    def __init__(self):
        super().__init__()
        self.counts_int_bricks = randint(12, 20)
        self.setupUi(self)
        self.s = str(self.counts_int_bricks)
        self.count_of_bricks.setText("Количество кирпичей: " + self.s)
        self.push_button_1.clicked.connect(self.event_minus_one)
        self.push_button_2.clicked.connect(self.event_minus_two)
        self.push_button_3.clicked.connect(self.event_minus_three)
        self.action_stats.triggered.connect(self.open_stats)
        self.action_logs.triggered.connect(self.open_logs)

    @staticmethod
    def open_stats():
        stats_frame = Tk()
        listbox = Listbox(stats_frame, height=100, width=100)
        listbox.pack()
        listbox.insert(END, "Stats of game")
        with open('stats', 'r') as file:
            lst = file.readlines()
        for item in lst:
            listbox.insert(END, item)
        mainloop()

    @staticmethod
    def open_logs():
        frame_logs = Tk()
        listbox = Listbox(frame_logs, height=100, width=100)
        listbox.pack()
        listbox.insert(END, "This is logs")
        with open('logs', 'r') as file:
            lst = file.readlines()
        for item in lst:
            listbox.insert(END, item)
        mainloop()

    def game_again(self):
        self.counts_int_bricks = randint(12, 20)
        self.count_of_bricks.setText("Количество кирпичей: " + str(self.counts_int_bricks))
        self.is_game_enabled = True

    def make_step(self, num):
        self.users_steps += 1
        if self.is_game_enabled:
            self.counts_int_bricks -= num
            self.count_of_bricks.setText("")
            self.count_of_bricks.setText("Количество кирпичей: " + str(self.counts_int_bricks))
            write_in_logs("User makes step")
            write_in_stats(self.users_steps, self.comp_steps, self.users_wins, self.comp_steps)

            if self.counts_int_bricks <= 0:
                self.is_game_enabled = False
                self.users_wins += 1
                self.user_score.display(str(self.users_wins))
                write_in_logs("User win")
                write_in_logs(" ")
                self.game_again()

            if self.counts_int_bricks > 0:
                self.minus_comp()
                self.comp_steps += 1
                write_in_logs("Computer makes step")

                if self.counts_int_bricks <= 0:
                    self.is_game_enabled = False
                    self.comp_wins += 1
                    self.comp_score.display(str(self.comp_wins))
                    write_in_logs("Computer win")
                    write_in_logs(" ")
                    self.game_again()
        write_in_stats(self.users_steps, self.comp_steps, self.users_wins, self.comp_wins)

    def minus_comp(self):
        step = 0
        if self.counts_int_bricks > 15:
            step = randint(1, 3)
        else:
            if self.counts_int_bricks == 15:
                step = 3
            if self.counts_int_bricks == 14:
                step = 2
            if self.counts_int_bricks == 13:
                step = 1
            if self.counts_int_bricks == 12:
                step = 2
            if self.counts_int_bricks == 11:
                step = 3
            if self.counts_int_bricks == 10:
                step = 2
            if self.counts_int_bricks == 9:
                step = 1
            if self.counts_int_bricks == 8:
                step = 3
            if self.counts_int_bricks == 7:
                step = 3
            if self.counts_int_bricks == 6:
                step = 2
            if self.counts_int_bricks == 5:
                step = 1
            if self.counts_int_bricks == 4:
                step = randint(1, 3)
            if self.counts_int_bricks == 3:
                step = 3
            if self.counts_int_bricks == 2:
                step = 2
            if self.counts_int_bricks == 1:
                step = 1

        self.counts_int_bricks -= step
        self.comp_step.setText(str(step))
        self.count_of_bricks.setText("")
        self.count_of_bricks.setText("Количество кирпичей: " + str(self.counts_int_bricks))

    def event_minus_one(self):
        self.make_step(1)

    def event_minus_two(self):
        self.make_step(2)

    def event_minus_three(self):
        self.make_step(3)


def main():
    app = QtWidgets.QApplication(sys.argv)  # new QApplication
    window = ExampleApp()  # Create new object of ExampleApp launch app
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
