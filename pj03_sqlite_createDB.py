import sqlite3

conn = sqlite3.connect('/home/[USER NAME]/python/DB/buttonDB.db')
c = conn.cursor()
#c.execute('DROP TABLE IF EXISTS bStatesTable')
c.execute('CREATE TABLE bStatesTable (bState TEXT, bValue INTEGER, date TEXT)')
example1 = 'on'
#c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, DATETIME('now'))", (example1, 1))
c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, DATETIME('now','localtime'))", (example1, 1))
example2 = 'off'
#c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, DATETIME('now'))", (example2, 0))
c.execute("INSERT INTO bStatesTable (bState, bValue, date) VALUES (?, ?, DATETIME('now','localtime'))", (example2, 0))
conn.commit()
conn.close()    
#===SELECT
conn = sqlite3.connect('/home/[USER NAME]/python/DB/buttonDB.db')
c = conn.cursor()
#c.execute("SELECT * FROM bStatesTable WHERE date BETWEEN '2022-01-01 10:10:10' AND DATETIME('now')")
c.execute("SELECT * FROM bStatesTable WHERE date BETWEEN '2022-01-01 10:10:10' AND DATETIME('now','localtime')")
results = c.fetchall()
conn.close()

print("SELECT DB results: \n", results)