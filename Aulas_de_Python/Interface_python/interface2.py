
from tkinter import *
from tkinter import messagebox

# AINDA EM CONSTRUÇÃO AULA 2 

janela = Tk()
janela.title('Systems OS') 
janela.geometry('500x400')

w= Spinbox(janela, values=("Python", "HTML", "Java", "Javascript"))
w.pack()

e = Spinbox(janela, values=("carnes", "Verduras", "Legumes", "Frutas"))
e.pack()



janela.mainloop()
