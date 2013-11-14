import glob
import sqlite3
import datetime
import time


def showAvailableSessions():
	pass

def init_db():
	# print glob.glob("*.csv")
	db = sqlite3.connect(":memory:")
	cursor = db.cursor()
	f = open('dbSchema.sql', 'r')
	sqlscript = f.read()
	f.close()
	cursor.executescript(sqlscript)
	db.commit()
	
	# Was used to get all the fields of the DB
	# cursor.execute("PRAGMA table_info(session_types)")
	# print cursor.fetchall()
	
	cursor.close()
	return db
	
def getClasses(db):
	cursor = db.cursor()
	cursor.execute("SELECT sessions.id, session_types.Label FROM sessions, session_types WHERE sessions.session_type_id=session_types.id")
	db.commit()
	rows = cursor.fetchall()
	if not rows:
		print "No classes."
	else:
		for row in rows:
			print "%s. %s" % (row[0], row[1]) 
	cursor.close()
	
def createClass(db, className):
	cursor = db.cursor()
	cursor.execute("INSERT INTO session_types(label) VALUES (?)", (className,) )
	db.commit()
	
	# cursor.execute("SELECT * FROM session_types")
	# rows = cursor.fetchall()
	# print rows
	
	cursor.close()
	
def insertSession(db, className, start, end):
	cursor = db.cursor()
	cursor.execute("SELECT id FROM session_types WHERE label=(?)", (className,))
	try:
		sessionID = cursor.fetchone()[0]
		
		# Thanks to this stack overflow answer: http://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python
		startSecs = time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y %H:%M").timetuple())
		endSecs = time.mktime(datetime.datetime.strptime(end, "%d/%m/%Y %H:%M").timetuple())
		
		cursor.execute("INSERT INTO sessions(session_type_id, starts, ends) VALUES (?, ?, ?)", (sessionID, startSecs, endSecs) )
		db.commit()

	except:
		print "Class not found."
	finally:
		cursor.close()

	
	
# if __name__ == '__main__':
# 	run()