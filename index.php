<!DOCTYPE html>
<html class="no-js" lang="en">
<head>

    <!--- basic page needs
    ================================================== -->
    <meta charset="utf-8">
    <title>SPYthon</title>
    <meta name="description" content="">
    <meta name="author" content="">
    
   <!-- <style>
    h1 {text-align: center;}
    h2 {text-align: center;}
    p {text-align: center;}
    div {text-align: center;}
    </style> -->

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
    <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>

    <!-- favicons
    ================================================== -->
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="static/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="static/favicon-16x16.png">
    <link rel="manifest" href="manifest/site.webmanifest">

</head>


<body id="top">
    
    <!-- header
    ================================================== -->
    <header class="s-header s-header--blog">
        <div class="row">

            <div class="s-header__logo">
                <a href="https://104.236.241.177">
                    <img src="images/logo.png" alt="Homepage">
                </a>
            </div>

            <nav class="s-header__nav">
                <ul>
                    <li><a href="https://104.236.241.177">Home</a></li>
                </ul>
            </nav>

            <a class="s-header__menu-toggle" href="#0" title="Menu">
                <span class="s-header__menu-icon"></span>
            </a>

        </div> <!-- end row -->
    </header> <!-- end s-header -->
    
    <div class="blog-content">
        <div>
            <div>
                <h1 style="text-align: center;">
                    SPYthon.
                </h1>
            </div>
            <div class="blog-post__content">
                <img src="images/thumbs/post/minimalist-1800.jpg" sizes="(max-width: 2400px) 100vw, 2400px" srcset="images/thumbs/post/minimalist-2400.jpg 2400w, images/thumbs/post/minimalist-1800.jpg 1800w, images/thumbs/post/minimalist-600.jpg 600w" alt="" />
            </div>
            <div class="blog-post__content">
                <p style="text-align: center;">
                    Enter a hostname or IP address
                </p>
                <p>
                <form method="POST" action="results.php" style="text-align: center;">
                    <!--<fieldset>-->
                        <!--<div class="form-group">-->
                            <p><input name="chost_ip" class="h-full-width h-remove-bottom" placeholder="Hostname or IP Address" type="text"/></p>
                            <p><input name="shodan_api" class="h-full-width h-remove-bottom" placeholder="Shodan API Key" type="text"/></p>
			    <p><input name="virus_api" class="h-full-width h-remove-bottom" placeholder="VirusTotal API Key" type="text"/></p>
			    <p><input name="submit" value="Submit" type="submit"></p>
                        <!--</div>-->
                        
                   <!-- </fieldset>-->
                    
                </form> <!-- end form -->

		</p>
                <p>
                    <img src="images/wheel-1000.jpg" sizes="(max-width: 2000px) 100vw, 2000px" srcset="images/wheel-2000.jpg 2000w, images/wheel-1000.jpg 1000w, images/wheel-500.jpg 500w" alt="" />
                </p>
                <h2 style="text-align: center;">
                    What Is SPYthon?
                </h2>
                <p style="text-align: center;">
                    ArgusIO is a free tool that will generate HTML reports on what exploits can be run against what host.
                </p>
            </div>
        </div>
    </div>
    
    <footer class="s-footer">
        <div class="row">
            <div>
                <ul class="s-footer__social">
                    <li><a href="#0"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                    <li><a href="#0"><i class="fab fa-github" aria-hidden="true"></i></a></li>
                    <li><a href="#0"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                </ul>
            </div>
        </div>
    </footer>
</body>

</html>

