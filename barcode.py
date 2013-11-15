from HelperFunctions import *
import sys

def show_session(session_id):
    while True:
        print("list -- List all students that are registered to attend")
        print("mark [ present | abset ] matric ...")
        print("import filename -- Import attendance data from a CSV file")
        print("quit -- exit the program")
        print("back -- return to the session list")
        try:
            choice = raw_input(">>>").split(None, 1)
            command = choice[0]
            if command == "quit":
                sys.exit()
            elif command == "back":
                return
            elif command == "list":
                list_students(session_id)
            else:
                print(choice)
        except IndexError:
            print("Invalid command")

def list_students(session_id):
    for s in getStudents(db, session_id):
        sign = "-"
        if s[2]:
            sign = "+"
        print("[{0}] {1} {2}".format(sign, s[1], s[0]))

def select_class():
    classes = getClasses(db)

    # List of available classes numbered 1...n 
    for i in range(len(classes)):
        print("{0}. {1}".format(i+1, classes[i][1]))
    print("quit -- exit the program")
    try:
        choice = raw_input("[Select a class]\n>>>")
        if choice == "quit":
            sys.exit(0)
        choice = int(choice) - 1
        print(">>>{0}".format(classes[choice][1]))
        select_session(classes[choice][0])
    except ValueError:
        print("Invalid choice")

def select_session(class_id):
    while True:
        sessions = getSessions(db, class_id)

        # List of avialable sessions for selected class numbered 1...n
        for i in range(len(sessions)):
            print("{0}. {1} - {2}".format(i+1, sessions[i][1], sessions[i][2]))
        print("back -- return to the class list")
        print("quit -- exit the program")

        try:
            choice = raw_input("[Select a session]\n>>>")
            if choice == "quite":
                sys.exit(0)
            elif choice == "back":
                return
            choice = int(choice) - 1
            print(">>>{0} - {1}".format(sessions[choice][1], sessions[choice][2]))
            show_session(sessions[choice][0])
        except ValueError:
            print("Invalid choice")

if __name__ == '__main__':
    course = ""
    db = init_db()
    while True:
        select_class()
