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

# for x in range(5):
# 	print(deck.S[x][3])

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
	elif (deck.S[card_in_deck][pos]):
		return "[~XX~]"
	else:
		if(deck.S[card_in_deck][num] == 1):
			return("[~A"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 11):
			return("[~J"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 12):
			return("[~1"+deck.S[card_in_deck][suit]+"~]")
		elif(deck.S[card_in_deck][num] == 13):
			return("[~K"+deck.S[card_in_deck][suit]+"~]")
		else:
			return("[~"+str(deck.S[card_in_deck][num])+deck.S[card_in_deck][suit]+"~]")

def move_cards(stack1, stack2):	
	stack2.push(stack1.S[stack1.top])
	stack1.pop()

def switch_location(stack, new_location):
	stack.S[stack.top][2] = new_location

def switch_postion(stack):	#shows card
	stack.S[stack.top][3] = False

def compare_color(stack, card):
	# stack.S[stack.top].suit
	# card.suit
	if (card[suit] == stack.S[stack.top][suit]):
		return 1 #same suit for emptystack
	#allow to be placed in boardstack
	elif((card[suit] == 'C' or card[suit] == 'S') and (stack.S[stack.top][suit] == 'H' or stack.S[stack.top][suit] == 'D')):
		return 2
	elif((card[suit] == 'H' or card[suit] == 'D') and (stack.S[stack.top][suit] == 'C' or stack.S[stack.top][suit] == 'S')):
		return 2
	else:
		return False #unvalid move

#gameplay will be added		
for x in range(len(boardstack)):
	for c in range(x+1):
		move_cards(deck,boardstack[c])
		switch_location(boardstack[c], 2)

for x in range(7):
	switch_postion(boardstack[x])

print("Cards Left:", deck.top+1, "\n")
print("",display_card(deck, deck.top),end = ' ')

for x in reversed(range(3)):
	print(display_card(cardshownstack, x), end = '')
print("         ",end = ' ')

for x in range(len(emptystack)):
	print(display_card(emptystack[x], emptystack[x].top), end = ' ')
print("\n")

for x in range(len(boardstack)):
	print("              ", end = ' ')
	for i in (range(len(boardstack))):
		print(display_card(boardstack[x], i), end = ' ')
	print()

print()
