import socket                                                           # Import Sockets
from threading import Thread                                            # Import Threading
from socketserver import ThreadingMixIn                                 # Import socketserver from threadingmixin
import pyinputplus as pp                                                # Import pyinputplus for validation

class ClientThread(Thread):                                             # Create Client
    def __init__(self,ip,port):                                         # Create a function within the class to set port and IP list new clients
        Thread.__init__(self)
        self.ip = ip                                                    # Store client IP
        self.port = port                                                # Store client port
        print("[+] New socket started for " + ip + ":" + str(port))     # List connect client with IP & Port

    def run(self):                                                      # What is sent to or recived from the client
        while True:                                                     # While loop to make the session until close
            s.send(b"Hello!\n")                                         # Send Basic Message
            s.close()                                                   # Close connection
            break                                                       # Break the loop

TCP_IP = pp.inputIP("Enter the server IP address: ")                    # Obtain and sanitize for the IP
TCP_PORT = pp.inputNum(prompt='Enter server port: ', min=1, max=65353)  # Obtain and sanitize for port

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creating the socket
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         # Set Socket
tcpServer.bind((TCP_IP, TCP_PORT))                                      # Bind the server port and IP
threads = []                                                            # Create a list of threads

while True:                                                             # Created an infinite while loop
    tcpServer.listen(4)                                                 # Start server Listener
    print("Waiting for a connection to",TCP_IP,"at",TCP_PORT,"...")     # Output server status with IP and Port
    (s, (ip,port)) = tcpServer.accept()                                 # Accept a new client
    newthread = ClientThread(ip,port)                                   # Create a new thread
    newthread.start()                                                   # Start new thread
    threads.append(newthread)                                           # Add new thread to list of threads

for t in threads:                                                       # for loop of number of given number threads
    t.join()                                                            # join new thread, this is how multi threadding is done
