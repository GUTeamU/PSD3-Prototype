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


	
	
# if __name__ == '__main__':
# 	run()