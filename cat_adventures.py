def game_description():
	"""Prints some information about this game"""
	print "Imagine that you are a cat playing in a room."
	print "There are lots of places where you can play a bit."
	print "And you can choose where to play."
	print "So, lets go!"
	print "(press any key to continue)"

def menu():
	"""Shows main menu of this game"""
	visited_places = []
	score = 0

	while True:
		raw_input()
		print "Choose a place to go:"
		print "1. Bathroom."
		print "2. Kitchen."
		print "3. Balcony."
		print "4. Go get some sleep (Exit from the game)."
	
		choice = raw_input("> ")
		if not choice in ['1','2','3']:
			print "Choose one of available options!"
			print "(press any key to continue)"
			continue

		if choice in visited_places:
			print "You've already been there! Isn't it boring to play again in the same place?"
			print "(press any key to continue)"
			continue

		if choice == "1":
			visited_places.append(choice)
			score += bathroom()
			print "You've finished you adventures in a bath."
			print "Time to go play to another room."
			print "(press any key to continue)"
		elif choice == "2":
			visited_places.append(choice)
			score += kitchen()
			print "You've finished you adventures in a kitchen."
			print "Time to go play to another room."
			print "(press any key to continue)"
		elif choice == "3":
			visited_places.append(choice)
			score += balcony()
			print "You've finished your adventures in a balcony."
			print "Time to go play to another room."
			print "(press any key to continue)"
		elif choice == "4": 
			exit(0)	
		else: 
			print "Something really wired had happened. We should never reach this statement"
		if len(visited_places) == 3:
			evaluate_scores(score)
			exit(0)
	
def bathroom():
	"""Handles playing in bathroom"""
	print "You are now in the bathroom."
	print "Here you see a basin with a sand in it."
	print "What would you do?"
	print "1. Scrabble a sand and make a poo."
	print "2. Scatter a sand all around a bathroom."
	print "3. Take a nap inside a basin."
	
	choice = make_choice(3)
	if choice == "1":
		return 2
	elif choice == "2":
		return 0
	elif choice == "3":
		return 1
	else:
		print "make_choice(n) has returned", choice, "which should not happen" 
	
def kitchen():
	"""Playing in kitchen realization"""
	print "Here is the kitchen - a place"
	print "where all the food resids."
	print "You notice a plate of chicken"
	print "pieces which looks very tasty."
	print "What would you do?"

	print "1. Smash off the plate on the foor."
	print "2. Take a piece of tasty chicken."
	print "3. Start mewing and asking for a food."

	choice = make_choice(3)
	if choice == "1":
		return 0
	elif choice == "2":
		return 1
	elif choice == "3":
		return 2 
	else:
		print "make_choice(n) has returned", choice, "which should not happen" 
			
def balcony():
	"""Playing in balcony realization"""
	print "You are now entering a balcony."
	print "Here you see a lot of interesting"
	print "things. You start sneeking around"
	print "and suddenly notice a fly on the "
	print "wall. What would you do?"

	print "1. Trying to cach a fly breaking everithing around you."
	print "2. Watch on the fly and make one precise jump to cache it."
	print "3. Lay on the floor and lazily stare at the fly."
	
	choice = make_choice(3)
	if choice == "1":
		return 0
	elif choice == "2":
		return 2
	elif choice == "3":
		return 1
	else:
		print "make_choice(n) has returned", choice, "which should not happen" 

def evaluate_scores(n):
	"""Evaluates scores and print results"""
	print "Your score is ", n 
	print "So, I can say that you"
	if n in range(0,3):
		print "are a very nasty cat and"
		print "it is not very"
		print "funny to clean up all mess"
		print "after you, but your master"
		print "will never get bored for sure"
	elif n in range(3,6):
		print "are an active cat who doesn't"
		print "afraid of new challenges"
		print "but loyal to your masters"
	
	elif n in range(6,10):
		print "have too straight behavior"
		print "it is pleasent to your "
		print "masters, but is shamefully"
		print "for you as a cat."
	else:
		print "n equals to ", n, "and this should not happen for this game"

def make_choice(max):
	choice = raw_input("> ")
	if not int(choice) in range(1,max + 1):
		print "Please, choose an option from a list"
		return make_choice(max)
	return choice

game_description()
menu()
