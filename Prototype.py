from HelperFunctions import *

# Get user login

# Import the sessions
# Present the user with the sessions
db = init_db()
print "before"
getSessions(db)
print "After"
insertSession(db, "PSD3")
getSessions(db)
#showAvailableSessions()

# Get user input for selecting the session
# Process appropriately, eg. for a recurring task prompt the user to select a specific session

# Present the user with list of options for selected session
# Get users input and process appropriately