# SPYthon

**Project Description**\
The idea for this project is to create a multi-threaded python server that will generate HTML reports on what exploits can be run against what host. First, the user will create a new session with the host and give the host an IP. Based on whether or not that IP can be scanned passively (if it exists in Shodan/Censys) it will ask the user if this is owned or allowed infrastructure to scan. If the user consents, the server will scan the host with Nmap and determine what versions the host is running and if their services are vulnerable. If the user does not approve the server will not scan the host. If the given host has already been scanned by Censys/Shodan then those results will be fed into the server via API's. The server/script will then determine if the vulnerability has a given exploit, which it will then display to the user along with the ports in a report that is in HTML format.


**Roles and Responsibilities**

| Member             | Role                                  | Responsibilities                                                                    |
|--------------------|---------------------------------------|-------------------------------------------------------------------------------------|
| Jack Zimmer        | Developer, Project Manager            | Will develop the project and manage the project timeline and team.                  |
| Gabrielle Merriken | Developer, Documenter                 | Will develop the project and create, format, proofread, and submit documentation.   |
| Christian Ekeigwe  | Developer, Infrastructure, Bug Tester | Will develop the project and troubleshoot and test for bugs throughout the project. |


**Useful Sources**\
Python3 HTML: Report Generation\
https://programminghistorian.org/en/lessons/output-data-as-html-file \
https://plotly.com/python/v3/html-reports/

Censys:\
By default, Censys performs full-text searches. For example, searching for “Dell” will find any hosts where the word Dell appears in the record—it won't limit the search to Dell manufactured devices. However, this is possible by querying specific fields using the syntax in the link below:\
https://censys.io/ipv4/help?q=& \
https://censys.io/api

Shodan:\
The REST API: provides methods to search Shodan, look up hosts, get summary information on queries and a variety of utility methods to make developing easier.\
https://developer.shodan.io/api 

Exploit DB:\
The name of this utility is SearchSploit and as its name indicates, it will search for all exploits and shellcode.\
https://www.exploit-db.com/searchsploit 

Nmap:\
“A python 3 library which helps in using nmap port scanner. The way this tools works is by defining each nmap command into a python function making it very easy to use sophisticated nmap commands in other python scripts. Nmap is a complicated piece of software used for reconnaissance on target networks, over the years new features have been added making it more sophisticated.” Ref pypi.org\
https://pypi.org/project/python3-nmap/
