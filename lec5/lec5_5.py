from tkinter import *


def handler1(event):
    print("Hello World!")


def handelr2(event):
    exit()


# инициализация
root = Tk()
hello_label = Label(root, text="Hello, world!", font="Times 40")
hello_label.pack()

# привязка обработчиков - к событию и виджету:
# виджет.bind(событие, обработчик)
hello_label.bild('<Button-1>', handler1)
hello_label.bild('<Button-3>', handler2)

# гдавный цикл (проект)
root.mainloop()
#window.title("Добро пожаловать в приложение PythonRu")
# window.mainloop()
