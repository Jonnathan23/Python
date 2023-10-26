
def generatePhrase(word):
        phrase = ""
        for c in word:
            print(c)
            if(c == " "):
                phrase += " - "
            else:
                phrase += "_ "
        return phrase