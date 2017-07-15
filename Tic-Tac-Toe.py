#Global Declarations
board = ['1','2','3','4','5','6','7','8','9']
first_player_no = None #random_player_starts_func(), #tic_tac_toe_func()
second_player_no = None #random_player_starts_func(), #tic_tac_toe_func()
start_game = None #start_game_func()
current_marker = None #current_player_func(), winner_player_func(), insert_input_func()
input = None #check_input_func(), insert_input_func()

#Input Functions
def start_game_func():
	global start_game
	if start_game == None:
		start_game = raw_input('Do you want to play Tic-Tac-Toe? [Yes/No]: ')
	else: 
		start_game == None
		start_game = raw_input('Do you want to play again? [Yes/No]: ')
	return start_game.lower() == 'yes'

def player_input_func():
		player_input = raw_input('Please choose a number to make a move: ')
		return player_input

#Processes Functions
def random_player_starts_func():
	import random
	global first_player_no
	global second_player_no
	import random
	first_player_no = random.randrange(1,3)
	if first_player_no == 1:
		second_player_no = 2
	else: 
		second_player_no = 1

def full_board_check_func():
	total_length = board.count('o') + board.count('x')
	return total_length

def display_board_func():
	print ''
	print ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2]
	print '---+---+---'
	print ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] 
	print '---+---+---'
	print ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8]
	print ''

def check_input_func():
	global input
	input = player_input_func()
	if input not in board: 
		print '\nInvalid move. \nNo alphabets or spaces allowed.'
		print 'Please choose between 1 to 9, which are not taken up.\n'
		check_input_func()
	elif 0 < int(input) < 10 and board[int(input)-1].isdigit():
		insert_input_func()

def insert_input_func():
	global current_marker
	global input
	if (9 - full_board_check_func()) %2 == 1 or full_board_check_func == 0:
		current_marker = 'o'
	else:
		current_marker = 'x'
	board[int(input)-1] = current_marker
	
def current_player_func():
	global current_marker
	if current_marker == 'o':
		current_player = second_player_no
	else: 
		current_player = first_player_no
	return current_player

def winner_player_func():
	global current_marker
	if current_marker == 'o':
		current_player = first_player_no
	else: 
		current_player = second_player_no
	return current_player

def win_check_func():
		if board[0] == board[1] == board[2] \
			or board[3] == board[4] == board[5] \
			or board[6] == board[7] == board[8] \
			or board[0] == board[3] == board[6] \
			or board[1] == board[4] == board[7] \
			or board[2] == board[5] == board[8] \
			or board[0] == board[4] == board[8] \
			or board[2] == board[4] == board[6]:
			return True

def reset_game_func():
	global board
	board = ['1','2','3','4','5','6','7','8','9']

#Overall Function
def tic_tac_toe_func():
	print 'Welcome to Tic-Tac-Toe!'
	while start_game_func() == True:
		random_player_starts_func()			
		print '\n\n\nPlayer {x} starts the game!'.format(x=first_player_no)
		display_board_func()
		print 'Player {x}: o ; Player {y}: x'.format(x=first_player_no,y=second_player_no)
		check_input_func()

		while full_board_check_func() != 9: 
			print '\n\n\nPlayer {x} to make a move.'.format(x=current_player_func())
			display_board_func()
			print '\nPlayer {x}: o ; Player {y}: x'.format(x=first_player_no,y=second_player_no)
			check_input_func()

			if win_check_func() == True:
				print '\n\n\nPlayer {x} has won the game!'.format(x=winner_player_func())
				display_board_func()
				reset_game_func()
				break
		else:
			print "\n\n\nDraw Game!"
			display_board_func()
			reset_game_func()

	else:
		print '\n\n\nGoodbye!'

tic_tac_toe_func()