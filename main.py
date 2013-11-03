# -*- coding: utf-8 -*-

import random
import string

t = 0 #Anzahl Versuche
l = [] #Richtig geratene Buchstaben
w = [] #Falsch geratene Buchstaben


def find_word(): 

#Die Funktion öffnet die words.txt, liest sie ein und speichert das Eingelesene in die Variable world_list .
#Danach wird die Textdatei geschlossen und der Variable word die importierte Funktion random.choice zugewiesen,
#welche ein zufälliges Wort aus der word_list aussucht. Mittels return word.strip() wird dann das Wort zwischengespeichert.

    file = open("words.txt", "r")
    word_list = file.readlines()   
    file.close()
    word = random.choice(word_list)
    return word.strip()  #WHOOP WHOOP


def begin_game(): 
    
#Die Funktion definiert wie das Spiel gestartet wird. Es werden globale Variablen festgelegt, t für die verbrauchten Versuche, l für die richtigen Buchstaben und w für die Falschen.
#Der Variable word wird das zufällige Wort der find_word Funktion zugewiesen und mithilfe der while Schleife werden * für die Hervorhebung des Spiels generiert,
#welche sich der Länge des zu ratenden Wortes anpassen.

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
    
#Die Funktion "importiert" die Variablen der begin_game() Funktion, um sie nicht neu definieren zu müssen.
#Zuerst wird abgefragt, ob alle 11 Versuche verbraucht sind, um daraufhin das Spiel neuzustarten.

    global t
    global l
    global w
    if t == 11:
        restart()
        
#Falls noch Versuche übrig sind, dann wird verlangt einen Buchstaben einzugeben. Der Variable guess wird der Buchstabe zugewiesen.
#Die if Schleife prüft ob der geratene Buchstabe im ausgesuchten Wort vorkommt.

    else:
        rguess = raw_input("\n \n Your guess: ")
        guess = rguess.upper()
        
#Falls die Eingabelänge 0 ist, kommt eine Fehlermeldung, das gleiche passiert auch falls der erratene Buchstabe schon einmal benutzt wurde.
#Falls der Buchstabe richtig ist, erhöht sich die Anzahl der verbrauchten Versuche t um 1 und wird den verbleibenden Versuchen f abgezogen.
#Die append Funktion fügt den Buchstaben aus guess den richtig geratenen Buchstaben l hinzu.

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

#Falls der falsche Buchstabe schon einmal eingegeben wurde, dann kommt folgende Fehlermeldung.                  

                if guess in w:
                    print "\n Dummy, you already tried this one! \n"

#Falls der Buchstabe nicht zum Alphabet gehört und länger als 1 Zeichen ist, dann kommt folgende Fehlermeldung.                
                
                elif guess not in string.ascii_uppercase:
                    print "\n Dummy, only characters of the alphabet! (A-Z) \n"

#Falls der geratene Buchstabe falsch ist, erhöht sich wieder die Anzahl der verbrauchten Versuche t um 1 und wird den verbleibenden Versuchen f abgezogen.
#Nur wird jetzt der Buchstabe der Liste der falsch geratenen Buchstaben hinzugefügt.

                else:
                    t += 1
                    f = 11 - t
                    w.append(guess)
                    print "\n No, wrong! Wrong letters: %s" %w
                    print "You may try %i more times. \n" %f
        show_word(word)


def show_word(word):

#Wenn show_word aufgerufen wird, gibt das Programm das zu erratene Wort aus. Die bisher nicht erratenen Buchstaben werden durch Sternchen ersetzt.
#Hierfür werden die Variablen i (Index), l (Liste mit erratenen korrekten Buchstaben), c (Liste mit den ausgegebenen Zeichen) und s (String "'*") benutzt.
#Die Funktion show_word geht der Länge (n) des Wortes nach jeden Index (0-n) durch und überprüft, ob sich an dieser Stelle ein Buchstabe befindet, welcher bereits vom Nutzer erraten wurde.
#Wenn ja, wird dieser ausgegeben. Wenn nicht, wird ein Sternchen an Stelle des Buchstaben ausgegeben. So wird dem Nutzer sein Fortschritt beim Erraten des Lösungswortes angezeigt.
#Nach jeder Runde wird i eins höher gesetzt, um den nächsten Buchstaben zu überprüfen. Zum Schluss wird mit Hilfe der Liste c überprüft, ob Sternchen ausgegeben wurden.
#Wenn ja, wird quizmaster(word) aufgerufen, wenn nicht, hat der Nutzer das Spiel gewonnen, da alle Buchstaben erraten wurden und die Funktion ruft you_win() auf.

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

#Neustart des Spiels, falls verloren
    print "Whoops! You lose. So sorry. \n ...but you can try again! \n \n"
    begin_game()


def you_win():

#Neustart des Spiels, falls gewonnen

    print "C-ON-G-R-A-T-U-L-A-T-I-O-N-S-!-!-! \n You won! Be happy! \n \n \n"
    begin_game


if __name__ == '__main__':
    begin_game()
