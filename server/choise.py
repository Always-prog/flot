from constructor import *
from data import run as runD
from dont_works import run as runDW
from server import PTS_run
import sqlite3 as sq

conn = sq.connect("info.db")
cursor = conn.cursor()

def add_user(MegaUser):
    def save_user(save_login,save_password):
        save_login = save_login
        save_password = save_password
        paste = [(save_login,save_password,1)]
        sql = "INSERT INTO USERS VALUES (?,?,?)"
        cursor.executemany(sql,paste,)
        conn.commit()
        print("Пользователь успешно добавлен!" )
    MegaUser = MegaUser
    add_user_root = Tk()
    add_user_root["bg"] = "#03899c"
    add_user_root.geometry("400x300")
    add_user_root.title("Новый пользователь")
    AUR = instruments(add_user_root)
    En1 = instruments(add_user_root)
    En2 = instruments(add_user_root)
    AUR.send_label("Логин нового пользователя",50,30)
    En1.send_entry(30,80,30)
    AUR.send_label("Пароль пользователя",50,120)
    En2.send_entry(30,170,30)
    AUR.send_button("Создать",250,140, lambda: save_user(En1.save_entry(),En2.save_entry()))
    add_user_root.mainloop()

def runC(MegaUser):
    MegaUser = MegaUser
    start_root = Tk()
    ST = instruments(start_root)
    ST.send_canvas()
    ST.send_canvas_text("Выберите действие",40,20)
    ST.send_canvas_button("Календарный план",200,40, lambda: runD())
    ST.send_canvas_button("Журнал неисправностей",200,100, lambda: runDW())
    ST.send_canvas_button("Отправить базу данных",200,160, lambda: PTS_run())
    if MegaUser == True:
        ST.send_canvas_button("Добавить пользователя",200,220,lambda: add_user(MegaUser))
    start_root.mainloop()
