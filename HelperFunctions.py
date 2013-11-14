import glob
import sqlite3
import datetime
import time


def showAvailableSessions():
	pass

def init_db():
	db = sqlite3.connect(":memory:")
	cursor = db.cursor()
	f = open('dbSchema.sql', 'r')
	sqlscript = f.read()
	f.close()
	cursor.executescript(sqlscript)
	db.commit()	
	cursor.close()
	return db
	
def createClass(db, className):
	cursor = db.cursor()
	cursor.execute("INSERT INTO session_types(label) VALUES (?)", (className,) )	# You need the comma at the end.
																					# It won't work without it for some reason.
	db.commit()
	cursor.close()
	
def getClasses(db):
	cursor = db.cursor()
	cursor.execute("SELECT sessions.id, session_types.Label FROM sessions, session_types WHERE sessions.session_type_id=session_types.id")
	rows = cursor.fetchall()
	classes = []
	if not rows:
		print "No classes."
	else:
		for row in rows:
			print "%s. %s" % (row[0], row[1]) 
			classes.append(str(row[1]))
	cursor.close()
	return classes
	
def insertSession(db, className, start, end, capacity):
	cursor = db.cursor()
	cursor.execute("SELECT id FROM session_types WHERE label=(?)", (className,))
	try:
		sessionID = cursor.fetchone()[0]
		
		# Thanks to this stack overflow answer: http://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python
		startSecs = time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y %H:%M").timetuple())
		endSecs = time.mktime(datetime.datetime.strptime(end, "%d/%m/%Y %H:%M").timetuple())
		
		cursor.execute("INSERT INTO sessions(session_type_id, starts, ends, capacity) VALUES (?, ?, ?, ?)", (sessionID, startSecs, endSecs, capacity) )
		db.commit()

	except:
		print "Class not found."
	finally:
		cursor.close()
	
def getSessions(db, sessionID):
	cursor = db.cursor()
	cursor.execute("SELECT sessions.id, session_types.label, sessions.starts, sessions.ends, sessions.capacity \
	               FROM sessions, session_types \
	               WHERE sessions.session_type_id==session_types.id \
	               AND session_types.id==(?)", (sessionID,))
	rows = cursor.fetchall()
	if not rows:
		print "Invalid session selection"
	else:
		for row in rows:
			print "%s. %s: Start time: %s, End time: %s, Capacity: %s, Space Available: %s " \
			% (row[0], row[1], row[2], row[3], row[4], getSlotsAvailable(db, row[0]) )
	cursor.close()

def getSlotsAvailable(db, sessionID):
	cursor = db.cursor()	
	cursor.execute("SELECT sessions.capacity \
	               FROM sessions \
	               WHERE sessions.id==(?)", (sessionID,))
	capacity = cursor.fetchall()[0][0]
	
	cursor.execute("SELECT session_users.session_id \
	               FROM session_users \
	               WHERE session_users.session_id==(?)", (sessionID,))
	rows = cursor.fetchall()
	cursor.close()
	return capacity-len(rows)

def userJoinSession(db, sessionID, userID):
	cursor = db.cursor()
	if(getSlotsAvailable(db, sessionID) > 0):
		cursor.execute("INSERT INTO session_users(user_id, session_id) VALUES (?, ?)", (userID, sessionID) )
		db.commit()
	cursor.close()

def showUsersSessions(db, userID):
	pass

def createUser(db, name, password, barcode):
	cursor = db.cursor()
	cursor.execute("INSERT INTO users(username, password, barcode) VALUES (?, ?, ?)", (name, password, barcode) )
	db.commit()
	cursor.close()

def getUsers(db):
	cursor = db.cursor()
	cursor.execute("SELECT username, barcode FROM users")
	rows = cursor.fetchall()
	users = []
	if not rows:
		print "No users."
	else:
		for row in rows:
			print "%s, %s" % (row[0], row[1])
			users.append(str(row[1]))
	cursor.close()
	return users

def loginUser(db, name, pw):
	cursor = db.cursor()
	cursor.execute("SELECT password FROM users WHERE username=(?)", (name,))
	rows = cursor.fetchall()
	if not rows:
		print "This user is not registered on the system."
		return false
	elif rows[0][0] == pw:
		print "Successful"
		return True
	else:
		print "Login Failed"
		return False
	cursor.close()


	

	
	
# if __name__ == '__main__':
# 	run()
