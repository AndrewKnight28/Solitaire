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
def display_card(deck):
	num = 0
	suit = 1
	pos = 3#so i don't have to change everything
	if (deck.isEmpty()):
		return "[    ]"
	elif (deck.S[deck.top][pos]):
		return "[~XX~]"
	else:
		if(deck.S[deck.top][num] == 1):
			return("[~A"+deck.S[deck.top][suit]+"~]")
		elif(deck.S[deck.top][num] == 11):
			return("[~J"+deck.S[deck.top][suit]+"~]")
		elif(deck.S[deck.top][num] == 12):
			return("[~1"+deck.S[deck.top][suit]+"~]")
		elif(deck.S[deck.top][num] == 13):
			return("[~K"+deck.S[deck.top][suit]+"~]")
		else:
			return("[~"+str(deck.S[deck.top][num])+deck.S[deck.top][suit]+"~]")

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
for x in range(len(boardstack)):
	for c in range(x+1):
		move_cards(deck,boardstack[c])
		switch_location(boardstack[c], 2)

switch_postion(deck)

for x in range(7):
	switch_postion(boardstack[x])

print("Cards Left:", deck.top+1, "\n")
# print(deck.S[deck.top].pos)
print("",display_card(deck),"                   ",display_card(emptystack[0]),display_card(emptystack[1]),display_card(emptystack[2]),display_card(emptystack[3]),"\n")

print("        ", end = ' ')

	for x in range(len(boardstack)):
		print(display_card(boardstack[x]), end = ' ')

print()import random 
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
def display_card(deck):
	num = 0
	suit = 1
	pos = 3#so i don't have to change everything
	if (deck.isEmpty()):
		return "[    ]"
	elif (deck.S[deck.top][pos]):
		return "[~XX~]"
	else:
		if(deck.S[deck.top][num] == 1):
			return("[~A"+deck.S[deck.top][suit]+"~]")
		elif(deck.S[deck.top][num] == 11):
			return("[~J"+deck.S[deck.top][suit]+"~]")
		elif(deck.S[deck.top][num] == 12):
			return("[~1"+deck.S[deck.top][suit]+"~]")
		elif(deck.S[deck.top][num] == 13):
			return("[~K"+deck.S[deck.top][suit]+"~]")
		else:
			return("[~"+str(deck.S[deck.top][num])+deck.S[deck.top][suit]+"~]")

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
for x in range(len(boardstack)):
	for c in range(x+1):
		move_cards(deck,boardstack[c])
		switch_location(boardstack[c], 2)

switch_postion(deck)

for x in range(7):
	switch_postion(boardstack[x])

print("Cards Left:", deck.top+1, "\n")
# print(deck.S[deck.top].pos)
print("",display_card(deck),"                   ",display_card(emptystack[0]),display_card(emptystack[1]),display_card(emptystack[2]),display_card(emptystack[3]),"\n")

print("        ", end = ' ')

	for x in range(len(boardstack)):
		print(display_card(boardstack[x]), end = ' ')

print()
