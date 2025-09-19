import sqlite3



def create_table_user():
    conn = sqlite3.connect('your_database.db') 
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Username TEXT, 
            Password TEXT, 
            Nickname TEXT, 
            Locked INTEGER
        )
    """)
    conn.commit()
    conn.close()


def save_user(Username,Password,Nickname,Locked):
    connection = sqlite3.connect("data_access/user_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into user (Username , Password , Nickname , Locked) values(?,?,?,?)",
                   [Username, Password, Nickname, Locked])
    connection.commit()
    connection.close()