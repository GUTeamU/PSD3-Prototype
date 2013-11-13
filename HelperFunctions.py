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
	
	
# if __name__ == '__main__':
# 	run()