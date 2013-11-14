
# Shows all csv files
print glob.glob("*.csv")

# Was used to get all the fields of the table session_types
cursor.execute("PRAGMA table_info(session_types)")
print cursor.fetchall()

# Gets all data from session_types and prints it
cursor.execute("SELECT * FROM session_types")
rows = cursor.fetchall()
print rows

