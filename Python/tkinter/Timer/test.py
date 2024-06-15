from tkinter import *
from tkinter import ttk

def on_select(event):
    index = listbox.curselection()[0]
    selected_language.set(languages[index])

languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", 
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
  
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

selected_language = StringVar()
  
languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
listbox.bind("<<ListboxSelect>>", on_select)
  
scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
  
listbox["yscrollcommand"] = scrollbar.set
  
selected_label = Label(root, textvariable=selected_language)
selected_label.pack()

root.mainloop()