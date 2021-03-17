import socket                                                           # Import Sockets
from threading import Thread                                            # Import Threading
from socketserver import ThreadingMixIn                                 # Import socketserver from threadingmixin
import pyinputplus as pp                                                # Import pyinputplus for validation
import datetime                                                         # Imports date time for status updates
import nmap3                                                            # This is for scannign through nmap
import os                                                               # Imports OS for cd and command execution
import json                                                             # For formatting json
from shodan import Shodan                                               # For passive scanning through Shodan

# SPYython Ascii Art
asciiart=b"""
                                          .,cdk0XNNNK0xo:.
                                       .;d0WMMNK0OkO0XWMWNOl'
                                     .c0WMWKdc,. .;od:;lkXWMXx;
                                   .c0WMNx;.      .,k0o. .cOWMNk,
                                  ,kWMNx,           .,k0o. .:0WMXo.
                                 cXMW0;          .;ox,.,x0o. .oXMWO,
                               .dNMNx.             .o0x,.,k0o. ;0WMK:
                              .kWMXl.             ....o0x,.,x0o''kWMXl
                             .OWMX:              .,okc..o0x,.,x0o;xNMNo.
                            .OWMK;                 .:kOc..o0x;.,x0k0WMNo.
                           .OWMK;                 .'..:kOc..o0x;.,xXWMMNo
                          .kWMK:                 .,o0d'.:kOc..o0k;.,xNMMNl             \033[40m\033[1;34mWelcome to SPYthon!\033[40m\033[0m
                         .xWMX:                 .. .:OKd'.:kOc..oOk;.,OWMXc
                        .oWMNl  ..';:clodxkkOO0000000KWMXOxONW0o:lOXk;'kWMK;
                        lNMW0ook0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMNkxNMM0'
                       :XMMMMMMMMMMMWXKKKKKKKKKKKKKKKKKKKKKKKKKNMMMMMMMMMMMWk.
                      ,0MMMMMMMMMMMMx'.........................:KMMMMMMMMMMMWd.
                     .xMMMMMMMMMMMMMk.           .:;.          :XMMMMMMMMMMMMN:
                     .dWMMMMMMMMMMMMNc           .;xd.        .kMMMMMMMMMMMMMX;
                      .xNMMMMMMMMMMMM0'          ..lx,        lNMMMMMMMMMMMMXc
                        :0WMMMMMMMMMMWx.                     ;KMMMMMMMMMMMNx'
                         .c0WMMMMMMMMMWo.                   '0MMMMMMMMMMNx,
                          .oXMMMMMMMMMMNx'                .:0MMMMMMMMMMM0;
                       .;dKWMMMMMMMMMMMMMNOl;..       .':dKWMMMMMMMMMMMMMNOl,
                    .;dKWMMMMMMMMMMMMMMMMMMMWX0kdoooxOKNMMMMMMMMMMMMMMMMMMMMNOl'
                  ;dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl'
                ,ONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd.
               cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,
              cNMMMMMXdlllllccllllllllllllllcclllllllllllllllllllllllllllcclllkWMMMMMO'
             ;KMMMMMMx.                                                       ;KMMMMMWx.
            'OMMMMMMMk.                                                       ;XMMMMMMWo
           .xWMMMMMMMk.                       \033[40m\033[1;31m{}{}{}{}\033[40m\033[0m                        :NMMMMMMMXc
           oWMMMMMMMMO.                    \033[40m\033[1;31m{}{}{}{}{}{}{}\033[40m\033[0m                     :NMMMMMMMMK,
          :XMMMMMMMMM0'                  \033[40m\033[1;31m{}{}{}{}{}{}{}{}{}\033[40m\033[0m                   cWMMMMMMMMMO.
         ,KMMMMMMMMMMK,                 \033[40m\033[1;31m{}{}{}{}{}{}{}{}{}{}\033[40m\033[0m                  lWMMMMMMMMMWx.
        .OMMMMMMMMMMMK,                \033[40m\033[1;31m{}{}{}{}{}{}{}{}{}{}{}\033[40m\033[0m                 oMMMMMMMMMMMNl
        oWMMMMMMMMMMMX;                \033[40m\033[1;31m{}{}{}{}{}{}{}{}{}{}{}\033[40m\033[0m                 dMMMMMMMMMMMMK;
       '0MMMMMMMMMMMMX;                \033[40m\033[1;31m{}       {}{}       {}\033[40m\033[0m                 dMMMMMMMMMMMMMo
       ,KMMMMMMMMMMMMN:                 \033[40m\033[1;31m{}     {}{}{}     {}\033[40m\033[0m                 .xMMMMMMMMMMMMMx.
       .OMMMMMMMMMMMMWc                  \033[40m\033[1;31m{}{}{}{}{}{}{}{}{}\033[40m\033[0m                  .kMMMMMMMMMMMMWo
        cNMMMMMMMMMMMWl                  \033[40m\033[1;31m{}{}{}/ || \{}{}{}\033[40m\033[0m                  .kMMMMMMMMMMMM0'
         lNMMMMMMMMMMMo                  \033[40m\033[1;31m{}{}{}{}{}{}{}{}{}\033[40m\033[0m                  .OMMMMMMMMMMM0,
          ;0WMMMMMMMMMo                      \033[40m\033[1;31m{}{}{}{}{}\033[40m\033[0m                      '0MMMMMMMMMNx.
           .oXMMMMMMMMd                       \033[40m\033[1;31m{}{}{}{}\033[40m\033[0m                       '0MMMMMMMW0:.
            OXMMMMMMMMx.                                                     ,KMMMMMMMW
              NNNWMMMMO;.....................................................lXMMMMW/`
                ':OWMMWNNNNNNNNNNXNXXXNXXXNNNNXNNNXXNNNNNNNNNNNNNNNNNNNNNNNXNNMMMNx;
                  .OMMN0kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkKWMWo
                  .xMMKl,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,xWMN:
                   dMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMX;
                   ;KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNx.     
"""

