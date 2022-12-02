import socket                                                           # Import Sockets
from threading import Thread                                            # Import Threading
from socketserver import ThreadingMixIn                                 # Import socketserver from threadingmixin
import pyinputplus as pp                                                # Import pyinputplus for validation
import datetime                                                         # Imports date time for status updates
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
    def run(self):                                                      # What is sent to or received from the client
        while True:                                                     # While loop to make the session until close
            s.send(asciiart)                                            # Prints Ascii Art
            # Sends data asking for the client to give an IP to scan
            s.send(bytes("\n Hello "+ip+"!\n"+"What would you like to scan?: ", 'utf-8'))
            result=s.recv(SOCKET_BUFFER_SIZE)                           # Receives user's data and stores it
            UserIn = str(result.decode('utf-8').rstrip("\n"))           # Formats user's sent data
            # Prints status of scan starting with datetime                                              # Close File

            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Passive Scan of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            shodan_api = Shodan(SHODAN_API_KEY)                                # Set api key
            passiveOut = shodan_api.host(UserIn)                               # Run the shodan scan
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] Passive Scan of",str(UserIn)," finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            jsonPassive = json.dumps(passiveOut, indent = 4)            # Format json objects from Shodan Output
            f = open(passiveScan, "w")                                  # Open new text file for passive scan
            f.write(str(jsonPassive))                                   # Write text file from json_object
            f.close()

            headers = { "x-api-key" : CRIMINALIP_API_KEY }
            print(requests.get("https://api.criminalip.io/v1/ip/data?ip="+UserIn+"full=true", headers=headers, verify=False).text) # Criminalip Raw Data

            HTMLFile = "Report-"+datetime.datetime.now().strftime("%Y%m%d%H%M")+"-"+str(UserIn)+".html"
            location = str(passiveOut["city"])+", "+str(passiveOut["region_code"])+" "+str(passiveOut["country_name"])
            whois = os.popen(f'whois {UserIn}').read().replace('\n', '<br>')
            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Active Scan of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            services = os.popen(f'nmap -sV {UserIn}').read().replace('\n', '<br>')
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] Active Scan of",str(UserIn)," finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] VirusTotal of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            virustotal = os.popen(f"curl --request GET --url 'https://www.virustotal.com/vtapi/v2/url/report?apikey={VIRUSTOTAL_API_KEY}&resource={UserIn}'").read().replace('\n', '<br>')
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] VirusTotal of",str(UserIn)," finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            shodanDump = ""
            dataOut = passiveOut['data']
            for i in range(len(dataOut)):
                shodanDump=shodanDump + str(dataOut[i]['data'])
            shodanDump = shodanDump.replace('\n', '<br>')

            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Dig of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            dig = os.popen(f'dig -x {UserIn}').read().replace('\n', '<br>')
            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Dig of",str(UserIn),"finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Traceroute of",str(UserIn),"started for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            traceroute = os.popen(f'traceroute -m 6 {UserIn}').read().replace('\n', '<br>')
            print(datetime.datetime.now(),"\033[40m\033[1;33m[*] Traceroute of",str(UserIn),"finished for client " + str(ip) + ":" + str(port),"\033[40m\033[0m")
            html = f'''
            <!DOCTYPE html>
            <html class="no-js" lang="en">
            <head>

                <!--- basic page needs
                ================================================== -->
                <meta charset="utf-8">
                <title>SPYthon Report</title>
                <meta name="description" content="">
                <meta name="author" content="">

                <!-- mobile specific metas
                ================================================== -->
                <meta name="viewport" content="width=device-width, initial-scale=1">

                <!-- CSS
                ================================================== -->
                <link rel="stylesheet" href="css/styles.css">
                <link rel="stylesheet" href="css/vendor.css">

                <!-- script
                ================================================== -->
                <script src="js/modernizr.js"></script>
                <script defer src="js/fontawesome/all.min.js"></script>

                <!-- favicons
                ================================================== -->
                <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
                <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
                <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
                <link rel="manifest" href="site.webmanifest">

            </head>

            <body id="top">


                <!-- preloader
                ================================================== -->
                <div id="preloader">
                    <div id="loader"></div>
                </div>


                <!-- header
                ================================================== -->
                <header class="s-header">
                    <div class="row">

                        <div class="s-header__logo">
                            <a href="index.html">
                                <img src="images/logo.png" alt="Homepage">
                            </a>
                        </div>

                        <a class="s-header__menu-toggle" href="#0" title="Menu">
                            <span class="s-header__menu-icon"></span>
                        </a>

                    </div> <!-- end row -->
                </header> <!-- end s-header -->


                <!-- home
                ================================================== -->
                <section id="home" class="s-home target-section" data-parallax="scroll" data-image-src="images/bg.jpg" data-natural-width="3000" data-natural-height="2000">

                    <div class="s-home__content">

                        <div class="s-home__slider">

                            <div class="s-home__slide s-home__slide--1">
                                <div class="row">
                                    <div class="column large-12 s-home__slide-text">
                                        <h2>
                                        SPYthon Report of <span>{UserIn}</span>.
                                        </h2>
                                    </div>
                                </div>
                            </div> <!-- end s-home__slide -->

                            <div class="s-home__slide s-home__slide--2">
                                <div class="row">
                                    <div class="column large-12 s-home__slider-text">
                                        <h2>
                                        This report includes an executive summery of the all the data collected through <span>Nmap</span> Scans as well as the data from <span>Shodan</span>.
                                        </h2>
                                    </div>
                                </div>
                            </div> <!-- end s-home__slide -->

                        </div> <!-- end s-home__slider -->


                            <div class="s-home__slide s-home__slide--3">
                                <div class="row">
                                    <div class="column large-12 s-home__slider-text">
                                        <h2>
                                        This report includes an executive summery of the all the data collected through <span>Nmap</span> Scans as well as the data from <span>Criminalip</span>.
                                        </h2>
                                    </div>
                                </div>
                            </div> <!-- end s-home__slide -->

                        </div> <!-- end s-home__slider -->

                    </div> <!-- end s-home__content -->

                    <div class="s-home__nav-arrows">
                        <div class="s-home__arrow-prev">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12.707 17.293L8.414 13H18v-2H8.414l4.293-4.293-1.414-1.414L4.586 12l6.707 6.707z"/></svg>
                        </div>
                        <div class="s-home__arrow-next">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M11.293 17.293l1.414 1.414L19.414 12l-6.707-6.707-1.414 1.414L15.586 11H6v2h9.586z"/></svg>
                        </div>
                    </div> <!-- end s-home__nav-arrows -->

                    <div class="s-home__line"></div>

                </section> <!-- end s-home -->


                <!-- services
                ================================================== -->
                <section id="services" class="s-services target-section s-dark">

                    <div class="row section-head">
                        <div class="column large-3 medium-12" data-aos="fade-up">
                            <h2>Scan Results</h2>
                            <p class="desc">Here is a list of key data points collected from {UserIn}.</p>
                        </div>

                        <div class="column large-8 medium-12 align-x-right" data-aos="fade-up">
                            <p class="lead">
                            The IP:         {str(passiveOut["ip_str"])}<br>
                            The Org:        {str(passiveOut["org"])}<br>
                            The Location:   {str(passiveOut["city"])+", "+str(passiveOut["region_code"])+" "+str(passiveOut["country_name"])}<br>
                            Available Ports: {str(passiveOut["ports"])}
                            </p>
                        </div>
                    </div> <!-- end section-head -->

                    <div class="row block-large-1-3 block-medium-1-2 block-tab-full services-list">

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Whois</h5>
                            <p>
                            {whois}
                            </p>
                        </div> <!-- end services-item -->

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Nmap Service Scan</h5>
                            <p>
                            {services}
                            </p>
                        </div> <!-- end services-item -->

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Criminalip Report</h5>
                            <p>
                            {criminalipDump}
                            </p>
                        </div> <!-- end services-item -->

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Shodan Report</h5>
                            <p>
                            {shodanDump}
                            </p>
                        </div> <!-- end services-item -->

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Virustotal Report</h5>
                            <p>
                            {virustotal}
                            </p>
                        </div> <!-- end services-item -->

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Dig</h5>
                            <p>
                            {dig}
                            </p>
                        </div> <!-- end services-item -->

                        <div class="column services-item" data-aos="fade-up">
                            <h5>Traceroute</h5>
                            <p>
                            {traceroute}
                            </p>
                        </div> <!-- end services-item -->

                    </div> <!-- end services-list -->

                </section> <!-- end s-services -->

                <!-- about
                ================================================== -->
                <section id="about" class="s-about target-section">

                    <div class="row section-head">
                        <div class="column large-3 medium-12" data-aos="fade-up">
                            <h2>About SPYthon</h2>
                            <p class="desc">A brief description of the project</p>
                        </div>

                        <div class="column large-8 medium-12 align-x-right" data-aos="fade-up">
                            <p class="lead">
                            The idea for this project is to create a multi-threaded python server that will generate HTML reports on what exploits can be run against what host. First, the user will create a new session with the host and give the host an IP. Based on whether or not that IP can be scanned passively (if it exists in Shodan/Censys) it will ask the user if this is owned or allowed infrastructure to scan. If the user consents, the server will scan the host with Nmap and determine what versions the host is running and if their services are vulnerable. If the user does not approve the server will not scan the host. If the given host has already been scanned by Censys/Shodan then those results will be fed into the server via API's. The server/script will then determine if the vulnerability has a given exploit, which it will then display to the user along with the ports in a report that is in HTML format.
                            </p>
                        </div>
                    </div> <!-- end section-head -->

                     <div class="row">
                        <div class="column" data-aos="fade-up">
                            <h4>Meet The Team.</h4>
                        </div>
                    </div>

                    <div class="row block-large-1-4 block-medium-1-3 block-tab-1-2 block-500-stack team-block">

                        <div class="column team-member" data-aos="fade-up">
                            <div class="team-member__info">
                                <p class="team-member__name">
                                    Jack Zimmer
                                    <span>Developer, Project Manager</span>
                                </p>
                                <ul class="team-member__social">
                                    <li><a href="#0"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-dribbble" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div class="column team-member" data-aos="fade-up">
                            <div class="team-member__info">
                                <p class="team-member__name">
                                    Gabrielle Merriken
                                    <span>Developer, Documenter</span>
                                </p>
                                <ul class="team-member__social">
                                    <li><a href="#0"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-dribbble" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                                </ul>
                            </div>
                        </div>

                        <div class="column team-member" data-aos="fade-up">
                            <div class="team-member__info">
                                <p class="team-member__name">
                                    Christian Ekeigwe
                                    <span>Developer, Infrastructure, Bug Tester</span>
                                </p>
                                <ul class="team-member__social">
                                    <li><a href="#0"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-dribbble" aria-hidden="true"></i></a></li>
                                    <li><a href="#0"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                                </ul>
                            </div>
                        </div>

                    </div> <!-- end team-block -->

                </section> <!-- end s-about -->

                <!-- footer
                ================================================== -->
                <footer class="s-footer">
                    <div class="row">
                        <div class="column large-4 medium-6 w-1000-stack s-footer__social-block">
                            <ul class="s-footer__social">
                                <li><a href="#0"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                                <li><a href="#0"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                                <li><a href="#0"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                                <li><a href="#0"><i class="fab fa-dribbble" aria-hidden="true"></i></a></li>
                                <li><a href="#0"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                            </ul>
                        </div>

                        <div class="column large-7 medium-6 w-1000-stack ss-copyright">
                            <span>© Jack Zimmer, Gabrielle Merriken, Christian Ekeigwe 2021</span>
                        </div>
                    </div>

                    <div class="ss-go-top">
                        <a class="smoothscroll" title="Back to Top" href="#top">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 4h12v2H6zm5 10v6h2v-6h5l-6-6-6 6z"/></svg>
                        </a>
                    </div> <!-- end ss-go-top -->
                </footer>


                <!-- Java Script
                ================================================== -->
                <script src="js/jquery-3.2.1.min.js"></script>
                <script src="js/plugins.js"></script>
                <script src="js/main.js"></script>

            </body>

            </html>
            '''
            f = open(HTMLFile, "w")                                   # Open new text file for active scan
            f.write(html)                                   # Write text file from json_object
            f.close()
            s.send(bytes("Report Generated at: "+"http://"+str(TCP_IP)+":"+str(WEB_PORT)+"/"+str(HTMLFile)+"\n", 'utf-8'))
            # Prints status of finished scan
            print(datetime.datetime.now(),"\033[40m\033[1;33m[+] Scan of",UserIn," saved to file and link was sent to client " + ip + ":" + str(port),"\033[40m\033[0m")
            s.close()                                                   # Close connection
            # Print the status of the closed connection
            print(datetime.datetime.now(),"\033[40m\033[1;31m[-] client " + ip + ":" + str(port), "left the server","\033[40m\033[0m")
            break                                                       # Break the loop

