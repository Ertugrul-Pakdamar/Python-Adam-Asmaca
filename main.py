from asyncio.windows_events import NULL
from hashlib import new
import os
from os import times_result
from random import Random, randint, random

fh = open('wordlist.txt', 'a')

gameOpen = 1
newWord = ""

def oynanıs(selectedWord, wordLenght, can):
    
    gameStart = 1
    tireler = "_ "
    x = ""
    #print(selectedWord)
    print(tireler * wordLenght)
    
    while gameStart == 1:
        deneme = input("\n")
        
        if len(deneme) == wordLenght:
            
            if deneme in selectedWord:
                print("Word Is: %s" % selectedWord.upper())
                print("----WIN----\n")
                gameStart = 0
                
        elif deneme in selectedWord:
            x = selectedWord.index(deneme)
            x += 1
            print(x)
            
        else:
            can -= 1
            print("Wrong Word Health: %d" % can)
        
        if can <= 0:
            print("----Game Over----\n")
            print("Word Is: %s" % selectedWord)
            gameStart = 0

while(gameOpen == 1):
    adminmode = "off"
    tercihint = 0
    n = 0
    
    print("-----Kelime Tahmin Oyunu-----")
    print("  Ertuğrul Pakdamar")
    print(" Yazılım Geliştiricisi")
    print("Game-1")
    print("Exit-2")
    print("Not: Oyundaki Kelimeler İngilizcedir")
    tercihint = input("Tercih: ")
    
    if tercihint == "1":
        fh = open("wordlist.txt","r+",encoding="utf-8")
        lines = fh.readlines()
        linesLenght = len(lines)
        linesLenght -= 1
        wordLenght = 0
        selectedWord = (lines[randint(1, linesLenght)])
        wordLenght = len(selectedWord) - 2
        can = wordLenght - 1
        oynanıs(selectedWord, wordLenght, can)
    
    elif tercihint == ";adminmode on":
        
        fh = open("wordlist.txt","r+",encoding="utf-8")
        
        adminlines = fh.readlines()
        print(adminlines)
        
        adminmode = "on"
        while adminmode == "on":    
            newWord = input("Input New Words: ")
            
            if newWord == "bye":
                adminmode = "off"
            
            else:
                fh.write('%s \n' % newWord)
        
    elif tercihint == "2":
        print("Please Come Back Bye :)")
        gameOpen = 0
