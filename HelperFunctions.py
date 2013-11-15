import sqlite3
import datetime
import time

DATABASE = ':memory:'
SCHEMA = 'dbSchema.sql'

USERS = (
        ('1003492c', '12345678536014'),
        ('1102103l', '23456789457015'),
        ('1102115m', '34567890467016'),
        ('1102374p', '45678901400017'),
        ('2039411m', '56789901645017'),
        )

CLASSES = (
        'PSD3',
        'Alg3',
        'AP3',
        'PL3'
        )

SESSIONS = (
        ('30/09/2013'),
        ('07/10/2013'),
        ('14/10/2013'),
        ('21/10/2013'),
        ('28/10/2013'),
        ('04/11/2013'),
        ('11/11/2013'),
        ('18/11/2013'),
        ('25/11/2013'),
        )
START = '14:00'
END = '16:00'


def showAvailableSessions():
    pass

def init_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    with open(SCHEMA, 'r') as f:
        sqlscript = f.read()
        cursor.executescript(sqlscript)
        db.commit()    
    cursor.close()
    populate(db)
    return db

def populate(db):
    for row in USERS:
        createUser(db, *row)

    for i in range(len(CLASSES)):
        createClass(db, CLASSES[i])
        for row in SESSIONS:
            start = row + " " + START
            end = row + " " + END
            sid = insertSession(db, i+1, start, end)
            for uid in range(1, len(USERS)+1):
                userJoinSession(db, sid, uid)


def createClass(db, className):
    cursor = db.cursor()
    cursor.execute("INSERT INTO session_types(label) VALUES (?)", (className,) )    # You need the comma at the end.
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

def insertSession(db, class_id, start, end):
    # Thanks to this stack overflow answer: http://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python
    startSecs = time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y %H:%M").timetuple())
    endSecs = time.mktime(datetime.datetime.strptime(end, "%d/%m/%Y %H:%M").timetuple())

    cursor = db.cursor()
    sql = "INSERT INTO sessions(session_type_id, starts, ends) VALUES(?, ?, ?)"
    cursor.execute(sql, (class_id, startSecs, endSecs))
    db.commit()
    rowid = cursor.lastrowid
    cursor.close()
    return rowid

def getSession(db, sessionID):
    pass

def createUser(db, name, barcode):
    cursor = db.cursor()
    cursor.execute("INSERT INTO users(username, barcode) VALUES (?, ?)", (name, barcode) )
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

def userJoinSession(db, session_id, user_id):
    sql = "INSERT INTO session_users(session_id, user_id) VALUES(?, ?)"
    cursor = db.cursor()
    cursor.execute(sql, (session_id, user_id))
    db.commit()