# TCP_IP = "0.0.0.0"                                                    # Hardcoded IP to host server on all nics
# TCP_PORT = 1337                                                       # Hardcoded port 1337
SOCKET_BUFFER_SIZE = 4096                                               # Set socket buffer size

TCP_IP = pp.inputIP("Enter the SPYthon IP address: ")                    # Obtain and sanitize for the IP
TCP_PORT = pp.inputNum(prompt='Enter the SPYthon server port: ', min=1, max=65353)  # Obtain and sanitize for Server port
WEB_PORT = pp.inputNum(prompt='Enter the web server port: ', min=1, max=65353)      # Obtain and sanitize for Web Port
CRIMINALIP_API_KEY = pp.inputStr(prompt='Enter Your CRIMINALIP API KEY: ')      # Obtain Criminalip Key
SHODAN_API_KEY = pp.inputStr(prompt='Enter Your SHODAN API KEY: ')      # Obtain Shodan Key
VIRUSTOTAL_API_KEY = pp.inputStr("Enter your VirusTotal API KEY: ")

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creating the socket
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         # Set Socket
tcpServer.bind((TCP_IP, TCP_PORT))                                      # Bind the server port and IP
threads = []                                                            # Create a list of threads

# Print Status of the connection with start datetime and server IP and Port Info
print("\n"+str(datetime.datetime.now()),"\033[40m\033[1;34m[*]Waiting for a connection to SPYthon at ",TCP_IP,"at",TCP_PORT,"...\033[40m\033[0m")

web_dir = os.path.join(os.path.dirname(__file__), 'web')                # Sets path to web server
os.chdir(web_dir)                                                       # Changes to web server directory
os.system("python3 -m http.server "+str(WEB_PORT)+" &")                 # Runs web server through os.system bc of threading issue with running it in script

# Print Status of the web connection with start datetime and server IP and Port Info
print(str(datetime.datetime.now()),"\033[40m\033[1;34m[*]Waiting for a connection to Web Server at ",TCP_IP,"at",WEB_PORT,"...\033[40m\033[0m")                                                # Serves Web Server Forever

while True:                                                             # Created an infinite while loop
    tcpServer.listen(4)                                                 # Start server Listener     # Output server status with IP and Port
    (s, (ip,port)) = tcpServer.accept()                                 # Accept a new client
    newthread = ClientThread(ip,port)                                   # Create a new thread
    newthread.start()                                                   # Start new thread
    threads.append(newthread)                                           # Add new thread to list of threads

for t in threads:                                                       # for loop of number of given number threads
    t.join()                                                            # join new thread, this is how multi threading is done
