<?php
//if (isset($_POST['submit'])) { //to check if the form was submitted
$host_ip= $_POST['ip_addr'];
$excmd = exec('/usr/bin/python3 /var/www/argusio/teststuff/donmap.py ' . $host_ip);
echo $excmd;
//}

?>
