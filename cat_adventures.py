def game_description():
	"""Prints some information about this game"""
	print "Imagine that you are a cat playing in a room."
	print "There are lots of places where you can play a bit."
	print "And you can choose where to play."
	print "So, lets go!"

def menu():
	print "Choose a place to go:"
	print "1. Bathroom."
	print "2. Kitchen."
	print "3. Balcony."
	print "4. Go get some sleep (Exit from the game)."

	while True:
		choice = raw_input("> ")
		if choice == "1":
			bathroom()
		elif choice == "2":
			kitchen()
		elif choice == "3":
			balcony()
		else: 
			print "Choose one of available options"
