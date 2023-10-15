from  tkinter import *

class VentanaJuego:
    def __init__(self,wordGuess, phraseGuess):        
        self.wordGuess = wordGuess
        self.phraseGuess = phraseGuess
        
        self.rootPlay = Tk()
        self.rootPlay.title("Hanged")
        
        self.framePlay = Frame()
        self.framePlay.pack()       
        
        self.wordGuess = Label(self.framePlay,text= phraseGuess)
        self.wordGuess.grid(row=0, column=1, sticky="e", pady=6)
        
        # *Hanged IMG
        imgHanged = 
        # *buttons
        widthBt = 5
        heightBt = 2
        # Fila 1
        self.btA = Button(self.framePlay , text="A", width= widthBt, height= heightBt, command=self.comprobateLetter("A"))
        self.btA.grid(row=1, column=0, padx=5, pady=5)
        
        self.btB = Button(self.framePlay , text="B", width= widthBt, height= heightBt, command=self.comprobateLetter("B"))
        self.btB.grid(row=1, column=1, padx=5, pady=5)
        
        self.btC = Button(self.framePlay , text="C", width= widthBt, height= heightBt, command=self.comprobateLetter("C"))
        self.btC.grid(row=1, column=2, padx=5, pady=5)
        
        self.btD = Button(self.framePlay , text="D", width= widthBt, height= heightBt, command=self.comprobateLetter("D"))
        self.btD.grid(row=1, column=3, padx=5, pady=5)
        
        #Fila 2
        
        self.btE = Button(self.framePlay , text="E", width= widthBt, height= heightBt, command=self.comprobateLetter("E"))
        self.btE.grid(row=2, column=0, padx=5, pady=5)
        
        self.btF = Button(self.framePlay , text="F", width= widthBt, height= heightBt, command=self.comprobateLetter("F"))
        self.btF.grid(row=2, column=1, padx=5, pady=5)
        
        self.btG = Button(self.framePlay , text="G", width= widthBt, height= heightBt, command=self.comprobateLetter("G"))
        self.btG.grid(row=2, column=2, padx=5, pady=5)
        
        self.btH = Button(self.framePlay , text="H", width= widthBt, height= heightBt, command=self.comprobateLetter("H"))
        self.btH.grid(row=2, column=3, padx=5, pady=5)
        
        #Fila 3
        
        self.btI = Button(self.framePlay , text="I", width= widthBt, height= heightBt, command=self.comprobateLetter("I"))
        self.btI.grid(row=3, column=0 , padx=5, pady=5)
        
        self.btJ = Button(self.framePlay , text="J", width= widthBt, height= heightBt, command=self.comprobateLetter("J"))
        self.btJ.grid(row=3, column=1, padx=5, pady=5)
        
        self.btK = Button(self.framePlay , text="K", width= widthBt, height= heightBt, command=self.comprobateLetter("K"))
        self.btK.grid(row=3, column=2, padx=5, pady=5)
        
        self.btL = Button(self.framePlay , text="L", width= widthBt, height= heightBt, command=self.comprobateLetter("L"))
        self.btL.grid(row=3, column=3, padx=5, pady=5)
        
        # FILA 4
        
        self.btM = Button(self.framePlay , text="M", width= widthBt, height= heightBt, command=self.comprobateLetter("M"))
        self.btM.grid(row=4, column=0, padx=5, pady=5)
        
        self.btN = Button(self.framePlay , text="N", width= widthBt, height= heightBt, command=self.comprobateLetter("N"))
        self.btN.grid(row=4, column=1, padx=5, pady=5)
        
        self.btO = Button(self.framePlay , text="O", width= widthBt, height= heightBt, command=self.comprobateLetter("O"))
        self.btO.grid(row=4, column=2)
        
        self.btP = Button(self.framePlay , text="P", width= widthBt, height= heightBt, command=self.comprobateLetter("P"))
        self.btP.grid(row=4, column=3, padx=5, pady=5)
        
        # FILA 5
        
        self.btQ = Button(self.framePlay , text="Q", width= widthBt, height= heightBt, command=self.comprobateLetter("Q"))
        self.btQ.grid(row=5, column=0, padx=5, pady=5)
        
        self.btR = Button(self.framePlay , text="R", width= widthBt, height= heightBt, command=self.comprobateLetter("R"))
        self.btR.grid(row=5, column=1, padx=5, pady=5)
        
        self.btS = Button(self.framePlay , text="S", width= widthBt, height= heightBt, command=self.comprobateLetter("S"))
        self.btS.grid(row=5, column=2, padx=5, pady=5)
        
        self.btT = Button(self.framePlay , text="T", width= widthBt, height= heightBt, command=self.comprobateLetter("T"))
        self.btT.grid(row=5, column=3, padx=5, pady=5)
        
        # FILA 6
        
        self.btU = Button(self.framePlay , text="U", width= widthBt, height= heightBt, command=self.comprobateLetter("U"))
        self.btU.grid(row=6, column=0, padx=5, pady=5)
        
        self.btV = Button(self.framePlay , text="V", width= widthBt, height= heightBt, command=self.comprobateLetter("V"))
        self.btV.grid(row=6, column=1, padx=5, pady=5)
        
        self.btW = Button(self.framePlay , text="W", width= widthBt, height= heightBt, command=self.comprobateLetter("W"))
        self.btW.grid(row=6, column=2, padx=5, pady=5)
        
        self.btX = Button(self.framePlay , text="X", width= widthBt, height= heightBt, command=self.comprobateLetter("X"))
        self.btX.grid(row=6, column=3, padx=5, pady=5)
        
        #FILA 7
        
        self.btY = Button(self.framePlay , text="Y", width= widthBt, height= heightBt, command=self.comprobateLetter("Y"))
        self.btY.grid(row=7, column=0, padx=5, pady=5)
        
        self.btZ = Button(self.framePlay , text="Z", width= widthBt, height= heightBt, command=self.comprobateLetter("Z"))
        self.btZ.grid(row=7, column=1, padx=5, pady=5)
        
        
        self.wordGuess.mainloop()
    
    def comprobateLetter(self, letter):
        print("Hola")