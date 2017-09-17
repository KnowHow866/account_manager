import util
import DB
import sqlite3
import sys

# global 
space = 50

# test of data base connection
util.welcome_msg(space)
try:
    DB.init_db()
    util.msg('This is your firse time log in',space)
    util.msg('Wish you happy with my service',space)
except:
    util.log('DB ok')

while(1):
    cmd = input('<< ')

    if(cmd == 'e'): sys.exit()
    elif(cmd == 'h'): util.info(space)
    elif(cmd == 'n'): DB.insert(space)
    elif(cmd == 'l'): DB.list_account(space)
    elif(cmd == 't'): DB.list_tag(space)
    elif(cmd == 'u'): DB.update(space)
    elif(cmd == 'd'): DB.delete(space)
    else: 
        util.welcome_msg(space)



