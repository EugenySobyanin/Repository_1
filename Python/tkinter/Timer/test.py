import tkinter as tk

def start_timer():
    # Скрыть элементы интерфейса
    hour_scroll.pack_forget()
    minute_scroll.pack_forget()
    start_button.pack_forget()

    total_seconds = hour_scroll.get() * 3600 + minute_scroll.get() * 60
    update_time(total_seconds)

def countdown(timer):
    if timer > 0:
        hours = timer // 3600
        minutes = (timer % 3600) // 60
        seconds = timer % 60
        time_label.config(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}')
        root.after(1000, countdown, timer - 1)
    else:
        time_label.config(text='Time\'s up!')

def update_time(seconds):
    countdown(seconds)

root = tk.Tk()
root.title('Simple Timer')

hour_scroll = tk.Scale(root, from_=0, to=23, orient=tk.HORIZONTAL, label='Hours')
hour_scroll.pack()

minute_scroll = tk.Scale(root, from_=0, to=59, orient=tk.HORIZONTAL, label='Minutes')
minute_scroll.pack()

start_button = tk.Button(root, text='Start Timer', command=start_timer)
start_button.pack()

time_label = tk.Label(root, text='')
time_label.pack()

root.mainloop()