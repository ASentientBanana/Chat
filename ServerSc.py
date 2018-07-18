#Server script
from socket import AF_INET, socket , SOCK_STREAM
from threading import Thread
clients = {}
adresses = {}

HOST = '127.0.0.1'
PORT = 3000
BUFSIZ = 1024
ADDR = (HOST,PORT)
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_conections():
    while True:
        client,client_address = SERVER.accept()
        print("%s:%s has connected." % client_address  )
        client.send(bytes("Greetings " + " Now type your name and press ENTER!", "utf8"))
        adresses[client] = client_address
        Thread(target= handle_client, args = (client,)).start()

def handle_client(client): #takes client socket as argument
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s ! if you ever want to quit , type (quit) to exit' % name
    client.send(bytes(welcome,"utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg,"utf8"))
    clients[client] = name
    while True:
        
        msg = client.recv(BUFSIZ)
        if msg != bytes("(quit)","utf8"):
            broadcast(msg,name+": ")
        else:
            client.send(bytes("quit", "utf8"))
            client.close()
            del clientsp[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

            
def broadcast(msg,prefix =""):#prefix is for the name identification
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection ... ")
    ACCSEPT_THREAD = Thread(target=accept_incoming_conections)
    ACCSEPT_THREAD.start()
    ACCSEPT_THREAD.join()
    SERVER.close()


