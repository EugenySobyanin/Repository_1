from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

root = Tk()
root.title("METANIT.COM")
root.geometry("800x600+450+150")


def correct_bracket(expression):
    stack = []
    open_brackets = '([{'
    close_brackets = ')]}'
    expression = str(expression)
    for i in range(len(expression)):
        if expression[i] in open_brackets:
            stack.append(expression[i])
        elif expression[i] in close_brackets:
            if close_brackets.find(expression[i]) == open_brackets.find(stack[len(stack) - 1]):
                pass
            else:
                return False
    return True
            
        
def printHello():
    showinfo("Приветствие", "Привет мир!")


def sum(a, b):
    showinfo("Результат", f"{a+b}")


number1 = 5
number2 = 5


btn = ttk.Button(text=f"{number1}+{number2}=?",
                 command=lambda: sum(number1, number2),
                 )  # создаем кнопку из пакета ttk
btn.pack()


def show_message(message):
    try:
        label["text"] = eval(message)
    except NameError:
        showinfo("Ошибка", "Проверьте корректность введенных данных.")
        entry.delete(0, END)
    except ZeroDivisionError:
        showinfo("Ошибка", "На ноль делить нельзя.")
        entry.delete(0, END)
        

entry = ttk.Entry(font=("Arial", 16))
entry.pack(anchor=NW, padx=6, pady=6,)

btn = ttk.Button(text="Click", command=lambda: show_message(entry.get()))
btn.pack(anchor=NW, padx=6, pady=6)
# привязка события (нажатие клавиши Enter)
btn.bind('<KeyPress-KP_Enter>', lambda: show_message(entry.get())) # не работает

label = ttk.Label(font=("Arial", 16))
label.pack(anchor=NW, padx=6, pady=6,)

root.mainloop()
