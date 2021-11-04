
from tkinter import *
root = Tk()
root.geometry("400x300")
root.config(bg="goldenrod3")
root.title("Menu OS")

menuBar = Menu(root)
root.config(menu=menuBar)
archivoMenu = Menu(menuBar, tearoff=0)

archivoMenu.add_command(label="Novo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guarda")
archivoMenu.add_command(label="Finalizar")
archivoMenu.add_separator()
archivoMenu.add_command(label="sair", command=root.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Colar")

ajudaMenu = Menu(menuBar, tearoff=0)
ajudaMenu.add_command(label="Ajuda")
ajudaMenu.add_separator()

menuBar.add_cascade(label="Arquivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)
menuBar.add_cascade(label="Ajuda", menu=ajudaMenu)

root.mainloop()
