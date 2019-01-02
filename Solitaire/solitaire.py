import random
from ds_stacks import Stack

#deckstack cardshownstack(3)               emptystack(s) emptystack(h) emptystack(c) emptystack(d)
#boardstack(1) boardstack(2) boardstack(3) boardstack(4) boardstack(5) boardstack(6) boardstack(7)

class card():
	def __init__(self, num, suit, location):
		self.suit = suit
		self.num = num
		self.location = location
		self.pos = False#shown
	
	def card_position(self, current):
		self.pos = current

	def card_location(self, new_location):
		self.location = new_location

suits = ["H", "S", "D", "C"]
#["heart", "spades", "diamonds", "clubs"]

#make the deck
deck = Stack() #position 0

#fill deck
for suit in suits:
	for j in range (13):
		deck.push(card(j + 1, suit, 0))

random.shuffle(deck.S) #literally shuffles it

emptystack = []#position 1
boardstack = []#position 2
cardshownstack = Stack()#display must be capped at 3 elements .. position 3

#lets fill all this arrays with stacks
for y in range(4):
	emptystack.append(Stack())

for y in range(7):
	boardstack.append(Stack())

#prints a card
def display_card(deck):
	if (deck.isEmpty() or deck.S[deck.top].pos == False):
		return "[~XX~]"
	else:
	#	print("|~",deck.S[deck.top].suit,"~|")
		if(deck.S[deck.top].num == 1) :
			# print("|-","A","-|")
			return("[~A"+deck.S[deck.top].suit+"~]")
		elif(deck.S[deck.top].num == 11) :
			return("[~J"+deck.S[deck.top].suit+"~]")
		elif(deck.S[deck.top].num == 12) :
			return("[~Q"+deck.S[deck.top].suit+"~]")
		elif(deck.S[deck.top].num == 13) :
			return("[~K"+deck.S[deck.top].suit+"~]")
		else:
			return("[~"+str(deck.S[deck.top].num)+deck.S[deck.top].suit+"~]")

#takes top card from stack 1 and pushes into stack 2
def move_cards(stack1, stack2):	
	stack2.push(stack1.S[stack1.top])
	stack1.pop()

def switch_location(stack, new_location):
	stack.S[stack.top].card_location(new_location)

def switch_postion(stack):	#shows card
	stack.S[stack.top].card_position(True)

#rules for stacks
def compare_color(stack, card):
	stack.S[stack.top].suit
	card.suit
	if (card.suit == stack.S[stack.top].suit):
		return 1 #same suit for emptystack
	#allow to be placed in boardstack
	elif((card.suit == "C" or card.suit == "S") and (stack.S[stack.top].suit == "H" or stack.S[stack.top].suit == "D")):
		return 2
	elif((card.suit == "H" or card.suit == "D") and (stack.S[stack.top].suit == "C" or stack.S[stack.top].suit == "S")):
		return 2
	else:
		return False #unvalid move

# Filling stacks
for x in range(len(boardstack)):
	for c in range(x+1):
		move_cards(deck,boardstack[c])
		switch_location(boardstack[c], 2)
	# print(boardstack[x].S[boardstack[x].top].pos)
	switch_postion(boardstack[x])#top card is shown
	print(boardstack[x].S[boardstack[x].top].pos,x)
	print("",display_card(boardstack[x]), end = ' ')
	# print(boardstack[x].S[boardstack[x].top].pos)

# first display
switch_postion(deck)
print("Cards Left:", deck.top+1)
print()
print(deck.S[deck.top].pos)
print("",display_card(deck),"                   ",display_card(emptystack[0]),display_card(emptystack[1]),display_card(emptystack[2]),display_card(emptystack[3]))

for x in range(len(boardstack)):
	print("",display_card(boardstack[x]), end = ' ')
	print(boardstack[x].S[boardstack[x].top].pos,x)

# b = random.randint(1,13)
# print(deck.S[b].pos,b)
# display_card(b,deck)
