from tkinter import *
from VentanaJuegoDos import *
from GeneratePhrase import generatePhrase as gP
class VentanaIn():
    
    def __init__(self):                
        self.root = Tk()    
        self.root.title("Insert word")
        self.word = ""

        self.frame = Frame(self.root)
        self.frame.pack()

        Label(self.frame, text="Insert word").grid(
            row=0, column=0, padx=15, pady=25)
        self.txtWord = Entry(self.frame)
        self.txtWord.grid(row=0, column=1, padx=10)

        btPlay = Button(self.frame, text="Jugar", command = self.comenzarJuego)
        btPlay.grid(row=1, column=1, sticky="w", pady=5) # TODO: Falta asignar el evento
        self.root.mainloop()  
   
   
    
    def comenzarJuego(self):
        word = self.txtWord.get()
        word = word.upper()
        phrase = gP(word)
        self.root.destroy()
        print("Iniciando Juego")
        print(self.word)
        self.ventanaJuego = VentanaJuego(word,phrase)
        