import sqlite3 as sql

conn = sql.connect("sql_example.db")
# opens database

c = conn.cursor()
# cursor of database

def createTable():
	# creating a table
	c.execute("CREATE TABLE example(Language TEXT, Version REAL, Skill TEXT)")

def enterdata():
	# entering data into a table
	c.execute("INSERT INTO example VALUES('Python', 3.4, 'starter')")
	c.execute("INSERT INTO example VALUES('Python', 2.7, 'good')")
	c.execute("INSERT INTO example VALUES('Python', 3.5, 'expert')")
	c.execute("SELECT * FROM example ")
	conn.commit()

def dynamicdata():
	# inputting dynamic data
	lang = input("what lang? ")
	version = float(input("what version?"))
	skill = input("what level? ")

	c.execute("INSERT INTO example (language, version, skill) VALUES(?, ?, ?)", (lang, version, skill))

	conn.commit()

def find():
	# reading data
	sql_find = ("SELECT * FROM example")

	for row in c.execute(sql_find):
		print(row)
	print("\n\n")
	sql_find = ("SELECT * FROM example where Skill == 'expert'")
	for row in c.execute(sql_find):
		print(row)

	what_skill = input("what skill? ")
	print("\n\n")
	sql_find = ("SELECT * FROM example where Skill == ?")
	for row in c.execute(sql_find, [(what_skill)]):
		print(row)

find()

#conn.close()
