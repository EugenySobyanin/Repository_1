import tkinter as tk
from lib.evaluator import *
from lib.parser import *

tokens = []


def appendToken(token):
    if len(tokens) < 1:
        tokens.append(token)
        return

    if isOperator(token):
        if not (isOperator(tokens[len(tokens)-1])):
            tokens.append(token)
        else:
            tokens[len(tokens)-1] = token
    else:
        if token == '(' or token == ')':
            tokens.append(token)
        else:
            last = tokens[len(tokens)-1]
            if isOperator(last) or last == '(' or last == ')':
                tokens.append(token)
            else:
                tokens[len(tokens)-1] += token


def tokensToString():
    ans = ""
    for token in tokens:
        if isOperator(token):
            ans += " " + token + " "
        else:
            splitted = token.split('.')
            if (len(splitted) == 2):
                if len(splitted[1]) == 1 and splitted[1] == '0':
                    ans += splitted[0]
                else:
                    ans += token
            else:
                ans += token
    return ans


def update_display(value):
    appendToken(value)
    new_text = tokensToString()
    display.set(new_text)


def calculate_result():
    try:
        result = Evaluate(Parse(tokens))
        tokens.clear()
        update_display(result)
    except Exception as e:
        display.set("Error")


def clear_display():
    tokens.clear()
    display.set("")


# Создаём основное окно tkinter
parent = tk.Tk()
parent.configure(bg="black")
parent.title("Калькулятор")

# В этой переменной храним значение для отображения на экране
display = tk.StringVar()
display.set("")


display_entry = tk.Entry(parent, textvariable=display,
                         font=("Arial", 18), justify="right", bg="lightpink")
display_entry.grid(row=0, column=0, columnspan=4,
                   padx=10, pady=10, ipadx=10, ipady=10)

button_labels = [
    '7', '8', '9', '/', '(',
    '4', '5', '6', '*', ')',
    '1', '2', '3', '-', '^',
    '0', '.', '=', '+', 'C'
]

# Create and arrange the buttons in a grid
row_val = 1
col_val = 0

for label in button_labels:
    if label == '=':
        tk.Button(parent, text=label, padx=30, pady=30, width=2, height=1, font=(
            "Arial", 16), bg="sky blue", command=calculate_result).grid(row=row_val, column=col_val)
    elif label == 'C':
        tk.Button(parent, text=label, padx=30, pady=30, width=2, height=1, font=(
            "Arial", 16), bg="sky blue", command=clear_display).grid(row=row_val, column=col_val)
    else:
        print(f'Сработал цикл блок элс для {label}')
        tk.Button(parent, text=label, padx=30, pady=30, width=2, height=1, font=("Arial", 16), bg="sky blue",
                  command=lambda l=label: update_display(l)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Run the Tkinter main loop
parent.mainloop()
