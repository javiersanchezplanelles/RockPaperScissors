from random import randint

human    = 0
computer = 0
winning_score = 3

while human < winning_score and computer < winning_score:
	player1 = input('Enter your choice:').lower()
	if player1 == 'q':
		break

	machine = randint(1,4)

	if machine == 1:
		machine = 'rock'
	elif machine == 2:
		machine = 'paper'
	else:
		machine = 'scissors'

	if player1 == 'rock':
		if machine == 'rock':
			print('Machine chooses rock. Draw')
		if machine == 'scissors':
			print('Machine chooses scissors. Player 1 wins!')
			human += 1
		if machine == 'paper':
			print('Machine chooses paper. Machine wins!')
			computer += 1
	elif player1 == 'paper':
		if machine == 'rock':
			print('Machine chooses rock. Player 1 wins!')
			human += 1
		if machine == 'scissors':
			print('Machine chooses scissors. Machine wins!')
			computer += 1
		if machine == 'paper':
			print('Machine chooses paper. Draw')
	elif player1 == 'scissors':
		if machine == 'rock':
			print('Machine chooses rock. Machine wins!')
			computer += 1
		if machine == 'scissors':
			print('Machine chooses scissors. Draw')
		if machine == 'paper':
			print('Machine chooses paper. Player 1 wins!')
			human += 1
if human > computer:
	print('Human wins!')
elif computer > human:
	print('Computer wins!')
else: 
	print('No one wins!')