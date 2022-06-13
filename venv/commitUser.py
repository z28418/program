def createTable():
    db = "./customers.db"
    conn = sqlite3.connect(db)


    conn.execute('''CREATE TABLE IF NOT EXISTS users
                    (USERID        INT     PRIMARY KEY     NOT NULL,
                     CUST_NAME     TEXT    NOT NULL,
                     PHONE          TEXT    NOT NULL, 
                      
                     ADDRESS        TEXT   NOT NULL)
                     ;''')
    

def createUser():
    pass
    
