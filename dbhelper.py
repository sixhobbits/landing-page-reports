import sqlite3
from datetime import datetime

def setup():
    conn = sqlite3.connect('landingpages.sqlite')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE pages 
             (date text, name text, url text, html text, plaintext text)''')

    conn.close()


def add_page(name, url, html, text):
    conn = sqlite3.connect('landingpages.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO pages(name, url, html, plaintext) VALUES (?,?,?,?)", (name, url, html, text))
    conn.commit()
    conn.close()