class ClientThread(Thread):                                             # Create Client
    def __init__(self,ip,port):                                         # Create a function within the class to set port and IP list new clients
        Thread.__init__(self)
        self.ip = ip                                                    # Store client IP
        self.port = port                                                # Store client port
        # Prints new socket info with date time and client IP's
        print(datetime.datetime.now(),"\033[40m\033[1;32m[+] New socket started for " + ip + ":" + str(port),"\033[40m\033[0m")
    def run(self):                                                      # What is sent to or recived from the client
        while True:                                                     # While loop to make the session until close
            s.send(asciiart)                                            # Prints Ascii Art
            # Sends data asking for the client to give an IP to scan
            s.send(bytes("\n Hello "+ip+"!\n"+"What would you like to scan?: ", 'utf-8'))
            result=s.recv(SOCKET_BUFFER_SIZE)                           # Recieves user's data and stores it
            UserIn = str(result.decode('utf-8').rstrip("\n"))           # Formats user's sent data
            # Prints status of scan starting with datetime
            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Active Scan of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            nm = nmap3.Nmap()                                           # Sets nm = to the nmap function
            nmapDict = nm.scan_top_ports(UserIn)
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] Active Scan of",str(UserIn)," finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            json_object = json.dumps(nmapDict, indent = 4)              # Format json objects from nmapDict
            # Sets file for active scan
            activeScan = "ScanOutput-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"-Active_Scan-"+str(UserIn)+".json"
            f = open(activeScan, "w")                                   # Open new text file for active scan
            f.write(str(json_object))                                   # Write text file from json_object
            f.close()                                                   # Close File
            s.send(bytes("View file at: "+"http://"+str(TCP_IP)+":"+str(WEB_PORT)+"/"+str(activeScan)+"\n", 'utf-8'))

            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Passive Scan of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            api = Shodan(SHODAN_API_KEY)                                # Set api key
            passiveOut = api.host(UserIn)                               # Run the shodan scan
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] Passive Scan of",str(UserIn)," finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            json_object = json.dumps(passiveOut, indent = 4)            # Format json objects from Shodan Output
            # Sets file for passive scan
            passiveScan = "ScanOutput-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"-Passive_Scan-"+str(UserIn)+".json"
            f = open(passiveScan, "w")                                  # Open new text file for passive scan
            f.write(str(json_object))                                   # Write text file from json_object
            f.close()                                                   # Close File
            s.send(bytes("View file at: "+"http://"+str(TCP_IP)+":"+str(WEB_PORT)+"/"+str(passiveScan)+"\n", 'utf-8'))   # Returns scan data to user
            # Prints status of finished scan
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] Scan of",UserIn," saved to file and link was sent to client " + ip + ":" + str(port),"\033[40m\033[0m")
            s.close()                                                   # Close connection
            # Print the status of the closed connection
            print(datetime.datetime.now(),"\033[40m\033[1;31m[-] client " + ip + ":" + str(port), "left the server","\033[40m\033[0m")
            break                                                       # Break the loop

# TCP_IP = "0.0.0.0"                                                    # Hardcoded IP to host server on all nics
# TCP_PORT = 1337                                                       # Harded port 1337
SOCKET_BUFFER_SIZE = 4096                                               # Set socket buffer size

TCP_IP = pp.inputIP("Enter the SPYthon IP address: ")                    # Obtain and sanitize for the IP
TCP_PORT = pp.inputNum(prompt='Enter the SPYthon server port: ', min=1, max=65353)  # Obtain and sanitize for Server port
WEB_PORT = pp.inputNum(prompt='Enter the web server port: ', min=1, max=65353)      # Obtain and sanitize for Web Port
SHODAN_API_KEY = pp.inputStr(prompt='Enter Your SHODAN API KEY: ')      # Obtain Shodan Key

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creating the socket
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         # Set Socket
tcpServer.bind((TCP_IP, TCP_PORT))                                      # Bind the server port and IP
threads = []                                                            # Create a list of threads

# Print Status of the connection with start datetime and server IP and Port Info
print("\n"+str(datetime.datetime.now()),"\033[40m\033[1;34m[*]Waiting for a connection to SPYthon at ",TCP_IP,"at",TCP_PORT,"...\033[40m\033[0m")

web_dir = os.path.join(os.path.dirname(__file__), 'web')                # Sets path to web server
os.chdir(web_dir)                                                       # Changes to web server directory
os.system("python3 -m http.server "+str(WEB_PORT)+" &")                 # Runs web server through os.system bc of threadding issue with running it in script

# Print Status of the web connection with start datetime and server IP and Port Info
print(str(datetime.datetime.now()),"\033[40m\033[1;34m[*]Waiting for a connection to Web Server at ",TCP_IP,"at",WEB_PORT,"...\033[40m\033[0m")                                                # Serves Web Server Forever

while True:                                                             # Created an infinite while loop
    tcpServer.listen(4)                                                 # Start server Listener     # Output server status with IP and Port
    (s, (ip,port)) = tcpServer.accept()                                 # Accept a new client
    newthread = ClientThread(ip,port)                                   # Create a new thread
    newthread.start()                                                   # Start new thread
    threads.append(newthread)                                           # Add new thread to list of threads

for t in threads:                                                       # for loop of number of given number threads
    t.join()                                                            # join new thread, this is how multi threadding is done
