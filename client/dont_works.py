from constructor import *
from tkinter import *
import sqlite3 as sq
import webbrowser
import random
conn = sq.connect("info.db")
cursor = conn.cursor()

"""
В талбице "DW" содержатся следующие значения:
DA = дата обнаружения
OB = оборудование
NA = нименование
US = услования
OT = ответственный 
SO = состояние
DO = документ
I = индекс элемента 


"""

DW_root = None
DW = None
sql = None
index_height = 150
en1 = None
en2 = None
en3 = None
en4 = None
en5 = None
en6 = None
en7 = None
data = None
deleteTFDW = False
elem = None

def Gotovo(cal):
    global data
    data = cal.get_date()
def func_add(list_add,index_height,indexs):
    global DW
    global WD_info
    index_x = 100
    index_doc = 0
    doc_name = []
    for elem in range(len(list_add)):
        if "#<file>#" in list_add[elem]:
            
            DW.send_canvas_button(list_add[elem][:12],index_x,index_height,lambda: WD_info(indexs))
        elif list_add[elem] == "0":
            DW.send_canvas_button("Состояние 1",index_x,index_height,lambda: WD_info(indexs))
        elif list_add[elem] == "1":
            DW.send_canvas_button("Состояние 2",index_x,index_height,lambda: WD_info(indexs))
        elif list_add[elem] == "2":
            DW.send_canvas_button("Состояние 3",index_x,index_height,lambda: WD_info(indexs))

        else:
            DW.send_canvas_button(list_add[elem],index_x,index_height,lambda: WD_info(indexs))
        index_x += 150


def WD_info(indexs):
    global update
    global deleteTFDW
    global elem
    if deleteTFDW == True:
        sql = "DELETE FROM DW WHERE I = "+str(indexs)
        cursor.execute(sql)
        conn.commit()
        update()
    else:

        sql = "SELECT rowid, * FROM DW ORDER BY I"
        for row in cursor.execute(sql):
            if str(indexs) == str(row[8]):
                elem = row
                break

        info_root = Tk()
        info_root.geometry("700x700")
        info_root.title("Информация о неисправности")
        IR = instruments(info_root)
        IR.send_canvas()
        IR.add_scrollH()
        IR.add_scrollV()
        IR.send_canvas_text("Дата:",50,50)
        IR.send_canvas_text("Оборудование:",50,100)
        IR.send_canvas_text("Наименование:",50,150)
        IR.send_canvas_text("условия:",50,200)
        IR.send_canvas_text("ответственный:",50,250)
        IR.send_canvas_text("Состояние:",50,300)
        IR.send_canvas_text("Документ:",50,350)
        IR.send_canvas_text(elem[1],200,50)
        IR.send_canvas_text(elem[2],200,100)
        IR.send_canvas_text(elem[3],200,150)
        IR.send_canvas_text(elem[4],200,200)
        IR.send_canvas_text(elem[5],200,250)
        IR.send_canvas_text(elem[6],200,300)
        IR.send_canvas_button("Посмотреть документ",200,350, lambda: view_doc(elem))
        def view_doc(elem):
            webbrowser.open(elem[7])
        info_root.mainloop()




def fulls():
    global DW
    global sql
    global cursor
    global func_add
    global index_height
    global index_last
    sql = "SELECT rowid, * FROM DW ORDER BY I"
    for row in cursor.execute(sql):
        func_add([row[1],row[2],row[3],row[4],row[5],row[6],row[7]],index_height,row[8])
        index_height += 100
        

def update():
    global DW
    global index_height
    global deleteTFDW
    index_height = 150
    deleteTFDW = False
    DW.clear_window()
    start()
    fulls()
 
def delete():
    global deleteTFDW
    global DW
    DW.send_canvas_text("Нажмите на элемент котоырй хотите удалить",600,25)
    deleteTFDW = True

def add():
    global en1
    global en2
    global en3
    global en4
    global en5
    global en6
    global en7
    global index_last
    global update
    global Gotovo
    def add_save():
        global en1
        global en2
        global en3
        global en4
        global en5
        global en6
        global en7
        global add_DW
        global index_last
        global update
        global data
        index_last = random.randint(0,999999999)
        sql = "SELECT rowid, * FROM DW ORDER BY I"
        for row in cursor.execute(sql):
            index_last = random.randint(0,999999999)
            while row[8] == index_last:
                index_last = random.randint(0,999999999)
        
        print(index_last)
        save_list = [data,
                     en2.save_menu(),
                     en3.save_entry(),
                     en4.save_entry(),
                     en5.save_entry(),
                     en6.save_radio(),
                     en7.save_entry(),
                     str(index_last),]
        sql = "INSERT INTO DW VALUES (?,?,?,?,?,?,?,?)"
        paste = (save_list,)
        cursor.executemany(sql,paste)
        conn.commit()
        en3.clear_entry()
        en4.clear_entry()
        en5.clear_entry()
        en7.clear_entry()
        update()
    def data_send():
        global data
        global Gotovo
        root_data_send = Tk()
        root_data_send.title("Дата обнаружения")
        data_root = Calendar(master=root_data_send)
        data_root.pack()
        btn = Button(root_data_send,text="Готово",command=lambda: Gotovo(data_root))
        btn.pack()
        root_data_send.mainloop()

    add_root_DW = Tk()
    add_root_DW.geometry("600x600")
    add_root_DW.title("Регистрация неисправностей")
    add_root_DW["bg"] = "#03899c"
    add_DW = instruments(add_root_DW)
    add_DW.send_label("Дата обнаружения:",20,20)
    add_DW.send_label("Оборудование:",20,70)
    add_DW.send_label("Наименование:",20,120)
    add_DW.send_label("Условия:",20,170)
    add_DW.send_label("Ответственный:",20,220)
    add_DW.send_label("состояние:",20,270)
    add_DW.send_label("документ:",20,390)
    en1 = instruments(add_root_DW)
    en2 = instruments(add_root_DW)
    en3 = instruments(add_root_DW)
    en4 = instruments(add_root_DW)
    en5 = instruments(add_root_DW)
    en6 = instruments(add_root_DW)
    en7 = instruments(add_root_DW)
    en1.send_button("Выставить дату",150,20,lambda: data_send())
    en2.send_menu(["Пусковая установка","Антенный пост","Система управления"],150,70)
    en3.send_entry(150,120,15)
    en4.send_entry(150,170,15)
    en5.send_entry(150,220,15)
    en6.send_radio(["Состояние 1", "Состояние 2", "Состояние 3"], 150, 270)
    en7.send_entry(150,390,25)
    add_DW.send_button("Сохранить",250,500, lambda: add_save())

    add_root_DW.mainloop()
def start():
    global DW
    DW = instruments(DW_root)
    DW.send_canvas()
    DW.add_scrollV()
    DW.send_canvas_button("Обновить",325,25, lambda: update())
    DW.send_canvas_button("Зарегистрировать неисправность",100,25, lambda: add())
    DW.send_canvas_button("Удалить", 245,25,lambda: delete())
    DW.send_canvas_text("Дата обнаружения",100,80)
    DW.send_canvas_text("Оборудование",250,80)
    DW.send_canvas_text("Наименование",400,80)
    DW.send_canvas_text("Условия",550,80)
    DW.send_canvas_text("Ответственный",700,80)
    DW.send_canvas_text("Состояние",850,80)
    DW.send_canvas_text("Документ",1000,80)




def run():
    global DW_root
    global start
    global fulls
    DW_root = Toplevel()
    DW_root.geometry("1200x600")
    DW_root.title("Регистрация неисправностей")
    start()
    fulls()
    DW_root.mainloop()
