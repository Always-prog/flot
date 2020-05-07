from constructor import *
from data import run as runD
from dont_works import run as runDW
from client import PTS_run
start_root = Tk()
ST = instruments(start_root)
ST.send_canvas()
ST.send_canvas_text("Выбирите действие",50,50)
ST.send_canvas_button("Даты",60,100, lambda: runD())
ST.send_canvas_button("Журнал неисправностей",200,100, lambda: runDW())
ST.send_canvas_button("принять базу данных",100,200,lambda: PTS_run())
start_root.mainloop()

