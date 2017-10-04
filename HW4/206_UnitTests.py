import random
import unittest

# SI 206 Fall 2017
# Homework 3 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time:
# People you worked with:Kayla Williams

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.
#if card created with rank 12,"Queen" rank
class CardTests(unittest.TestCase):
	def test1(self):
		queen= Card(rank=12)
		self.assertEqual(str(queen), "Queen of Diamonds", "Checking you can make a card with rank Queen")
#Rank 1, "Ace"
	def test2(self):
		ace= Card(rank=1)
		self.assertEqual(str(ace), "Ace of Diamonds")
#Card instance with rank 3
	def test3(self):
		card3= Card(0,3)
		self.assertEqual(card3.rank, 3, "Rank of 3")
#Suit 1, suit is Clubs
	def test_4(self):
		card4= Card(1,2)
		self.assertEqual(card4.suit, "Clubs")
#Suit 2, suit is Hearts
	def test_5(self):
		card5= Card(suit=2)
		self.assertEqual(str(card5), "2 of Hearts")
#Test that if you create a card instance, it will have access to a
#variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	def test_cardInstance(self):
		cards = Card()
		self.assertEqual(cards.suit_names,["Diamonds","Clubs","Hearts","Spades"])
#if you invoke __str__ method instance that is created with suit=2
#rank=7, it returns the string '7 of hearts'
	def test7(self):
		card7= Card(2,7)
		self.assertEqual(str(card7), "7 of Hearts")
#deck instance w 52 cards
	def test8(self):
		cards1= Deck()
		self.assertEqual(len(cards1.cards), 52)
#pop_card instance returns card instance
	def test9(self):
		d=Deck()
		ci= Card()
		self.assertEqual(type(d.pop_card()),type(ci))
#test play_war_game for 3 element tuples
	def test10(self):
		w= play_war_game()
		self.assertEqual(len(w),3)
		self.assertEqual(type(w[0]), str)
#2 additional tests
#Test that suit is Spades and rank gives us 2
	def test11_1(self):
		card11= Card(3,2)
		self.assertEqual(str(card11), "2 of Spades")
#Test to find faces along with their suit number
	def test11_2(self):
		c11=Card()
		self.assertEqual(c11.faces,{1:"Ace",11:"Jack",12:"Queen",13:"King"})
#############
## The following is a line to run all of the tests you include:
unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
