from  tkinter import *
from Buttons import createBt
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
        
       
        
        # *buttons
        widthBt = 5
        heightBt = 2
        
        self.btA = createBt(self.framePlay,"A", 1,0, self.wordGuess, self.phraseGuess, self)
        self.btB = createBt(self.framePlay,"B", 1,1, self.wordGuess, self.phraseGuess, self)
        self.btC = createBt(self.framePlay,"C", 1,2, self.wordGuess, self.phraseGuess, self)
        self.btD = createBt(self.framePlay,"D", 1,3, self.wordGuess, self.phraseGuess, self)
        
        self.btE = createBt(self.framePlay,"E", 2,0, self.wordGuess, self.phraseGuess, self)
        self.btF = createBt(self.framePlay,"F", 2,1, self.wordGuess, self.phraseGuess, self)
        self.btG = createBt(self.framePlay,"G", 2,2, self.wordGuess, self.phraseGuess, self)
        self.btH = createBt(self.framePlay,"H", 2,3, self.wordGuess, self.phraseGuess, self)
        
        self.btI = createBt(self.framePlay,"I", 3,0, self.wordGuess, self.phraseGuess, self)
        self.btJ = createBt(self.framePlay,"J", 3,1, self.wordGuess, self.phraseGuess, self)
        self.btK = createBt(self.framePlay,"K", 3,2, self.wordGuess, self.phraseGuess, self)
        self.btL = createBt(self.framePlay,"L", 3,3, self.wordGuess, self.phraseGuess, self)
        
        self.btM = createBt(self.framePlay,"M", 4,0, self.wordGuess, self.phraseGuess, self)
        self.btN = createBt(self.framePlay,"N", 4,1, self.wordGuess, self.phraseGuess, self)
        self.btNE = createBt(self.framePlay,"Ñ", 4,2, self.wordGuess, self.phraseGuess, self)
        self.btO = createBt(self.framePlay,"O", 4,3, self.wordGuess, self.phraseGuess, self)
        
        self.btP = createBt(self.framePlay,"P", 5,0, self.wordGuess, self.phraseGuess, self)
        self.btQ = createBt(self.framePlay,"Q", 5,1, self.wordGuess, self.phraseGuess, self)
        self.btR = createBt(self.framePlay,"R", 5,2, self.wordGuess, self.phraseGuess, self)
        self.btS = createBt(self.framePlay,"S", 5,3, self.wordGuess, self.phraseGuess, self)
        
        self.btT = createBt(self.framePlay,"T", 6,0, self.wordGuess, self.phraseGuess, self)
        self.btU = createBt(self.framePlay,"U", 6,1, self.wordGuess, self.phraseGuess, self)
        self.btV = createBt(self.framePlay,"V", 6,2, self.wordGuess, self.phraseGuess, self)
        self.btW = createBt(self.framePlay,"W", 6,3, self.wordGuess, self.phraseGuess, self)
        
        self.btX = createBt(self.framePlay,"X", 7,0, self.wordGuess, self.phraseGuess, self)
        self.btY = createBt(self.framePlay,"Y", 7,1, self.wordGuess, self.phraseGuess, self)
        self.btZ = createBt(self.framePlay,"Z", 7,2, self.wordGuess, self.phraseGuess, self)
        
         #* Hanged IMG
        imgHanged = PhotoImage(file="imgs//capi.gif")
        self.lbImgHanged = Label(self.framePlay, image= imgHanged).grid(row=0, column=4, padx=15, pady=15)
      
    def updatePhrase(self,phrase):
        self.phraseGuess = phrase    