from tkinter import*
import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1200x320')
root.resizable(1200,320)
root['bg'] = 'orange'

root.title('LANGUAGE TRANSLATER')
Label(root,text="LANGUAGE TRANSLATER",font="Arial 20 bold").pack()

Label(root,text = "Enter Text",font = "Arial 13 bold",bg= "white smoke").place(x=165,y=90)


Input_text = Entry(root,width= 60)
Input_text.place(x=30,y=130)
Input_text.get()
Label(root,text= "Output",font="Arial 13 bold",bg="white smoke").place(x=700,y=90)
Output_text= Text(root,font="Arial 10", height = 5,wrap= WORD,padx=5,pady=5,width=50)
Output_text.place(x=600,y=130)

language = list(LANGUAGES.values())

lang= ttk.Combobox(root, values=language, width = 22)
lang.place(x=130,y=180)
lang.set("choose language")


lang = ttk.Combobox(root, values=language, width = 22)
lang.set("choose language")

def Translate():
    translator = Translator()
    try:
        translated = translator.translate(text=Input_text.get(),dest = lang.get() or "english")
        Output_text.delete(1.0, END)
        Output_text.insert(END,translated.text)
    except:
        Output_text.delete(1.0, END)
        Output_text.insert(END,"An error occurred.")

trans=Button(root,text="Translate",font="arial 12 bold",pady=5, command= Translate ,bg= "orange", activebackground="green")
trans.place(x=445,y=180)


clear=Button(root,text="Clear",font="arial 12 bold",pady=5, command= lambda: clear_all() ,bg= "orange", activebackground="green")
clear.place(x=700,y=180)

def clear_all():
    Input_text.delete(0,END)
    Output_text.delete(1.0, END)



root.mainloop()


