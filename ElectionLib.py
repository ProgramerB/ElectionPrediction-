import sqlite3

def importDataTwitter(id, text, created_at, geo, lang, party, key):
    conn=sqlite3.connect("Election.sqlite")
    cur=conn.cursor()
    try:
        if party == 'b':
            cur.execute('''CREATE TABLE IF NOT EXISTS Twitter_BJP
                (id INTEGER, text TEXT, created_at DATETIME, geo TEXT, lang TEXT, keyword TEXT)''')

            cur.execute('INSERT INTO Twitter_BJP (id, text, created_at, geo, lang, keyword) VALUES (?, ?, ?, ?, ?, ?)',(id, text, created_at, geo, lang, key))
        else:
            cur.execute('''CREATE TABLE IF NOT EXISTS Twitter_INC
                (id INTEGER, text TEXT, created_at DATETIME, geo TEXT, lang TEXT, keyword TEXT)''')

            cur.execute('INSERT INTO Twitter_INC (id, text, created_at, geo, lang, keyword) VALUES (?, ?, ?, ?, ?, ?)',(id, text, created_at, geo, lang, key))
        conn.commit()
    except:
        print("Same Tweet")

def importDataReddit(id, title, text, created_at, score, party, key):
    conn=sqlite3.connect("Election.sqlite")
    cur=conn.cursor()
    
    if party == 'b':
        cur.execute('''CREATE TABLE IF NOT EXISTS Reddit_BJP
            (id INTEGER PRIMARY KEY, title TEXT, text TEXT, created_at FLOAT, score INT, keyword TEXT)''')

        cur.execute('INSERT INTO Reddit_BJP ( title, text, created_at, score, keyword) VALUES ( ?, ?, ?, ?, ?)',( title, text, created_at, score, key))
    else:
        cur.execute('''CREATE TABLE IF NOT EXISTS Reddit_INC
            (id INTEGER PRIMARY KEY, title TEXT, text TEXT, created_at FLOAT, score INT, keyword TEXT)''')

        cur.execute('INSERT INTO Reddit_INC ( title, text, created_at, score, keyword) VALUES ( ?, ?, ?, ?, ?)',( title, text, created_at, score, key))
    conn.commit()

'''def ExportData():
    conn=sqlite3.connect("Election.sqlite")
    cur=conn.cursor()

    textlist=[]
    cur.execute('SELECT text FROM Tweets')
    rows=cur.fetchall()
    print('Total number of rows:',len(rows))
    for row in rows:
        #print(row[0])
        textlist.append(row[0])
    return textlist'''

def exportDataReddit(party):
    conn=sqlite3.connect("Election.sqlite")
    cur=conn.cursor()

    textlist=[]
    if party == 'b':
        cur.execute('SELECT title, text FROM Reddit_BJP')
    else:
        cur.execute('SELECT title, text FROM Reddit_INC')
    rows=cur.fetchall()
    #print('Total number of rows:',len(rows))
    for row in rows:
        #print(row[0])
        textlist.append(row[0]+". "+row[1])
    return textlist

def exportDataTwitter(lang,party):
    conn=sqlite3.connect("Election.sqlite")
    cur=conn.cursor()

    textlist=[]
    if party == 'b':
        cur.execute('SELECT text, lang FROM Twitter_BJP')
    else:
        cur.execute('SELECT text, lang FROM Twitter_INC')
    rows=cur.fetchall()
    #print('Total number of rows:',len(rows))
    for row in rows:
        #print(row[0])
        if row[1] == lang:
            textlist.append(row[0])
            #print(row[1])
    return textlist