from tkinter import *
def iniciarJuego():
    print("Bienvenido")
    
root = Tk()
root.config()
root.title("Botones")
miFrame = Frame(root)
miFrame.pack()

Label(miFrame, text="Ingrese palabra:").grid(row=0, column=0, sticky="e", padx=15, pady=50)
txtPalabra = Entry(miFrame, width=20).grid(row=0, column=1, sticky="w", padx=15, pady=50)

# Boton
btJugar = Button(miFrame, text="Jugar", justify="center", command= iniciarJuego).grid(row=1, column=1, pady=20, sticky="w")


root.mainloop()