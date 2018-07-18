from socket import AF_INET , socket, SOCK_STREAM
from threading import Thread
import tkinter
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list. insert(tkinter.END,msg)
        except OSError : # Possibly client has left the chat
            break
def send(event =  None):
    msg = my_msg.get()
    my_msg.set("") #clears input field
    client_socket.send(bytes(msg , "utf8"))
    if msg =="(quit)":
        client.socket.close()
        top.quit()

def on_closing(event = None):
    my_msg.set("(quit)")
    send()
top = tkinter.Tk()
top.title("Chatter")
messages_frame = tkinter.Frame(top)
my_msg= tkinter.StringVar() #For massages to be sent
my_msg.set("Type your message here.")
scrollbar = tkinter.Scrollbar(messages_frame) #navigation through past messages

msg_list = tkinter.Listbox(messages_frame, height = 15 , width = 50 , yscrollcommand = scrollbar.set)
scrollbar.pack(side= tkinter.RIGHT,fill = tkinter.Y)
msg_list.pack(side = tkinter.LEFT, fill = tkinter.BOTH)

messages_frame.pack()
entry_field  = tkinter.Entry(top , textvariable = my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text = "Send" , command =send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)


HOST = input('Enter host: ')
PORT = input("Enter port: ")

if not PORT:
    PORT = 3000
else:
    PORT = int(PORT)

if not HOST:
    HOST = "127.0.0.1"
else:
    HOST = int(HOST)

BUFSIZ = 1024
ADDR = (HOST,PORT)
client_socket= socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)


receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() #starts GUI
