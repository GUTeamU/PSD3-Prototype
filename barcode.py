def sessions():
	print "\n"
	print"= Old ======="
	print"1. 30/09/2013"
	print"2. 07/10/2013"
	print"3. 14/10/2013" 
	print"4. 21/10/2013"
	print"5. 28/10/2013" 
	print"6. 04/11/2013"
	print"= Last =======" 
	print"7. 11/11/2013"
	print"= Upcoming ==="
	print"8. 18/11/2013"
	print"9. 25/11/2013"
	print"\n"
	option = raw_input("Which date would you like to view?: ")
	return option
	
def give_sessions():

	choice2 = sessions()
			
	if choice2 == "1":
		print course,"lab 30/09/2013"
		commands()
	elif choice2 == "2":
		print course,"lab 07/10/2013"
		commands()
	elif choice2 == "3":
		print course,"lab 21/10/2013"
		commands()
	elif choice2 == "4":
		print course,"lab 28/102013"
		commands()
	else:
		print"invalid option"
	choice = give_sessions



def commands():
	print"list -- List all students that are registered to attend"
	print"mark [+ | -]matric -- Mark students presence or absence"
	print"import filename -- Import attendance data from a CSV file"
	print"\n"
	option = raw_input("which option would you like to choose?: ")
	return option

def choose_command():
	choice = commands()
	
	if choice == "list":
		print "list of all students \n, student\n"
	elif choice == "import":
		print "SDFSDFSDFSDF"


def print_options():

	print "1. PSD3 lab (Recurring)"
	print "2. ALG3 lab (Recurring)"
	print "3. AP3  lab (Recurring)"
	print "4. PL3  lab (Recurring)"
	print "5. Quit"
	print ("\n\n")
	
	option = raw_input("Which option would you like to choose?: ")
	return option
	
def give_option():
	global course
	choice = print_options()
			
	if choice == "1":
		print "PSD3 lab sessions"
		course = "PSD"
		give_sessions()
	elif choice == "2":
		print "ALG3 lab sessions"
		course = "ALG3"
		give_sessions()
	elif choice == "3":
		print "AP3 lab sessions"
		course = "AP3"
		give_sessions()
	elif choice == "4":
		print "PL3 lab sessions"
		course = PL3
		give_sessions()
	else:
		print"invalid option"
	choice = print_options()
		
def login():
	option = str.lower(raw_input("hit y to begin: "))
	if option == "y":
		choice = give_option()



login()
