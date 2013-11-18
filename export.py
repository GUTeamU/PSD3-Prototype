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
from time import gmtime, strftime

STUDENT_FILE = "student_{0}_{1}.csv"
COURSE_FILE = "course_{0}_{1}.csv"

#database =[
#        ["JP2", "ADS2", "AP3", "AF2", "CS1P", "Alg3", "CS1Q"], #courses
#        ["1","2","3","4","5"], # students
#        ]

def export():
    try:
        choice = raw_input(">>Do you want to export a (1) course or a (2) student? ")
        if choice == "1":
            exportCourse()
        elif choice == "2":
            exportStudent()
    except ValueError:
        print ">>Input not recognised, please try again"


def exportCourse():
    listCourses()
    while True:
        try:
            course_id = raw_input(">>Enter course ID:")
            data = getCourseExportData(db, course_id)
            filename = COURSE_FILE.format(strftime("%Y-%m-%d", gmtime()), course_id)
            with open(filename, "w") as f:
                labels = getCourseSessionLabels(db, course_id)
                f.write("First name, Surname, ID number, Assignment: ")
                f.write(", Assignment: ".join(labels)+"\r")
                for row in data:
                    # take the first and last names from the full name
                    first = row[0].split(" ")[0]
                    last = row[0].split(" ")[-1]
                    row = [first] + row
                    row[1] = last

                    f.write(",".join(row) + "\r")
            print(">>Export Succesful: {0}".format(filename))
            return
        except ValueError:
            print ">>Input not recognised, please try again"
        except IOError:
            print(">>Error: couldn't save to file {0}".format(filename))

def exportStudent():
    data = getAllStudents(db)
    listStudens(data)

    while True:
        student = raw_input(">>Enter student's matric number: ")
        data = getStudentExportData(db, student)
        if not data:
            print("Student not found")
            continue

        listStudentData(data)

        filename = STUDENT_FILE.format(strftime("%Y-%m-%d", gmtime()), student)
        try:
            with open(filename, "w") as f:
                f.write("Course,ID number,Assignment,Mark\r")
                for row in data:
                    if row[3]:
                        mark = "present"
                    else:
                        mark = "absent"
                    f.write("{0},{1},{2},{3}\r".format(row[0], row[1], row[2], mark))

            print("Export Succesful: {0}".format(filename))
            return
        except IOError:
            print("Error: couldn't save to file {0}".format(filename))

def listCourses():
    print("-"*17)
    style = "| {0:<6} | {1:<4} |"
    print(style.format("Course", "ID"))
    print("-"*17)
    for row in getCourses(db):
        print(style.format(*row))
    print("-"*17)

def listStudentData(data):
    print("-"*43)
    style = "| {0:<6} | {1:<4} | {2:<13} | {3:<7} |"
    print(style.format("Course", "ID", "Assignment", "Mark"))
    print("-"*43)
    for row in data:
        print(style.format(*row))
    print("-"*43)

def listStudens(data):
    style = "| {1:<8} | {0:<35} |"
    print("-"*50)
    print(style.format("Name", "Matric"))
    print("-"*50)
    for row in data:
        print(style.format(*row))
    print("-"*50)


if __name__ == '__main__':
    db = init_db()
    while True:
        export()
