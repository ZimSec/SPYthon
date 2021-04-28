<?php
$host_ip = $_POST['dataPoint'];
$excmd = exec('/usr/bin/python3 /var/www/argusio/hostpass.py ' . $host_ip);
echo $excmd;
?>
