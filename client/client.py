import socket
from tkinter import *
from constructor import *
def PTS_run():
    get_ip_root = Tk()
    get_ip_root.geometry("215x120")
    get_ip_root.title("Впишите IP сервера")
    GIP = instruments(get_ip_root)
    GIP.send_label("Впишите IP сервера",20,20)
    GIP.send_entry(20,50,30)
    GIP.send_button("Начать прием",20,80,lambda: run_client(GIP.save_entry()))
def run_client(IP):
    sock = socket.socket()
    sock.connect((IP,9090))
    list_bytes = []
    mass_str = ""
    while True:
        data = sock.recv(20048)  
        if not data:
            massL = list(mass_str)
            paste = ""
            for i in range(len(massL)):
                if massL[i] != "/":
                   paste += massL[i]
                else:
                   list_bytes.append(int(paste))
                   paste = ""
                print(i,"/",len(massL))                  
            print("файл передан, прием заканчивается")
            file = open("info.db","wb")
            file.write(bytes(list_bytes))
            file.close()
            break  
        mass_str += data.decode("utf-8")

    



    
"""   
def PTS_run():
    file = open("info.db","rb")
    file_read = file.read()
    file.close()
    file_readS = (str(file_read))
    file_readL = list(file_readS)
    a = ""
    
    
    file = open("new_info.db","wb")
    file.write(file_readS) 
    file.close()
    
def PTS_run():
    UPD_PORT = 5005
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(("",UPD_PORT))
    list_bytes = []
    
    
    while True:
        sock.settimeout(10.0)
        try:
            data = sock.recv(2048)
        except(BaseException):
            print("файл передан, прием заканчивается")
            file = open("info.db","wb")
            file.write(bytes(list_bytes))
            file.close()
            break
        list_bytes.append(len(list(data.decode("utf-8"))))
        print(data)
        print("AsdasdA")
    
    
    
    
    
    
"""


    
