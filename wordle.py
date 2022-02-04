import nltk
from nltk.corpus import words
import tkinter as tk
AllWords = [word.lower() for word in words.words() if len(word)==5]

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
    global AllWords
    Ewords = notWithWords(AllWords,X)
    Ewords = withWords(Ewords,C)
    for i in range(5):
        if Cp[i]!="":
            Ewords = getWords(Ewords,i,Cp[i])
        if Xp[i]!="":
            Ewords = getWordsNot(Ewords,i,Xp[i])
    return list(set(Ewords))
def wordsToTry(X,C,Cp,Xp):
    all_words = X+C
def main():
    X = "grhcswu"
    C = "peat"
    Cp = ["","","e","a","t"]
    Xp = ["","","","",""]
    # Cp = [""]*5
    getPossibleWords(X,C,Cp,Xp)
class UserInterface:
    def __init__(self):
        self.N = 5
        self.allPossibleWords = []
        self.bestGuesses = []
        self.selected = [" "]*self.N
        self.dropDown = [" "]*self.N
        self.notSure = [" "]*self.N
        self.entry = [" "]*self.N
        self.notPresent = ""
        self.window = tk.Tk()
        self.window.title("Wordle Helper")
        self.window.geometry("480x480")
    def showPossibleWords(self):
        print("Hi")
        CP = []
        XP = []
        for i in self.selected:
            word = i.get().strip().lower()
            if len(word) == 1:
                CP.append(word)
            else:
                CP.append("")
        for i in self.notSure:
            word = i.get().strip().lower()
            if len(word)>0:
                XP.append(word)
            else:
                XP.append("")
        C = "".join(CP) + "".join(XP)
        X = []
        if self.notPresent.get() is not None:
            X = self.notPresent.get().strip().lower()
        wordList = getPossibleWords(X,C,CP,XP)
        allWords = tk.Text(self.window,width=7)
        for i,word in enumerate(wordList):
            allWords.insert(tk.END, f"{word}\n")
        allWords.grid(row = 7, column = 0, rowspan=len(wordList)+1)
        
    def showWordsTobeEntered(self):
        print("Bo")
        self.allPossibleWords = []
        self.bestGuesses =  ["Words"]

    def GUI(self):
        options = ["Select"] + [f"  {chr(ord('A')+i)}  " for i in range(26)]
        l1 = tk.Label(self.window, text = "Enter words with positions certained")
        l1.grid(row=0, column = 1, sticky = tk.W, pady = 2, columnspan=5)
        for i in range(self.N):
            self.selected[i] = tk.StringVar()
            self.selected[i].set("Select")
            self.dropDown[i] = tk.OptionMenu(self.window,self.selected[i],*options)
            self.dropDown[i].grid(row=1, column = i, sticky = tk.W, pady = 2)
        l1 = tk.Label(self.window, text = "Enter words present, but not in this position")
        l1.grid(row=2, column = 1, sticky = tk.W, pady = 2, columnspan=5)
        for i in range(5):
            self.notSure[i] = tk.StringVar()
            self.notSure[i].set(" ")
            self.entry[i] = tk.Entry(self.window, textvariable=self.notSure[i], width=5)
            self.entry[i].grid(row = 3, column = i, sticky = tk.W, pady = 2)
        l2 = tk.Label(self.window, text = "Enter words which are not present")
        l2.grid(row=5, column = 0, sticky = tk.W, pady = 2, columnspan=3)
        self.notPresent = tk.StringVar()
        self.notPresent.set(" ")
        notPresentEntry = tk.Entry(self.window, textvariable=self.notPresent)
        notPresentEntry.grid(row = 5, column = 3, sticky = tk.W, pady = 2, columnspan=5)
        submit = tk.Button(self.window, text = "Show Possible Words", command = self.showPossibleWords)
        submit.grid(row=6, column = 0, sticky =tk.W, pady = 2, columnspan=3)

        submit1 = tk.Button(self.window, text = "Show Word to Guess", command = self.showWordsTobeEntered)
        submit1.grid(row=6, column = 3, sticky =tk.W, pady = 2, columnspan=3)
        
        self.window.mainloop()
UserInterface().GUI()

    
