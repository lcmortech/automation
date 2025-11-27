import sqlite3

conn = sqlite3.connect("tutorial.db")

cur = conn.cursor()

cur.execute("CREATE TABLE movie(title, year score)")

cur.execute("SELECT title FROM movies")

result = cur.execute("SELECT name FROM sqlite_master")