from tkinter import Button
from Principal import showPhrase
def createBt(container,letter, rowBt, colBt, word, phrase, windowPlay):
    widthBt = 5
    heightBt = 2
    return Button(container , text=letter, width= widthBt, height= heightBt,
                command =lambda l=letter, w=word, p=phrase, wP = windowPlay: comprobateLetter(l,w,p)).grid(
        row=rowBt, column=colBt, padx=5, pady=5)

def comprobateLetter(letter, word, phrase):
    print(f'Letra: {letter}')
    print(f'Palabra: {word}')
    print(f'Frase: {phrase}')
    showPhrase()