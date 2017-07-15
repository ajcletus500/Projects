'''def tic(play):
	print(play)
	print(lis)
	print(''	{}_|_{}_|_{}	
	{}_|_{}_|_{}	
	{} | {} | {}	''.format(box[0],box[1],box[2],box[3],box[4],box[5],box[6],box[7],box[8]))

global lis
lis=[chr(i) for i in range(ord('a'),ord('i')+1)]
temp=lis
box=['_','_','_','_','_','_','_','_','_']
print(box[8])

player=1
for n in range(9):
	play = input('Player%s: Select a box to play your turn: ' %player)

	if player==1 and 'a'<=play<='i' :
		if play in lis:
			box=['X' if x == play else '_' for x in lis]
			print('box is',box)
			temp=[None for x in temp if x != play]

			print('lis is',lis)
			tic(play)
		else:
			print("Available boxes are ",lis)
	elif player==2 and 'a'<=play<='i' :
		if play in lis:
			box=['O' if x == play else '_' for x in lis]
			print('box is',box)
			temp=[None for x in temp if x != play]

			print('lis is',lis)
			tic(play)
		else:
			print("Available boxes are ",lis)
	else:
		print('your input is out of range')
	if player==1:
		player=2
	else:
		player=1'''


def tic():
	#print(play)
	#print(lis)
	print('''	{}_|_{}_|_{}	
	{}_|_{}_|_{}	
	{} | {} | {}	'''.format(box[0],box[1],box[2],box[3],box[4],box[5],box[6],box[7],box[8]))

box=['_','_','_','_','_','_',' ',' ',' ']
tic()





def player1(p1):
	if p1 in lis:
		ind=lis.index(p1)
		box[ind]='X'
		#print(lis)
		tic()
	

def player2(p2):
	if p2 in lis:
		ind=lis.index(p2)
		box[ind]='0'
		print(lis)
		tic()

def win(p):
	if box[0]==box[1]==box[2] or box[3]==box[4]==box[5] or box[6]==box[7]==box[8] or box[4]==box[0]==box[8] or box[2]==box[4]==box[6] or box[6]==box[0]==box[3] or box[1]==box[7]==box[4] or box[2]==box[5]==box[8]:
		print('Winner',p)
		return True
	#elif i==8:
	#	print("Game Drawn")
	#	return  False


lis=[chr(i) for i in range(ord('a'),ord('i')+1)]
#box=lis

i=0
for x in range(0,5):
	p1=input('Player1: input box to place X:')
	player1(p1)
	if x==3 and win("Player1"):
		print('game over')
		break
	p2=input('Player2: input box to place O:')
	player2(p2)
	if x==3 and win("Player2"):
		print('game over')
		break
	i+=2
	if i==8:
		print('game draw')
		break