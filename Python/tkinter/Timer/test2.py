"""Запрос: напиши пример простого кода на python, tkinter, где в окне расположен скроллбар с числами, пользователь кликает по числу и оно записывается в переменную

поменяй немного, вместо скроллбара обычный листбокс
"""

import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_value.set(listbox.get(selected_index))

root = tk.Tk()
root.title('Listbox Example')

# Создаем Listbox с числами
numbers = list(range(1, 101))
selected_value = tk.StringVar()

listbox = tk.Listbox(root)
for num in numbers:
    listbox.insert(tk.END, num)
listbox.pack()

# Переменная, в которую будет записываться выбранное число

listbox.bind('<<ListboxSelect>>', on_select)

selected_label = tk.Label(root, textvariable=selected_value)
selected_label.pack()

root.mainloop()