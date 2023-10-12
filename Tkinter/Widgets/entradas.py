from tkinter import *

raiz = Tk()
raiz.title("Entrada")
miFrame = Frame(raiz, width = "600" , height="400")
miFrame.pack()

Label(miFrame, text="Ingrese palabra").grid(row=0, column=0, sticky="e", padx=25)
# Cuadro de texto
txtEntrada = Entry(miFrame)
txtEntrada.config(justify="center")
txtEntrada.grid(row=0, column=1, sticky="w", pady=75, padx=25)


raiz.mainloop()