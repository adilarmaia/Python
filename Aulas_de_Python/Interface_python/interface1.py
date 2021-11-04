
# INTERFACE COM MENU...

from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x300")
root.config(bg="goldenrod3")
root.title("Menu OS")

menuBar = Menu(root)
root.config(menu=menuBar)

def finalizar():     
    messagebox.askquestion("finalizar", message="Deseja fechar?")  # FUNÇÃO DE PERGUNTAR ...

def licenca():
    messagebox.showinfo("version", message= "version Beta 1.0.21 - Desenvolvedor Adilar Maia")

def erro():
    messagebox.showerror("erro! guardar", message= "não foi possível guardar")

def atencao():
    messagebox.showwarning("Atenção!", message="O atual será excluido")

archivoMenu = Menu(menuBar, tearoff=0)

archivoMenu.add_command(label="Novo")
archivoMenu.add_command(label="Abrir", command=atencao)
archivoMenu.add_command(label="Guarda", command=erro)
archivoMenu.add_command(label="Finalizar", command=finalizar)
archivoMenu.add_separator()
archivoMenu.add_command(label="sair", command=root.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Colar")

ajudaMenu = Menu(menuBar, tearoff=0)
ajudaMenu.add_command(label="Ajuda", command=licenca)
ajudaMenu.add_separator()

menuBar.add_cascade(label="Arquivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)
menuBar.add_cascade(label="Ajuda", menu=ajudaMenu)

root.mainloop()
