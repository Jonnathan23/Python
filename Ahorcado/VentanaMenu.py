from tkinter import *
from VentanaInicio import *
from GeneratePhrase import generatePhrase as gP
import random

diccionario = ["Murciélago", "Mariposa", "Elefante","Guitarra","Catarata","Chocolate","Computadora","Biblioteca","Aventura","Tortuga","Pintura","Helicóptero","Camiseta","Maquillaje","Fútbol","Helado","Serpiente","Dinosaurio"
,"Invierno","Montaña","Pájaro","Arcoíris","Espejo","Cámara","Papel","Globo","Telescopio","Nube","Luna","Barco","León","Café","Perro","Tigre","Radio","Sol","Unicornio","Avión","Árbol","Reloj","Hamburguesa","Playa"
,"Tren","Delfín","Fruta","Calendario"
,"Sombrero","Pelota","Plátano","Payaso"]



class VentanaMenu:
    def __init__ (self):
        self.root = Tk()
        self.root.title("Menu")
        
        
        self.frame = Frame()
        self.frame.pack()
        
        #*  TITLE
        Label(self.frame, text="Bienvenido").grid(row=0 , column= 0, padx= 50, pady=15)
        
        #*  BUTTONS
        # Button's dimension
        btPadx = 75
        btPady = 20
        btWidth = 20
        #   create bt
        self.btSinglePlayer = Button(self.frame, text="Un solo jugador",
                                command= self.singlePlayer, width = btWidth)
        self.btSinglePlayer.grid(row=1, column=0, padx= btPadx, pady= btPady)
        
        self.btTwoPlayers = Button(self.frame, text="Dos jugadores",
                                command= self.twoPlayers, width= btWidth)
        self.btTwoPlayers.grid(row=2, column= 0, padx= btPadx, pady= btPady)
        
        
        self.root.mainloop()
        
        
    
    def singlePlayer(self):
        wordRandom = random.choice(diccionario)
        phrase = gP(wordRandom)
        print(wordRandom)
        print(phrase + "\n-----")        
        self.root.destroy()
        self.ventanaJuego = VentanaJuego(wordRandom,phrase)
    
    def twoPlayers(self):
        self.root.destroy()
        self.ventanaInicio = VentanaIn()
