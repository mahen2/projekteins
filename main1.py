# -*- coding: utf-8 -*-

import random
import string


t = 0 # Anzahl Versuche.
l = [] # Richtig geratene Buchstaben.
w = [] # Falsch geratene Buchstaben.

#to do: checken, ob die eingabe länger als 1 Buchstabe ist
#to do: checken, ob nichts eingegeben wurde
#Bildschirm löschen: os.system("cls"), import os
#from time import sleep, sleep(2)
# .upper()

def find_word():
        file = open("words.txt", "r")
        word_list = file.readlines() # Erfragen, wie man den Zeilenumbrauch am Besten rausmacht.
        file.close()
        word = random.choice(word_list)
        return word.strip() #WHOOP WHOOP


def begin_game():
        global t
        global l
        global w
        t = 0
        l = []
        w = []
        word = find_word()
        print "Try to guess the word. You may try 11 times. \n"
        a = 0
        while a < len(word):
                print("*"),
                a += 1
        quizmaster(word)
        
def quizmaster(word):
        global t
        global l
        global w
        if t == 11:
                restart()
        else:
                rguess = raw_input("\n \n Your guess: ")
                guess = rguess.upper()
                if guess in word:
                        t += 1
                        f = 11 - t
                        l.append(guess)
                        print "\n Good choice! Please continue... you may try %i more times. \n" %f
                        
                else:
                        
                        if guess in w:
                                print "\n Dummy, you already tried this one! \n"

                        elif guess not in string.ascii_uppercase:
                                print "\n Dummy, only alphabetic characters! \n"
			

                        else: 
                                t += 1
                                f = 11 - t
                                w.append(guess)
                                print "\n No, wrong! Wrong letters: %s" %w
                                print "You may try %i more times. \n" %f
                show_word(word)




def show_word(word):
        global l
        i = 0
        c = []
        s = "*"
        while i < len(word):
                if word[i] in l:
                        c.append(word[i])
                        print (word[i]),
                else:
                        print(s),
                        c.append(s)
                i += 1
        print "\n"
        if s in c:
                quizmaster(word)
        else:
                you_win()
        
                

def restart():
        print "Whoops! You lose. So sorry."
        print "...but you can try again!"
        print "..."
        print "... \n"
        begin_game()
        
        
def you_win():
        print "C-ON-G-R-A-T-U-L-A-T-I-O-N-S-!-!-!"
        print "You won! Be happy!"
        print "..."
        print "... \n"
        begin_game
        
        

begin_game()
