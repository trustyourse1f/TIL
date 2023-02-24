import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS cities')
c.execute('''
''')
