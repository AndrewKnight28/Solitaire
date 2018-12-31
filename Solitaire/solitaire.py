import random
from ds_stacks import Stack

#deckstack cardshownstack(3)               emptystack(s) emptystack(h) emptystack(c) emptystack(d)
#boardstack(1) boardstack(2) boardstack(3) boardstack(4) boardstack(5) boardstack(6) boardstack(7)

class card():
	def __init__(self, num,suit, pos):
		self.suit = suit
		self.pos = pos
		self.num = num

suits = ["H", "S", "C", "D"]
#["heart", "spades", "clubs", "diamonds"]

#make the deck
deck = Stack() #position 0

#fill deck
for i in range(0, 4):
	for j in range (0, 13):
		deck.push(card(j + 1, suits[i], 0))

random.shuffle(deck.S) #literally shuffles it

emptystack = []
boardstack = []
cardshownstack = Stack()

#prints a card
def display_card(x, deck):
	print("|~",deck[x].suit,"~|")
	if(deck[x].num == 1) :
		print("|-","A","-|")
	elif(deck[x].num == 11) :
		print("|-","J","-|")
	elif(deck[x].num == 12) :
		print("|-","Q","-|")
	elif(deck[x].num == 13) :
		print("|-","K","-|")
	else:
		print("|-",deck[x].num,"-|")
	print("|~",deck[x].suit,"~|")	
	print()
