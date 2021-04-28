#!/usr/bin/env python3
import os
import sys
import nmap3
import subprocess
import datetime

#def nmap_func():

ip = sys.argv[1]

print(ip)

#print("donmap.py", ip)

#nmap_p = os.popen(f"nmap {ip}")

#nm = nmap3.Nmap()
#os_results = nmap.nmap_os_detection("192.168.178.2")

#HTMLFile =("Report-"+datetime.datetime.now().strftime("%Y%m%d%H%M")+"-"+str(ip)+".html")
#print(HTMLFile)

nm = nmap3.Nmap() 
os_results = nm.nmap_os_detection(ip)

#print(nmap_p)

print(os_results)

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
                <link rel="stylesheet" href="~/flask/static/css/styles.css">
                <link rel="stylesheet" href="~/flask/static/css/vendor.css">
                <!-- script
                ================================================== -->
                <script src="~/flask/static/js/modernizr.js"></script>
                <script defer src="~/flask/static/js/fontawesome/all.min.js"></script>
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
                                        SPYthon Report of <span>{ip}</span>.
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
                            <p class="desc">Here is a list of key data points collected from {ip}.</p>
                        </div>
                        <div class="column large-8 medium-12 align-x-right" data-aos="fade-up">
                            <p>
			    Host Data:<br>
                            <object data="bucket.txt" type="text/plain"
                            width="1000" style="height:1000px;background-color:white;font-size:300%">
                            <a href="bucket.txt">No Support?</a>
                            </object>
			   </p>
                        </div>
                    </div> <!-- end section-head -->
                    <div class="row block-large-1-3 block-medium-1-2 block-tab-full services-list">
                        <div class="column services-item" data-aos="fade-up">
                            <h5>Nmap Service Scan</h5>
                            <p>
                            {os_results}
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

print(html)
