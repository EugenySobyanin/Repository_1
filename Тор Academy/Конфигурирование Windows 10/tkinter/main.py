from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

root = Tk()
root.title("METANIT.COM")
root.geometry("800x600")


def printHello():
    showinfo("Приветствие", "Привет мир!")


def sum(a, b):
    showinfo("Результат", f"{a+b}")


number1 = 5
number2 = 5


btn = ttk.Button(text=f"{number1}+{number2}=?", command=lambda: sum(number1, number2),
                 )  # создаем кнопку из пакета ttk

btn.pack()    # размещаем кнопку в окне


def show_message(message):
    label["text"] = eval(message)  # получаем введенный текст


entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=lambda: show_message(entry.get()))
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
