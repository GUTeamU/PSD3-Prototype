
def init_db():

# Creates a class, eg. PSD3 or Algs.	
def createClass(db, className):

# Returns the list of classes currently added.
def getClasses(db):

# Creates a session. Session must be associated with a class that already exists in the database.
# Class is inputted by its unique ID.	
def insertSession(db, sessionID, start, end, capacity):

# Prints the list of sessions available for a class via its unique ID.
def getSessions(db, classID):

# Prints the specified sessions information
def getSession(db, sessionID):

# Returns the number of available spaces in a given session via its unique session ID.
def getSlotsAvailable(db, sessionID):

# Inserts a user into a session if there is enough space.
# There will need to be more error checking added later on for this function,
# eg. that they haven't already signed up for a session, checking user exists etc.
def userJoinSession(db, sessionID, username):

# Shows the user the sessions they have signed up for.
def showUsersSessions(db, username):

# Creates a user in the user database.
def createUser(db, name, password, barcode):

# Gets a list of users and their barcodes.
def getUsers(db):

# A simple login function.
def loginUser(db, name, pw):
