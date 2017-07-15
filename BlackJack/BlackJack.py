import random

class Deck:

	max=52
	def __init__(self,decks):
		self.decks=decks
		Deck.max=52*decks	
		return
		

	def set_deck(self): #Build deck
		values = [v for v in range(2, 11)] + "J Q K A".split()
		values=values * self.decks
		suits = "Diamonds Clubs Hearts Spades".split()
		deck_of_cards = ["%s of %s" % (v, s) for v in values for s in suits]
		a=random.shuffle(deck_of_cards)
		return(deck_of_cards)
		

	def pick_card(self,de): #Pick a card
		#print("len de", len(de))
		a = random.randint(0,len(de)-1)
		#print("a=", a)
		return  de[a]

	def cal_total(self,card,total,hand): #Calculate total
		print("im in")
		face=[i[0:2].strip() for i in hand]
		face.sort()
		#print('face is',face)
		total_new=0
		while len(face)!=0 and face[0].isdigit():
			total_new+=int(face[0])
			del face[0]
			#print(face,total_new)
		face.sort(reverse=True)
		count=face.count('A')
		while len(face)!=0:
			if face[0]=='K' or face[0]=='Q' or face[0]=='J':
				total_new+=10
				del face[0]
			elif total_new<=10 and face[0]=='A':
				total_new+=11
				del face[0]
			elif total_new>10 and face[0]=='A':
				total_new+=1
				del face[0]
			

		#'''if card[0]=='K' or card[0]=='Q' or card[0]=='J' or card[0:2]=='10':
		#	total+=10
		#elif card[0]=='A' and (total+11) > 21 :
		#	total+=1
		#elif card[0]=='A':
		#	total+=11
		#else:
		#	total+= int(card[0])
		return total_new
		
	def check_total(self,total_p1,total_d):
		if total_p1 == 21:
			return 'Player wins the game'
		elif total_p1 > 21 :
			return 'Player lost'
		elif total_d <= 21 and total_d > total_p1 :
			print()
			return 'Player lost. You lost $ ' + str( tabs['Player1'])
		elif total_d < 21 and total_d < total_p1 :
			print()
			return "Player wins. You won $ " + str( tabs['Player1'])
		elif total_d > 21 :
			return "Player wins. You won $ " + str( tabs['Player1'])
		elif total_d==total_p1 :
			return  "Its a draw"

	
global d, deck, total_p1,total_d,playercards,dealercards,hand,tabs


def reset():
	global d, deck, total_p1,total_d,playercards,dealercards,hand,tabs
	d=Deck(3)
	deck=d.set_deck()
	total_p1=0
	total_d=0
	playercards=[]
	dealercards=[]
	hand=[]
	tabs={}

def game_play(hand,totalval):
	card=d.pick_card(deck)
	hand.append(card)
	total_value=d.cal_total(card,totalval,hand)
	
	deck.remove(card)
	return card, total_value, hand

#print(len(deck))


#Round1
#Player
def ini_round(players):
	global playercards,total_d, total_p1, dealercards
	for i in range(0,int(players)):
		card, total_p1, playercards= game_play(playercards,total_p1)
		print('Player'+str(i+1)+' this is your first card: '+ str(card) + ' and your current total is :', total_p1)

	#Dealer
	card, total_d, dealercards= game_play(dealercards,total_d)
	print('''this is the Dealer's first card: ''' + str(card) + " and the dealer's total is: ", total_d)

	for j in range(0,int(players)):
		#PlayerRound2
		card, total_p1, playercards= game_play(playercards,total_p1)
		print('Player' + str(0+1) +' this is your second card: '+ str(card) + ' and your current total is :', total_p1)
	if total_p1==21:
		print(d.check_total(total_p1,total_d))

def bets(players):
	global bet, tabs
	for i in range(0,int(players)):
		bet=int(input('Player' +str(players)+' how much would you like to bet: '))
		tabs['Player'+str(players)]=bet
		print(tabs)



def game_on():
	#players=input('How many players are playing: ')
	global playercards,total_d, total_p1, dealercards
	players=1
	bets(players)
	ini_round(players)
	if total_p1 !=21 :
		inm=input('Enter 1 to Hit or 2 to Stand: ')

	#PlayerLoop
	if total_p1<21:
		for i in range(0,int(players)):
			while inm.lower()=='1' and total_p1 < 22:
	
				card, total_p1, playercards= game_play(playercards,total_p1)
				print('this is your new card: '+ str(card) + ' and your current total is :', total_p1)
	
				#print(playercards)
				if total_p1 < 21:
					inm=input('Enter 1 to Hit or 2 to Stand: ')
				elif total_p1 == 21:
					print(d.check_total(total_p1,total_d))
					print('you won $', tabs['Player1']*1.5)
					break
				else:
					print(d.check_total(total_p1,total_d))
					print('you lost$', tabs['Player1'])

					break


	#DealerLoop
	while inm =='2' and total_d<17:
		card, total_d, dealercards= game_play(dealercards,total_d)
		print("\nthis is the Dealer's card: " + str(card) + " and the dealer's total is: ", total_d)
		if total_d > 21:
			print(d.check_total(total_p1,total_d))
			#print('Player won $', tabs['Player1'])

		elif total_d >= 17:
			print(d.check_total(total_p1,total_d))


i='yes'
while i=='yes':
	i=input('If you want to play type Yes else type No: ').lower()

	if i == 'yes':
		reset()
		game_on()
	else:
		print('Game over')


	