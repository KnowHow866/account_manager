import os


# 統一log 設定
def log(msg):
    import logging
    logging.basicConfig(level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    if type(msg) == str:
        logging.disable(logging.CRITICAL)
        logging.debug(msg)
    else:
        logging.debug('logging parameter type wrong')

# 格式化輸出
def msg(msg, num):
    msg = str(msg)
    print(msg.ljust(num,'-'))

# 系統回復訊息
def back(msg, num):
    msg = str(msg)
    print(msg.ljust(num,'-'))
    print()

# 歡迎訊息
def welcome_msg(space):
    os.system('clear')
    msg('',space)
    msg('',space)
    msg('WELCOME TO ACOUNT MANAGER',space)
    msg('',space)
    msg('',space)

    msg('press h to get help',space)
    msg('press n to generate new account',space)
    msg('press l to list all account detail',space)
    msg('press t to list all tag of account',space)
    msg('press u to update passwd of account',space)
    msg('press d to delete account',space)
    msg('press e to close the app',space)
    print()
    print("".ljust(space,'*'))
    print()

def info(space):
    os.system('clear')
    msg('An account consist of 3 para',space)
    msg('1. tag (text) : this key word help you to distinguish account',space)
    msg('2. account : the account (may be email or something)',space)
    msg('3. passwd : the pass word',space)

# md5 加密
def md5(passwd):
    import hashlib  
    if type(passwd) == str :
        m = hashlib.md5()
        # ust-8 編碼轉換
        m.update( passwd.encode('utf-8') )
        return m.hexdigest()
    else:
        return 'type wrong'


