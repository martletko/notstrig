from tkinter import *
from db_lab4 import *
import os


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Создать заметку")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Заметка")
        lbl.grid(sticky=W, pady=4, padx=5)

        self.area = Text(self)
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4,
                       padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="Save", command=self.save)
        abtn.grid(row=1, column=3)

    def save(self):
        data = self.area.get('1.0', END)
        curr_dir = os.getcwd()
        tmp_name = 'tmp.txt'
        tmp_path = os.path.join(curr_dir, tmp_name)
        with open(tmp_path, "w", encoding='utf-8') as file:
            file.write(data)

        self.exitbutton()

    def exitbutton(self):
        self.parent.destroy()


class Example1(Frame):
    def __init__(self, parent, text_message):
        Frame.__init__(self, parent)
        self.parent = parent
        self.text_message = text_message
        self.initUI(text_message)

    def initUI(self, text_message):
        self.parent.title("Редактировать заметку")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Заметка")
        lbl.grid(sticky=W, pady=4, padx=5)

        self.area = Text(self)
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4,
                       padx=5, sticky=E+W+S+N)
        self.area.insert('1.0', text_message)

        abtn = Button(self, text="Save", command=self.save)
        abtn.grid(row=1, column=3)

    def save(self):
        data = self.area.get('1.0', END)
        curr_dir = os.getcwd()
        tmp_name = 'tmp.txt'
        tmp_path = os.path.join(curr_dir, tmp_name)
        with open(tmp_path, "w", encoding='utf-8') as file:
            file.write(data)
        self.exitbutton()

    def exitbutton(self):
        self.parent.destroy()


def main_screen():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()


def read_screen(text_message):
    add_text = text_message
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example1(root, add_text)
    root.mainloop()


if __name__ == '__main__':
    pass
