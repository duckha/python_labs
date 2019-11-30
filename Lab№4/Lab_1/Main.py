from tkinter import *

main_window = Tk()
color_name_label = Label(main_window, bg='white', fg='black', width=20)
color_code_entry = Entry(main_window, text="цвет", width=20)
color_name_label.pack()
color_code_entry.pack()


class ChangeButton:
    def __init__(self, color, num):
        self.button = Button(bg=color, width=20)
        self.button.bind('<Button-1>', self.change)
        self.button.pack()
        self.color = color
        self.num = num

    def change(self, event):
        color_name_label.config(text=self.color)
        color_code_entry.delete(0, 'end')
        color_code_entry.insert(1, " " * 13 + self.num)


red = ChangeButton('red', '#ff0000')
orange = ChangeButton('orange', "#ff7d00")
yellow = ChangeButton('yellow', "#ffff00")
green = ChangeButton('green', "#00ff00")
blue = ChangeButton('blue', "#007dff")
dark_blue = ChangeButton('dark blue', "#0000ff")
violet = ChangeButton('violet', "#7d00ff")
main_window.mainloop()
