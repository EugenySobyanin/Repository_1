import sqlite3 as sq

con = sq.connect('database1')

cur = con.cursor()


players = [
    ('Alex Ovechkin',),
    ('Ilya Kovalchuck',),
    ('Pavel Datsuk',),
    ('Eugeny Malkin',),
    ('Sidney Crosby',),
    ('Patrick Kane',),
]







cur.execute('''
    CREATE TABLE IF NOT EXISTS hockey_players(
        id INTEGER RRIMARY KEY,
        name TEXT NOT NULL
    );
    

    
''')


cur.execute('''
    CREATE TABLE IF NOT EXISTS nhl_teams(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        players TEXT NOT NULL
    );
    
''')



# cur.execute('INSERT INTO hockey_players VALUES(?);', ('EugenySobyanin'))
# cur.executemany('INSERT INTO hockey_players VALUES(?);', players)









con.commit()
con.close()