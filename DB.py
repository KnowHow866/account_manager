import util
import os
import sqlite3

def db_conn():
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id,account_key,account,passwd FROM account')
    conn.commit()
    conn.close()

# 初始化資料庫函式
def init_db():
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()
    util.log('Dtabase init ...')

    # cursor.execute('DROP TABLE IF EXISTS account')
    # conn.commit()
    cursor.execute('''CREATE TABLE account(
        id            INTEGER PRIMARY KEY     NOT NULL,
        tag	            text	NOT NULL,
        account     	text	NOT NULL,
        passwd		    text	NOT NULL
        );
    ''')
    util.log('init over')
    conn.commit()

    util.log('Close database')
    conn.close()

def insert(space):
    os.system('clear')
    util.msg('An account need 3 para to build',space)
    util.msg('1. tag (text) : this key word help you to distinguish account',space)
    util.msg('2. account : the account (may be email or something)',space)
    util.msg('3. passwd : the pass word',space)
    print()

    tag= input('tag << ')
    account = input('account << ')
    passwd = input('passwd << ')

    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO account(tag,account,passwd) VALUES (?,?,?)',(tag,account,passwd) )
    cursor.rowcount
    conn.commit()

    os.system('clear')
    util.msg('CRETE NEW ACCOUNT SUCCESS',space)
    cursor.execute('SELECT * FROM account WHERE tag = ?', (tag,) )
    for row in cursor:
        print("id = ", row[0])
        print("tag = ", row[1])
        print("account = ", row[2])
        print("passwd = ", row[3], "\n")

    conn.close()

def list_account(space):
    util.msg('ACCOUNT LIST',space)
    print()

    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM account')
    for row in cursor:
        print("id = ", row[0])
        print("tag = ", row[1])
        print("account = ", row[2])
        print("passwd = ", row[3], "\n")

    conn.close()

def list_tag(space):
    util.msg('tag LIST',space)
    print()

    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM account')
    for row in cursor:
        print("* ", row[1])

    conn.close()    

def update(space):
    tag = input('Please input tag you want to update: ')
    passwd = input('New passwd: ')

    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE account SET passwd = ? WHERE tag = ?', (passwd,tag) )
    conn.commit()

    os.system('clear')
    util.msg('UPDATE SUCCESS',space)
    cursor.execute('SELECT * FROM account WHERE tag = ?', (tag,) )
    for row in cursor:
        print("tag = ", row[1])
        print("account = ", row[2])
        print("passwd = ", row[3], "\n")

def delete(space):
    tag = input('Input tag want to be deleted; ')

    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM account WHERE tag = ?',(tag,))
    conn.commit()

    util.msg('Numbers of rows to be delted: ' + str(conn.total_changes) , space)
    
    