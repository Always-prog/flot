from constructor import *
from choise import runC
import sqlite3 as sq
conn = sq.connect("info.db")
cursor = conn.cursor()
"""
В таблице "USERS" в базе данных "info.db" находятся следующие значения:
U = имя пользователья
P = пароль пользователья
I = индекс пользователья
(логин главного USER-а: "MegaUser"
пароль главного USER-а: "mega-user11")
"""
def user_login():
    global En1
    global En2
    global LR
    login = En1.save_entry()
    password = En2.save_entry()
    MegaUser = False
    sql = "SELECT rowid, * FROM USERS ORDER BY I"
    try:
        for row in cursor.execute(sql):
            if login == row[1]:
                print("логин найден")
                if password == row[2]:
                    print("пароль совпадает")
                    if login == "MegaUser":
                        MegaUser = True
                    user_login_successfully(MegaUser)
                else:
                    print("неверный пароль")
    except(BaseException):
        pass

def user_login_successfully(MegaUser):
    global LR
    global runC
    global conn
    LR.quit()
    conn.close()
    runC(MegaUser)

login_root = Tk()
login_root["bg"] = "#03899c"
login_root.geometry("300x300")
login_root.title("Авторизуйтесь")
LR = instruments(login_root)
En1 = instruments(login_root)
En2 = instruments(login_root)
LR.send_label("Введите логин",80,20)
En1.send_entry(80,70,25)
LR.send_label("Введите пароль",80,150)
En2.send_entry(80,200,25)
LR.send_button("Ввести",120,260,lambda: user_login())
login_root.mainloop()

