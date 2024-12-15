import requests
import random

defaultLength=4

def getRandomWord(len):
    URL="https://random-word-api.vercel.app/api?words=1&length="+len
    response=requests.get(URL)
    if(response.status_code==200):
        word=response.json()
        return word[0]
    else:
        print("response code error")
        return None

def wordBlanking(word):
    newWord = ""
    for char in word:
        if random.random() < 0.5:  # Adjust probability as needed
            newWord += "_"
        else:
            newWord += char
    return newWord


wordlen=input("enter length of the word: ")
if(wordlen!=None):
    word=getRandomWord(wordlen)
else:
    word=getRandomWord(defaultLength)


print(wordBlanking(word))


while(True):
    userGuess=input("gues the word ")
    if(userGuess!=word and userGuess!='quit'):
        print("not a correct guess")
        print()
    elif(userGuess=="quit"):
        print("the word is: "+word)
        break
    else:
        print("you won!!")
        break
