import random 
from ds_stacks import Stack

#deckstack cardshownstack(3)               emptystack(s) emptystack(h) emptystack(c) emptystack(d)
#boardstack(1) boardstack(2) boardstack(3) boardstack(4) boardstack(5) boardstack(6) boardstack(7)

#card = [num, suit, location, postion]

suits = ['H', 'S', 'D', 'C']
deck = Stack() #position 0

#fill deck
for suit in suits:
	for i in range(13):
		deck.push([(i + 1), suit, 0, True])

random.shuffle(deck.S) #literally shuffles it

emptystack = []#position 1
boardstack = []#position 2
cardshownstack = Stack()#display must be capped at 3 elements .. position 3

#lets fill all this arrays with stacks
for y in range(4):
	emptystack.append(Stack())

for y in range(7):
	boardstack.append(Stack())

#prints top card (REMASTERED)
def display_card(deck, card_in_deck):
	num = 0
	suit = 1
	pos = 3#so i don't have to change everything
	
	if (deck.isEmpty()):
		return "[    ]"
	
	if (deck.S[card_in_deck][pos]):
		return "[~  ~]"
	else:
		if(deck.S[card_in_deck][num] == 1):
			return("[~A"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 10):
			return("[~X"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 11):
			return("[~J"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 12):
			return("[~1"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 13):
			return("[~K"+deck.S[card_in_deck][suit]+"~]")
		else:
			return("[~"+str(deck.S[card_in_deck][num])+deck.S[card_in_deck][suit]+"~]")

def move_cards(stack1, stack2):	#source destiantion
	stack2.push(stack1.S[stack1.top])
	stack1.pop()
	if(stack1.S[stack1.top][2] != 0):
		switch_postion(stack1)
		

def switch_location(stack, new_location):
	stack.S[stack.top][2] = new_location

def switch_postion(stack):	#shows card
	stack.S[stack.top][3] = False

def compare_color(stack, card):
	suit = 1
	if (stack.isEmpty() or card[suit] == stack.S[stack.top][suit]):
		return 1 #same suit for emptystack
	#allow to be placed in boardstack
	elif((card[suit] == 'C' or card[suit] == 'S') and (stack.S[stack.top][suit] == 'H' or stack.S[stack.top][suit] == 'D')):
		return 2
	elif((card[suit] == 'H' or card[suit] == 'D') and (stack.S[stack.top][suit] == 'C' or stack.S[stack.top][suit] == 'S')):
		return 2
	else:
		return False #unvalid move

def check_location(stack1):#detination
	location = 2
	if(stack1.isEmpty() or stack1.S[stack1.top][location] == 1):
		return 1#to empty
	
	elif(stack1.isEmpty() or stack1.S[stack1.top][location] == 2 ):
		return 2 #to board 
	else:
		return False #unvalid move (cannot be moved to deck or shown)
		
for x in range(len(boardstack)):
	for c in reversed(range(x + 1)):
		move_cards(deck,boardstack[x])
		switch_location(boardstack[x], 2)

for x in range(7):
	switch_postion(boardstack[x])

menu = {'D':deck, 'S':cardshownstack, 'A1':emptystack[0], 'A2':emptystack[1], 'A3':emptystack[2], 'A4':emptystack[3], '1':boardstack[0], '2':boardstack[1], '3':boardstack[2], '4':boardstack[3], '5':boardstack[4], '6':boardstack[5], '7':boardstack[6]}


def show_rules(option):
	print("Welcome to this solitaire game.")
	print("how to play:")
	print("1.Choose a stack to pick a card or chose \'D\' to reveal. ")
	print("2.Choose a stack to place the card. ")
	print("3.You cannot place cards in Deck and the other rules from regular solitaire game.")

print("SOLITAIRE")
#DISPLAY
print("Cards Left:", deck.top + 1, "\n")
print("    D                    S            A1     A2     A3     A4")
print("",display_card(deck, deck.top), end = '   ')
for x in reversed(range(3)):
	try:
		print(display_card(cardshownstack, cardshownstack.top - x), end = '')
	except IndexError :
		print("[    ]", end = ' ')
	
print("        ",end = '')
for x in range(len(emptystack)):
	print(display_card(emptystack[x], emptystack[x].top), end = ' ')
print("\n")
print("                  1      2      3      4      5      6      7")
for x in range(len(boardstack)):
	print("              ", end = ' ')
	for i in range(len(boardstack)):
		try:
			print(display_card(boardstack[i], x), end = ' ')
		except IndexError :
			print("      ", end = ' ')
	print()
print()

op = True
while op: 
	print("Choose a stack to pick a card or chose \'D\' to reveal: ")
	f_input = input()#toupper	
	if(f_input == 'D'):
		for i in range(3):
			move_cards(deck, cardshownstack)
			switch_postion(cardshownstack)
			#it stops when deck is empty (will be fixed)
	else:
		print("Choose a stack to place the card : ")
		s_input = input()#toupper

		while (s_input == 'D'):
			print("Cannot be placed in Deck! : ")
			s_input = input()
		#must do different rules for each stack
		if(check_location(menu[s_input]) ==  compare_color(menu[s_input], menu[f_input].S[menu[f_input].top])):
			move_cards(menu[f_input], menu[s_input])
			switch_location(menu[s_input], check_location(menu[s_input]))
		else:
			print("Unvalid Move!")

	#DISPLAY
	print("Cards Left:", deck.top + 1, "\n")
	print("    D                    S            A1     A2     A3     A4")
	print("",display_card(deck, deck.top), end = '   ')

	for x in reversed(range(3)):
		try:
			print(display_card(cardshownstack, cardshownstack.top - x), end = '')
		except IndexError :
			print("[    ]", end = ' ')
		
	print("        ",end = '')

	for x in range(len(emptystack)):
		print(display_card(emptystack[x], emptystack[x].top), end = ' ')
	print("\n")

	print("                  1      2      3      4      5      6      7")
	for x in range(len(boardstack) + 2):
		print("              ", end = ' ')
		for i in range(len(boardstack)):
			try:
				print(display_card(boardstack[i], x), end = ' ')
			except IndexError :
				print("      ", end = ' ')
		print()

	print()
