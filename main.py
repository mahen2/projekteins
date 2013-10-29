import random
t = 0 # Anzahl Versuche.
l = [] # Richtig geratene Buchstaben.
w = [] # Falsch geratene Buchstaben.

#to do: checken, ob die eingabe länger als 1 buchstabe ist

def find_word():
	file = open("words.txt", "r")
	word_list = file.readlines()   # Erfragen, wie man den Zeilenumbrauch am Besten rausmacht.
	file.close()
	word = random.choice(word_list)
	return word


def begin_game():
	global t
	global l
	t = 0
	l = []
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
	i = 0
	if t == 11:
		restart()
	else:
		guess = raw_input("\n \n Your guess: ")
		if guess in word:
			t += 1
			l.append(guess)
			
			print "Good choice! Please continue..."
			
		else:
			t += 1
			if guess in w:
				print "Dummy, you already tried this one!"
			else:
				w.append(guess)
				print "No, wrong! Wrong letters:"
				print w
			quizmaster(word)


def restart():
	print "Whoops! You lose. So sorry."
	print "...but you can try again!"
	begin_game()
	

begin_game()
