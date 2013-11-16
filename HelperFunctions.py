import sqlite3
import datetime
import time

DATABASE = ':memory:'
SCHEMA = 'dbSchema.sql'

USERS = (
        ('Michael Cromie', '1003492c', '12345678536014'),
        ('Fraser Leishman', '1102103l', '23456789457015'),
        ('Andrew McDonald', '1102115m', '34567890467016'),
        ('Matthew Paterson', '1102374p', '45678901400017'),
        ('Edvin Malinovskis', '2039411m', '56789901645017'),
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
    sql = "INSERT INTO session_types(label) VALUES (?)"
    cursor.execute(sql, (className,) )    # You need the comma at the end.
                                          # It won't work without it for some reason.
    db.commit()
    cursor.close()

def getClasses(db):
    cursor = db.cursor()
    sql = "SELECT id, label FROM session_types";
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

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

def getSessions(db, class_id):
    sql = """
        SELECT id, datetime(starts, 'unixepoch'),
        time(ends, 'unixepoch') FROM sessions WHERE session_type_id = ?
        """
    cursor = db.cursor()
    cursor.execute(sql, (class_id,))
    return cursor.fetchall()

def getStudents(db, session_id):
    sql = """
        SELECT users.full_name, users.username, session_users.attended
        FROM session_users
        LEFT JOIN users ON(users.id = session_users.user_id)
        WHERE session_users.session_id = ?
        """
    cursor = db.cursor()
    cursor.execute(sql, (session_id,))
    return cursor.fetchall()

def markStudents(db, session_id, attended, users):
    sql = "SELECT id FROM users WHERE username "
    cursor = db.cursor()
    if len(users) > 1:
        sql += "IN({0})".format(",".join("?" * len(users)))
    else:
        sql += "= ?"
    sql = "UPDATE session_users SET attended = ? WHERE session_id = ? AND user_id IN({0})".format(sql)
    values = [attended, session_id] + users
    cursor.execute(sql, values)
    if cursor.rowcount:
        db.commit()
    else:
        db.rollback()

def updateAttendance(db, session_id, data):
    sql = "UPDATE session_users SET attended = 0 WHERE session_id = ?"
    cursor = db.cursor()
    cursor.execute(sql, (session_id,))
    if cursor.rowcount:
        sql = "SELECT id FROM users WHERE barcode "
        if len(data) > 1:
            sql += "IN({0})".format(",".join("?" * len(data)))
        else:
            sql += "= ?"
        sql = "UPDATE session_users SET attended = 1 WHERE session_id = ? AND user_id IN({0})".format(sql)
        values = [session_id] + [row[0] for row in data]
        cursor.execute(sql, values)
        if cursor.rowcount:
            db.commit()
            return

    # one of the updates failed
    db.rollback()

def createUser(db, full_name, username, barcode):
    cursor = db.cursor()
    sql = "INSERT INTO users(full_name, username, barcode) VALUES (?, ?, ?)"
    cursor.execute(sql, (full_name, username, barcode) )
    db.commit()

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
    for line in data:
        print(line)
    pass

def createUser(db, full_name, username, barcode):
    cursor = db.cursor()
    sql = "INSERT INTO users(full_name, username, barcode) VALUES (?, ?, ?)"
    cursor.execute(sql, (full_name, username, barcode) )
    db.commit()

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
