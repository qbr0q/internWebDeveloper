import sqlite3

def create_table():
    with sqlite3.connect('DB/TFIDF.sqlite') as con:
        cur = con.cursor()
        query = '''
            CREATE TABLE IF NOT EXISTS tf_idf(
                word TEXT,
                tf REAL,
                idf REAL
            );
        '''
        cur.execute(query)
        con.commit()

def add_tfidf(word, tf, idf):
    create_table()
    with sqlite3.connect('DB/TFIDF.sqlite') as con:
        cur = con.cursor()
        query = '''
        INSERT INTO tf_idf (word, tf, idf) VALUES(?, ?, ?);
        '''
        cur.execute(query, (word, tf, idf))
        con.commit()

def clean_bd():
    with sqlite3.connect('DB/TFIDF.sqlite') as con:
        cur = con.cursor()
        query = '''
        DELETE FROM tf_idf;
        '''
        con.execute(query)
    con.commit()

def get_context():
    with sqlite3.connect('DB/TFIDF.sqlite') as con:
        cur = con.cursor()
        query = '''
        SELECT *
        FROM tf_idf
        ORDER BY idf
        LIMIT 50
        '''
        words = cur.execute(query).fetchall()
    return words