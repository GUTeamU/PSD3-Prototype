from HelperFunctions import *

def sessions():
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
    option = raw_input("[Select a session]\n>>>")
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

def select_class():
    classes = getClasses(db)

    # List of available classes numbered 1...n 
    for i in range(len(classes)):
        print("{0}. {1}".format(i+1, classes[i][1]))

    try:
        choice = int(raw_input("[Select a class]\n>>>")) - 1
        print(">>>{0}".format(classes[choice][1]))
        select_session(classes[choice][0])
    except ValueError:
        print("Invalid choice")

def select_session(class_id):
    sessions = getSessions(db, class_id)

    # List of avialable sessions for selected class numbered 1...n
    for i in range(len(sessions)):
        print("{0}. {1} - {2}".format(i+1, sessions[i][1], sessions[i][2]))

    try:
        choice = int(raw_input("[Select a session]\n>>>")) -1
        print(sessions[choice][0])
    except ValueError:
        print("Invalid choice")

if __name__ == '__main__':
    course = ""
    db = init_db()
    while True:
        select_class()
