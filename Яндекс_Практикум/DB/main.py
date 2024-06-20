

import sqlite3 as sq

con = sq.connect('db_video_type_slogan.sqlite')

cur = con.cursor()


# players = [
#     ('Alex Ovechkin', 845, 1),
#     ('Ilya Kovalchuck', 450, 0),
#     ('Pavel Datsuk', 290, 3),
#     ('Eugeny Malkin', 500, 3),
#     ('Sidney Crosby', 10000, 22),
#     ('Patrick Kane',460, 3),
# ]


# players2 = [
#     ('Kirill Kaprizov', 120, 0),
#     ('Eugeny Kuznetsov', 200, 1), 
# ]






# cur.execute('''
#     CREATE TABLE IF NOT EXISTS hockey_players(
#         name TEXT NOT NULL,
#         pucks INTEGER NOT NULL,
#         stanley_caps INTEGER NOT NULL
#     );
# ''')

#cur.execute('INSERT INTO hockey_players VALUES(?, ?, ?);', ('EugenySobyanin', 121, 3))
#cur.executemany('INSERT INTO hockey_players VALUES(?, ?, ?);', players)
# cur.executemany('INSERT INTO hockey_players VALUES(?, ?, ?);', players2)


result = cur.execute('''
    SELECT video_products.title,
            slogans.slogan_text
    FROM video_products,
        slogans
    WHERE video_products.slogan_id = slogans.id
    ;
''')

#con.commit()

#print(result)

for el in result:
    print(el)
    
    
con.close()


