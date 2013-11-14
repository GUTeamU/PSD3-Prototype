#present the user with the option of exporting the whole course to CSV
# or a single student to CSV. Validate this input against syntax errors.

#>>>
#> Do you want to export a course or a student?
#>>> course
#> Enter Course:
#>>> JP2
#> Export Successful 

#>>>
#> Do you want to export a course or a student?
#>>> student
#> Enter Student's Matric Number:
#>>> Edvin
#> Student Number Not Recognised, Try Again:
#>>> 1102103
#> Export Successful

database = ["JP2", "ADS2", "AP3", "AF2", "CS1P", "Alg3", "CS1Q"]
sdatabase = ["test"]

def export():
	choice = raw_input(">>Do you want to export a (1) course or a (2) student? ")
	if choice == "1":
		exportCourse()
	elif choice == "2":
		exportStudent()
	else: 
		print ">>Input not recognised, please try again"
		export()

def exportStudent():
	student = raw_input(">>Enter student's matric number: ")
	while (student not in sdatabase):
		print ">>Input not recognised, please try again"
		student = raw_input(">>Enter student's matric number: ")
	# SEARCH FOR STUDENT

def exportCourse():
	print ">>Enter course name from: "
	for i in range(0, len(database)):
		print ">>" +  str(i) + ". " + database[i]	
	course = raw_input("")
	if course < 0: # or (course > len(database)): 
		print ">>Input not recognised, please try again"		
		exportCourse()
	print ">>YOU CHOSE COURSE " + database[int(course)]


export()
