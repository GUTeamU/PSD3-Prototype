import glob
import sqlite3

def showAvailableSessions():
	pass

def init_db():
	print glob.glob("*.csv")
	db = sqlite3.connect(":memory:")
	cursor = db.cursor()
	f = open('dbSchema.sql', 'r')
	sqlscript = f.read()
	f.close()
	cursor.executescript(sqlscript)
	db.commit()
	
	# Was used to test the DB
	# cursor.execute("PRAGMA table_info(session_types)")
	# print cursor.fetchall()
	
	cursor.close()
	return db
	
def getSessions(db):
	cursor = db.cursor()
	cursor.execute("SELECT sessions.id, session_types.Label FROM sessions, session_types WHERE sessions.session_type_id=session_types.id")
	db.commit()
	rows = cursor.fetchall()
	for row in rows:
		print "%s. %s" % (row[0], row[1]) 
	cursor.close()
	
def insertSession(db, session):
	cursor = db.cursor()
	cursor.execute("INSERT INTO session_types(label) VALUES (?)", (session,) )
	db.commit()
	cursor.execute("SELECT * FROM session_types")
	rows = cursor.fetchall()
	print rows
	cursor.close()

	
	
# if __name__ == '__main__':
# 	run()