
from tkinter import *
# Ventana
raiz = Tk()
raiz.title("Ventana Pepa")
raiz.iconbitmap("Graficos//pugIco.ico")
raiz.config(bg="green")


# Frame
nuevoFrame = Frame(raiz, width="500", height="450")
nuevoFrame.pack()

# Label
img = PhotoImage(file="Graficos//capi.gif")
Label(nuevoFrame, image = img).place(x=50, y = 15)

nuevoLabel = Label(nuevoFrame, text= "Capibara")
nuevoLabel.place(x= 100,y=275)



raiz.mainloop()