import sqlite3 as sq#импортирую библиотеку для работы с sqlite
from tkinter import *# импортирую библиотеку для окон
from tkcalendar import *
from PIL import ImageTk, Image


class instruments():# создаю класс на основе которого будет 
                    # создаватся интерфейс
    def __init__(self,root):
        self.root = root #инициализация окна
        self.calen = None

    def send_canvas(self,bg="#03899c",scrollR=[0,0,35000,35000]):
        self.canvas = Canvas(self.root,bg=bg,scrollregion=scrollR)
        self.canvas.pack(side=LEFT, fill="both",expand=True)


    def send_button(self,btn_label,x,y,click=None,bg="#00727d"):#функция добаления кнопок
        self.btn = Button(self.root,text=btn_label, bg=bg,font="Courier 8",command=click)
        self.btn.place(x=x,y=y)
    def send_canvas_button(self,btn_label,x,y,click=None,bg="#00727d"):
        self.Cbtn = Button(self.root,text=btn_label, bg=bg,font="Courier 8",command=click)
        self.canvas_widget = self.canvas.create_window(x+25, y+10, window=self.Cbtn)       

    def send_label(self,labels,x,y):#функция добавления надписей
        self.lab = Label(self.root,text=labels,bg="#03899c",fg="#FFFFFF",font="Courier 8")
        self.lab.place(x=x,y=y)
    def send_canvas_text(self,labels,x,y):
        self.Clab = self.canvas.create_text((x+25,y+10),text=labels)


    def delete_label(self):#функция удаления надписей
        self.lab.grid_remove()

    def send_entry(self,x,y,width=20):#функция создания поля ввода
        self.entr = Entry(self.root,width=width,bg="#498AAB")
        self.entr.place(x=x,y=y)
    def save_entry(self):#функция возврата написанного в поле ввода
        return self.entr.get()
    def clear_entry(self):#функция очистки поля ввода
        self.entr.delete(0,END)

    def send_text(self,x,y,width=30,height=40):#функция добавления поля ввода для 
                                               #объемного текста
        self.text = Text(self.root,width=width,height=height,bg="#498AAB",font="Courier 8")
        self.text.place(x=x,y=y)
    def save_text(self):#функция получения данных из объемного поля ввода
        return self.text.get(1.0,END)
    def clear_text(self):#функция очиски поля ввода
        self.text.delete(1.0,END)
    def quit(self):#функция насильного закрытия окна
        self.root.destroy()
    def clear_window(self):#функция очистки окна от всех компонентов
        for w in self.root.winfo_children():
            w.destroy()
    def add_scrollH(self,orient="horizontal"):#функция добавленя ползунка на окно
        self.scroll = Scrollbar(self.canvas,orient=orient)
        self.canvas.config(xscrollcommand=self.scroll.set)
        self.scroll.config(command=self.canvas.xview)
        self.scroll.pack(side=BOTTOM,fill=X)    

    def add_scrollV(self,orient="vertical"):#функция добавленя ползунка на окно
        self.scroll = Scrollbar(self.canvas,orient=orient)
        self.canvas.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.canvas.yview)
        self.scroll.pack(side=RIGHT,fill=Y)

    def send_radio(self,list_names,x,start_y):
        self.Rbuttons = []
        self.var = IntVar(self.root)
        self.var.set(0)
        for BtnR in range(len(list_names)):
            Radiobutton(self.root,text=str(list_names[BtnR]),variable=self.var, value=BtnR, command=self.select_radio)\
            .place(x=x,y=start_y)
            start_y += 40
    def save_radio(self):
        return self.var_get
    def select_radio(self):
        self.var_get = self.var.get()

    def send_calendar(self,master):
        self.calen = Calendar(master=master)
        self.calen.pack()
        self.calen_result = self.calen.selection_get()
    def save_calendar(self):
        return self.calen_result

    def send_menu(self,lists,x,y):
        self.StrVar = StringVar(self.root)
        self.StrVar.set(lists[0])
        self.menu = OptionMenu(self.root, self.StrVar, *lists)
        self.menu.place(x=x,y=y)
    def save_menu(self):
        return self.StrVar.get()
    def send_big_label(self,x,y,w,h,bg="#03899c"):
        self.big_lab = Label(self.root,bg=bg,width=w,height=h)
        self.big_lab.place(x=x,y=y)

