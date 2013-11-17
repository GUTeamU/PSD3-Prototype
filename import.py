from HelperFunctions import *
import sys

def show_session(session_id):
    while True:
        print("list -- List all students that are registered to attend")
        print("mark [ present | absent ] matric ...")
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
            elif command == "mark":
                mark_students(session_id, choice[1])
            elif command == "import":
                import_attendance(session_id, choice[1])
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

def import_attendance(session_id, arg):
    try:
        lines = [line.rstrip('\n').split(",") for line in open(arg)]
        updateAttendance(db, session_id, lines)
    except IOError:
        print("File not found: {0}".format(arg))

def mark_students(session_id, arg):
    command = arg.split()
    if len(command) < 2:
        print("Not enough arguments")
        return

    if command[0] == "present":
        markStudents(db, session_id, 1, command[1:])
    elif command[0] == "absent":
        markStudents(db, session_id, 0, command[1:])
    else:
        print("Unknown command: mark {0}".format(command[0]))

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
            if choice == "quit":
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
