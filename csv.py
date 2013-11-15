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

import os
from HelperFunctions import *
os.system('cls' if os.name == 'nt' else 'clear')

#database =[
#        ["JP2", "ADS2", "AP3", "AF2", "CS1P", "Alg3", "CS1Q"], #courses
#        ["1","2","3","4","5"], # students
#        ]

def export():
    classes = getClasses(db)
    users = getUsers(db)
    try:
        choice = raw_input(">>Do you want to export a (1) course or a (2) student? ")
        if choice == "1":
            exportCourse(classes)
        elif choice == "2":
            exportStudent(users)
    except ValueError:
        print ">>Input not recognised, please try again"


def exportCourse(database):
    print ">>Enter course name from: "
    for i in range(0, len(database[0])):
        print ">>" +  str(i) + ". " + database[i]	
    course = raw_input("")
    try:
            courseNo = int(course)
    except ValueError:
        print ">>Input not recognised, please try again"
        exportCourse(classes)
        return()
    if (courseNo < 0) or (courseNo > len(database) -1):
        print ">>Input not recognised, please try again"
        exportCourse(classes)
        return
    print ">>YOU CHOSE COURSE " + database[courseNo]
    print "Export Succesful"

def exportStudent(database):
    for i in range(len(users)):
        print("{0}. {1}".format(users[i]))
        student = raw_input(">>Enter student's matric number: ")
        print student
        print database[1]
    while student not in database[1]:
        print ">>Input not recognised, please try again"
        student = raw_input(">>Enter student's matric number: ")
    print ">>YOU CHOSE STUDENT " + student  
    print "Export Succesful"


if __name__ == '__main__':
    course =""
    db = init_db()
    while True:
        export()
