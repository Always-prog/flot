import socket
from time import sleep



def PTS_run():


    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print ('connected:', addr)

    file = open("info.db","rb")
    file_read = file.read()
    file.close()

    for i in file_read:
        i = str(i)+"/"
        conn.send(bytes(str.encode(str(i))))
        print(bytes(i.encode("utf-8")))
    conn.close()







        

   

    
"""
    
def PTS_run():
    global with_end
    UPD_PORT = 5005
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.connect(("192.168.137.213",5005))

    file = open("info.db","r",encoding="charmap")
    file_read = file.read()
    file.close()
    file_read = list(file_read)
    for sends in file_read:
        sock.send(bytes(sends.encode("charmap")))
        with_end += sends
        print(sends)
        sleep(1/1000)




        
def PTS_run():



    file = open("info.db","rb")
    file_read = file.read()
    file.close()
    list_bytes = []
    list_con = []

    for i in file_read:
        g = bytes(i)
        list_bytes.append(i)
        list_con.append(len(g.decode("utf-8")))
    file = open("new_info.db","wb")
    file.write(bytes(list_con))
    file.close()

PTS_run()
   






"""
