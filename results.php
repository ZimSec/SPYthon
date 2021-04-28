<?php
$ip_addr = $_POST['chost_ip'];
$shodan = $_POST['shodan_api'];
$virus = $_POST['virus_api'];
//$cmd = exec('echo ' . $ip_addr . $shodan  . $virus . ' | nc localhost 8899');
$cmd = exec('echo ' . $ip_addr . " " . $shodan . " "  . $virus . ' | nc localhost 8899');
?>

<!DOCTYPE html>
<html>
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
  <meta http-equiv="refresh" content="5; URL=<?php echo $cmd; ?>" />
</head>
<body>
  <div id="preloader">
  <div id="loader"></div>
  </div>
</body>
</html>
