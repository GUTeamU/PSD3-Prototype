from HelperFunctions import *

# Get user login

# Import the sessions
# Present the user with the sessions
db = init_db()

getClasses(db)
createClass(db, "PSD3")
createClass(db, "Algs3")
getClasses(db)

insertSession(db, 1, "14/11/2013 3:00", "14/11/2013 4:00", 10)
insertSession(db, 1, "14/11/2013 5:00", "14/11/2013 6:00", 10)
insertSession(db, 2, "14/11/2013 3:00", "14/11/2013 4:00", 15)
insertSession(db, 3, "14/11/2013 3:00", "14/11/2013 4:00", 50)

getSessions(db, 1)
userJoinSession(db, 1, 12)
getSessions(db, 1)

getUsers(db)
createUser(db, "1003492c", "123456", "122132132142")
getUsers(db)
loginUser(db, "1003492c", "123456")

#showAvailableSessions()

# Get user input for selecting the session
# Process appropriately, eg. for a recurring task prompt the user to select a specific session

# Present the user with list of options for selected session
# Get users input and process appropriately
