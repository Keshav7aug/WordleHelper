import nltk
from nltk.corpus import words
import tkinter
Ewords = [word.lower() for word in words.words() if len(word)==5]

def getWords(words,p,w):
    return [word for word in words if word[p]==w]
def getWordsNot(words,p,w):
    return [word for word in words if word[p]not in w]
def withWords(words,C):
    A=[]
    for word in words:
        for l in C:
            if l not in word:
                break
        else:
            A.append(word)
    return A
def notWithWords(words,X):
    A=[]
    for word in words:
        for l in word:
            if l in X:
                break
        else:
            A.append(word)
    return A

def getPossibleWords(X,C,Cp,Xp):
    global Ewords
    Ewords = notWithWords(Ewords,X)
    Ewords = withWords(Ewords,C)
    for i in range(5):
        if Cp[i]!="":
            Ewords = getWords(Ewords,i,Cp[i])
        if Xp[i]!="":
            Ewords = getWordsNot(Ewords,i,Xp[i])
    print(Ewords)
def wordsToTry(X,C,Cp,Xp):
    all_words = X+C
def main():
    X = "grhcswu"
    C = "peat"
    Cp = ["","","e","a","t"]
    Xp = ["","","","",""]
    # Cp = [""]*5
    getPossibleWords(X,C,Cp,Xp)

    
