# -*- coding: utf-8 -*-

import random
import string

t = 0 #count attempts
l = [] #letters guessed right
w = [] #letters guesses wrong


def find_word(): #read text file and choose random word
    file = open("words.txt", "r")
    word_list = file.readlines()   
    file.close()
    word = random.choice(word_list)
    return word.strip()  #WHOOP WHOOP


def begin_game():  #starts game, resets all variables
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


def quizmaster(word): #moderates game and checks input
    global t
    global l
    global w
    if t == 11:
        restart()
    else:
        rguess = raw_input("\n \n Your guess: ")
        guess = rguess.upper()
        if len(guess) == 0:
            print "\n No! Wrong" "You have to type something...  \n"
        else:
            if guess in word:
                t += 1
                f = 11 - t
                if guess in l:
                    print "\n That's right, but you already guessed this one! ...you may try %i more times. \n" %f
                else:
                    l.append(guess) 
                    print "\n Good choice! Please continue... you may try %i more times. \n" %f
            else:
                
                if guess in w:
                    print "\n Dummy, you already tried this one! \n"
                
                elif guess not in string.ascii_uppercase:
                                    print "\n Dummy, only characters of the alphabet! (A-Z) And only ONE at a time :P \n"
                
                else:
                    t += 1
                    f = 11 - t
                    w.append(guess)
                    print "\n No, wrong! Wrong letters: %s" %w
                    print "You may try %i more times. \n" %f
        show_word(word)


def show_word(word): #show word with stars for unknown letters
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


def restart(): #restart game if player has lost
    print "Whoops! You lose. So sorry. \n ...but you can try again! \n \n"
    begin_game()


def you_win(): #restart game if player has won
    print "C-ON-G-R-A-T-U-L-A-T-I-O-N-S-!-!-! \n You won! Be happy! \n \n \n"
    begin_game


if __name__ == '__main__':
    begin_game()
