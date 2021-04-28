import os
import sys

ip = sys.argv[1]

#ip = '157.245.124.20'

print(ip)
print("Hello\n")

#os.system(f"echo {ip} | nc localhost 8899")
os.system(f"nmap -oX - {ip} --top-ports 10")

HTMLFile = "Report-"+datetime.datetime.now().strftime("%Y%m%d%H%M")+"-"+str(UserIn)+".html"
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

</head>
<body>

<div>
Nmap Service Scan
{ip}
</div> <!-- end services-item -->
</body>
</html>

f = open(HTMLFile, "w")                                   # Open new text file for active scan
f.write(html)                                   # Write text file from json_object
f.close()

print(html)

final_url = (f"http://104.236.241.177:{WEB_PORT}/{HTMLFile}")

print(final_url)
