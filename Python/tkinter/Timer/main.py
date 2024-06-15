from tkinter import *
from tkinter import ttk     # подключаем пакет ttk
import datetime as dt

from pydub import AudioSegment
from pydub.playback import play


hours = [str(el) for el in range(24)]
minutes = [str(el) for el in range(60)]
my_font = ('Arial', 16)
my_font_bold = ('Arial', 18, 'bold')



def on_select(event):
    index = listbox_hours.curselection()[0]
    hours_select_var.set(hours[index])

def on_select2(event):
    index = listbox_min.curselection()[0]
    min_select_var.set(minutes[index])


def time_count():
    root.update()
    


a = dt.datetime.now()
print(a)


# def show_massage():
#     label2['text'] = entry1.get()
    


root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("600x500")    # устанавливаем размеры окна

label = Label(text="Введите время", font=my_font) # создаем текстовую метку
label.pack()    # размещаем метку в окне

# entry1 = ttk.Entry()
# entry1.pack(anchor="center", pady=[20, 0])


frame = ttk.Frame()
frame.pack()

# entry1.place(height=30, width=100, x=50, y=100)
# entry1.place(anchor='center')
# entry1.grid(column=6, row=6)
# entry1.pack(anchor=CENTER, expand=1)

hours_var = StringVar(value=hours)
min_var = StringVar(value=minutes)
hours_select_var= StringVar()
min_select_var = StringVar()
listbox_hours = Listbox(frame, listvariable=hours_var, height=5, width=3, font=my_font)
listbox_min = Listbox(frame, listvariable=min_var, height=5, width=3, font=my_font)
listbox_hours.pack(side=LEFT)
listbox_min.pack(side=LEFT)

listbox_hours.bind("<<ListboxSelect>>", on_select)
listbox_min.bind("<<ListboxSelect>>", on_select2)


frame2 = Frame()
frame2.pack()


label_hours_selected = Label(frame2,textvariable=hours_select_var, font=my_font_bold)
label_hours_selected.pack(side=LEFT)

label_min_selected = Label(frame2,textvariable=min_select_var, font=my_font_bold)
label_min_selected.pack(side=LEFT)



button1 = ttk.Button(text="Запустить таймер", width=25, command=time_count)
button1.pack()

# label2 = Label()
# label2.pack()






# audio = AudioSegment.from_file("Timer\\audio\home.mp3", format="mp3")
# play(audio)
root.mainloop()