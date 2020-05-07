#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
Эта программа создана для введения записей на фолте, для распределения объязанностей
сотрудников.
Эта программа крайне стабильна, использует язык программирование Python версии 3.7,
также технологии баз данных sqlite3, для работы на локальных устройствах.
применяется технологии ООП, для создание многочисеных объектов схожий между собой.
класс "instruments" является паттерном для обектов как one, tree, add.


"""

"""
таблица с датами под названием "dat":
эл.1  : O  = ответственный
эл.2  : S  = статус
эл.3  : N1 = наименование номер 1
эл.4  : N2 = наименование номер 2
эл.5  : T1 = требуемое количество штук 1 
эл.6  : T1 = требуемое количество штук 2
эл.7  : M1 = место хранение номер 1
эл.8  : M2 = место хранения номер 2 
эл.9  : I1  = индекс элемента 1
эл.10 : I2  = индекс элемента 2




"""
import sqlite3 as sq#импортирую библиотеку для работы с sqlite
from tkinter import *# импортирую библиотеку для окон
from constructor import *# класс для создангие удобного интерфейса

root = None

conn = None 
cursor = None
paste = [()]
save_list = []
save_list_data = []### НАЧАЛЬНАЯ ИНИЦИАЛИЗАЦИЯ ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ
index_last = 0
index_height = 110
deleteTF = False
one = None
i_data_day = 800





def add():#функция добавленя записей
    def Save():
        global save_list
        global index_last
        save_list.append(entry1.save_entry())#>
        save_list.append(entry2.save_entry()) #
        save_list.append(entry3.save_entry()) #собираю информацию со всех полей ввода
        save_list.append(entry4.save_text()) #>
        #инициализирую список содержащий вводную информацию
        paste = [(save_list[0],save_list[1],save_list[2],index_last,save_list[3])]
        SV = save_list
        #проверка на подлиность данных
        if len(SV[0]) > 0 and len(SV[1]) and len(SV[2]) > 0 and len(SV[3]) > 0:
            sql = "INSERT INTO OBVIinf VALUES (?,?,?,?,?)"
            cursor.executemany(sql,paste)
            sql = "INSERT INTO dat VALUES (?,?,?,?,?,?,?,?,?,?)"
            for elm in range(365):
                paste = (["None","None","None","None","None","None","None","None",index_last,elm,],)
                cursor.executemany(sql,paste)
            conn.commit()

            entry1.clear_entry()
            entry2.clear_entry()
            entry3.clear_entry()
            entry4.clear_text()
            save_list = []
            paste = [()]
        else:
            #и если данные не подленные
            tree.send_label("Информация `не заполнена!",60,450)
        #очищаем все вставки
        save_list = []
        paste = [()]
        index_last += 1
        update()
        
    #создание самого окна добавления
    root_add = Tk()
    root_add["bg"] = "#03899c"
    root_add.geometry("700x500")
    root_add.title("Добавлене объекта")
    tree = instruments(root_add)
    entry1 = instruments(root_add)
    entry2 = instruments(root_add)
    entry3 = instruments(root_add)
    entry4 = instruments(root_add)
    entry1.send_entry(150,100,20)
    entry2.send_entry(150,150,20)
    entry3.send_entry(150,200,20)
    entry4.send_text(400,100,35,20)
    entry1.send_label("Оборудование:",20,100)
    entry2.send_label("Наименование:",20,150)
    entry3.send_label("Вид работы:",20,200)
    entry4.send_label("Информация",470,70)
    tree.send_button("Сохранить",60,400, lambda: Save())



def delete_btn():#функция перенаправления, помогающая удалить запись
    global deleteTF
    one.send_label("Кликните на объект который хотите удалить",500,770)
    deleteTF = True
   

def func_add(add_list,height,indexs):#функция сихронного заполнение окна данными
    index = 10
    for i in range(len(add_list)):
        one.send_button(add_list[i],index,height, lambda : open_inf(indexs))
        index += 250

def open_inf(index):#функция просмотра данных о объекте
    global deleteTF
    global update
    if deleteTF == True:
        sql = "DELETE FROM OBVIinf WHERE I = "+str(index)
        cursor.execute(sql)
        conn.commit()
        sql = "DELETE FROM dat WHERE I1 ="+str(index)
        cursor.execute(sql)
        conn.commit()
        deleteTF = False
        one.delete_label()
        update()
    else:
        sql = "SELECT * FROM OBVIinf WHERE I=?"
        cursor.execute(sql, [(index)])
        info = cursor.fetchall()
        root_info = Tk()
        root_info["bg"] = "#03899c"
        root_info.title("Информация")
        root_info.geometry("500x500")
        four = instruments(root_info)
        four.send_label("Информация о объекте '"+str(info[0][0])+"':",10,10)
        four.send_label(info[0][4],10,50)
    

def update():#функция обновления данных
    global one
    global root
    global start
    global fulls
    global index_height
    global deleteTF
    global start_paint
    index_height = 110
    deleteTF = False
    one.clear_window()
    start()
    fulls()
    start_paint()



    

def save_sql(otdel, cto, indexs, indexs2):
    global cursor
    global conn
    def_sql = "UPDATE dat SET "+otdel+" = '"+str(cto)+"'"+"\nWHERE I1 = "+str(indexs)+" AND I2 = "+str(indexs2)
    cursor.execute(def_sql)
    conn.commit()
def data_inf(indexs,indexs2):# функция просмотра сведений о дате
    global save_list_data
    global save_sql
    add_data_root = Tk()# русую окно
    add_data_root["bg"] = "#03899c"# устанавливаю цвет заднего фона
    add_data_root.geometry("1200x600")# выставляю размер окна
    five = instruments(add_data_root)# присваеваю переменой "five" конструктор 
    sql = "SELECT rowid, * FROM OBVIinf ORDER BY I"# создаю sql запрос
    for row in cursor.execute(sql):# здесь нахожу информацию о дате на которую нажали
        if row[4] == indexs:
            element = row
            break
    five.send_label("Элемент:",10,10)
    five.send_label(element[1],70,10)
    five.send_label("Ответственный:",10,40)
    five.send_label("Статус:",10,80)
    five.send_radio(["запланирована","в работе","назначене","выполнена"],20,130)
    five.send_label("Необходимый инвентарь:", 10,300)
    five.send_label("Наименование:",10,320)
    five.send_label("Требуемое кол-во штук:",200,320)
    five.send_label("Место хранения:", 410,320)
    five.send_button("Сохранить",260,570,lambda: save_data())
    FE1 = instruments(add_data_root)
    FE2 = instruments(add_data_root)
    FE3 = instruments(add_data_root)
    FE4 = instruments(add_data_root)
    FE5 = instruments(add_data_root)
    FE6 = instruments(add_data_root)
    FE7 = instruments(add_data_root)
    FE1.send_entry(140,40,20)#ответственный
    FE2.send_entry(10,340,20)#наименование 1
    FE3.send_entry(10,360,20)#наименование 2
    FE4.send_entry(200,340,20)#требуемое кол-во штук 1
    FE5.send_entry(200,360,20)#требуемое кол-во штук 2
    FE6.send_entry(410,340,20)#место хранения 1
    FE7.send_entry(410,360,20)#место хранения 2
    sql = "SELECT rowid, * FROM dat ORDER BY I1"
    send_status = ""
    for row in cursor.execute(sql):
        if row[9] == indexs and row[10] == indexs2:
            five.send_label("ОТВЕТСТВЕННЫЙ:",900,20)
            five.send_label(row[1],1100,20)
            if row[2] == "0":
                send_status = "Запланирована"
            if row[2] == "1":
                send_status = "В работе"
            if row[2] == "2":
                send_status = "Назначена"
            if row[2] == "3":
                send_status = "Выполнена"
            five.send_label("СТАТУС:",900,50)
            five.send_label(send_status,1100,50)
            five.send_label("НАИМЕНОВАНИЕ №1",900,110)
            five.send_label(row[3],1100,110)
            five.send_label("НАИМЕНОВАНИЕ №2",900,140)
            five.send_label(row[4],1100,140)
            five.send_label("ТРЕБУЕМОЕ КОЛ-ВО ШТУК №1",900,170)
            five.send_label(row[5],1100,170)
            five.send_label("ТРЕБУЕМОЕ КОЛ-ВО ШТУК №2",900,200)
            five.send_label(row[6],1100,200)
            five.send_label("МЕСТО ХРАНЕНИЯ №1",900,230)
            five.send_label(row[7],1100,230)
            five.send_label("МЕСТО ХРАНЕНИЯ №2",900,260)
            five.send_label(row[8],1100,260)
    save_list_data = []
    def save_data():
        global save_list_data
        global save_sql
        global update
        save_list_data.append(FE1.save_entry())
        save_list_data.append(five.save_radio())
        save_list_data.append(FE2.save_entry())
        save_list_data.append(FE3.save_entry())
        save_list_data.append(FE4.save_entry())
        save_list_data.append(FE5.save_entry())
        save_list_data.append(FE6.save_entry())
        save_list_data.append(FE7.save_entry())
        sql = "SELECT rowid, * FROM dat ORDER BY I1"
        for row in cursor.execute(sql):
            if row[9] == indexs and row[10] == indexs2:
                element_data = row
                break
        save_sql("O",save_list_data[0],indexs,indexs2)
        save_sql("S",save_list_data[1],indexs,indexs2)
        save_sql("N1",save_list_data[2],indexs,indexs2)
        save_sql("N2",save_list_data[3],indexs,indexs2)
        save_sql("T1",save_list_data[4],indexs,indexs2)
        save_sql("T2",save_list_data[5],indexs,indexs2)
        save_sql("M1",save_list_data[6],indexs,indexs2)
        save_sql("M2",save_list_data[7],indexs,indexs2)
        update()
        
        paste = ([save_list_data[0],str(save_list_data[1]),save_list_data[2],save_list_data[3],
                  save_list_data[4],save_list_data[5],save_list_data[6],save_list_data[7],indexs,indexs2,],)


def fulls_data(indexs,indexs2,height,i_data_day,color_bg):# функция отрисовки плашек дат
    if color_bg == "0":      #
        back_color = "#3216B0"#
    elif color_bg == "1":     #
        back_color = "#FC0107"#
    elif color_bg == "2":     #
        back_color = "#FECE01"# Здесь выбирается цвет даты в зависимости-
    elif color_bg == "3":     #-что от того, что нашлось в базе данных на эту плашку
        back_color = "#1DD201"#
    else:                     #
        back_color = "#FFFFFF"#
    # рисование плашки
    one.send_canvas_button("  ", i_data_day, height, lambda : data_inf(indexs,indexs2),back_color)
    i_data_day += 90# увеличение отрисовки по X-
                    #-для того чтобы следующая дата-
                    #-рисовалась в новом месте

def ret_2020():
    MR = [31,29,31,30,31,30,31,31,30,31,30,31]
    WK = ["Ср","Чт","Пт","Сб","Вс","Пн","Вт"]
    week = 0
    ret_result_2020 = []
    for month in range(len(MR)):
        for days in range(MR[month]):

            if len(str(month+1)) > 1:#
                str_month = str(month+1)#
            else:                        #
                str_month = "0"+str(month+1)#Здесь я отбираю ставить ли "0" перед датой или нет
            if len(str(days+1)) > 1:       #
                str_days = str(days+1)    #
            else:                         #
                str_days = "0"+str(days+1)#

            ret_result_2020.append(str_month+"."+str_days+".20"+" "+WK[week])
            week += 1
            if week >= 7:
                week = 0
    return ret_result_2020



def paint_dates_2020():#эта функция нужна для открисовки названия дат
    global one
    global ret_2020
    list_dates = ret_2020()
    x_dates_paint = 800

    for text_data in list_dates:
        one.send_canvas_text(text_data,x_dates_paint,70)
        x_dates_paint += 90

def start():#функция выставления canvas-а и прикрепление к нему окна
    global one
    one = instruments(root)
    one.send_canvas()

def start_paint():#эта функция нужна для начального заполнения окна 
    global one    #компонентами
    global paint_dates_2020
    one.send_label("Оборудование",30,60)# надпись "Оборудование" на окне
    one.send_label("Наименование",280,60)# надпись "наименование" на окне
    one.send_label("Вид работы",490,60)# надпись "Вид работы" 
    one.send_button("Добавить",10,10,lambda: add())# кнопка "добавить"
    one.send_button("Обновить",80,10,lambda: update())# кнопка "обновить"
    one.send_button("Удалить",150,10,lambda: delete_btn())# кнопка кнопка удалить
    one.add_scrollH()# добавление колеса прокрутки
    paint_dates_2020()# функция прорисовки названия дат

def fulls():#функция заполнения-присваивания индексов элементам

    """

    Эта функция очень важная и одна из сложнейших, она собирает в себя практически все функции программы.

 
    """
    global one
    global index_last
    global index_height
    global fulls_data
    global i_data_day

    i_data_day = 800# переменная отвечающая за место отрисовки дат по X-су
    sql = "SELECT rowid, * FROM dat ORDER BY I1"# здесь формируется sql запрос к базе данных  
    year = 0# эта переменная нужная для перехода на новую строку при прорисовке дат
    for row in cursor.execute(sql):# здесь проходим по базе данных
        fulls_data(row[9],row[10],index_height,i_data_day,row[2])# вызываю метод отрисоки дат
        i_data_day += 90# здесь сдвигаю отрисовку дат вправо
        year += 1# эта переменная нужна для перехода на новую высоту-
                 #-после окончания отрисовки дат для года
        if year > 365:# если уже код отрисовали то переходим на новую строку и делаем все с начала 
            i_data_day = 800# возвращае отрисовку по осе X
            year = 0# превращаем "year" в ноль для того чтобы код начался с начала
            index_height += 50# возвращаем отрисовку по осе Y

    one.send_big_label(0,0,100,51)# рисуем плашку на заднем фоне окна-
                                  #-для того чтобы при прокрутке дат-
                                  #-их плашка закрывала, и они не сливались с компонентами
    sql = "SELECT rowid, * FROM OBVIinf ORDER BY I"# формируем sql запрос для базы данных
    index_height = 110# возвращаем отрисовку по осе X в начальное положение 
    for row in cursor.execute(sql):# проходим по базе данных компонентов
        func_add([row[1],row[2],row[3]],index_height,row[4])# функция отрисовки компонентов
        index_last = row[0]# выставляем последний индекс для последующего занесения его в базу данных
        index_height += 50# увеличаем отрисовку по осе X




        

def run():# функция для запуска из другой программы.-
          #-можно просто вызвать эту функцию из другой программы-
          #-и запуститься вся эта программа 
    global start
    global fulls
    global root
    global cursor
    global conn
    global paste
    global save_list
    global save_list_data
    global deleteTF
    global one
    global i_data_day
    global index_height
    global index_last

    root = Toplevel()#создаю окно
    root["bg"] = "#03899c"
    root.geometry("1200x800")#размером 1200x800
    root.title("Пользовательское окно")
    conn = sq.connect("info.db") #присоединяеюсь к локальной дазе данных
    cursor = conn.cursor()#создаю элемент управления-редактирования базой данных
    paste = [()]#создаю глобальную переменную вставки в базу данных
    save_list = []#список полученных данных
    save_list_data = []#список полученный данных для дат
    index_last = 0#последний индекс элемента
    index_height = 110#индекс размещания объектов
    deleteTF = False#переменная отвечающая за удаление записей
    i_data_day = 800
    start()
    fulls()
    start_paint()
    root.mainloop()#запускаем окно




