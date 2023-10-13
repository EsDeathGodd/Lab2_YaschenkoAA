import sqlite3



    
def checkIfRegistered(login): # checking if user login already exists in db
    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()
        

        sql_select_query = """select count(*) from userinfo where login= ?"""
        cursor.execute(sql_select_query, (login,))
        usersamount = cursor.fetchall()
        cursor.close()
       
        usersamount = str(usersamount[0])[1:-2]
        if int(usersamount) != 0:
            return True
        else:
            return False
        

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()






def addUser(login:str,password:str): # not being used bc yes...
    try:
        sqlite_connection = sqlite3.connect('laba.db')
        cursor = sqlite_connection.cursor()
        

        sqlite_insert_with_param = """INSERT INTO userinfo
                             (login,password)
                             VALUES ( ?, ?);"""

        data_tuple = (str(login),str(password))
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")