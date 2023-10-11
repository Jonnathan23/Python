from tkinter import *
# Ventana
raiz = Tk()
raiz.title("Ventana Pepa")
raiz.iconbitmap("Graficos//pugIco.ico")
raiz.config(bg="green")

# Frame
nuevoFrame = Frame()
nuevoFrame.pack(side="bottom", anchor=W)
nuevoFrame.config(bg="red")
nuevoFrame.config(width="260", height="80")

raiz.mainloop()