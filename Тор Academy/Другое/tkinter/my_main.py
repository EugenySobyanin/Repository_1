from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("Приложение Сабэна")     # устанавливаем заголовок окна
root.geometry("900x250")    # устанавливаем размеры окна
 
label = Label(text="Диджей Сабен") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()