<?php
    // session_start();

    header("Access-Control-Allow-Origin: *");
    
    $url = $_POST['url'];
    // echo $url;  
   
    $test = "py Test.py"." ".$url;
    // echo $test;
    $command = escapeshellcmd($test);
    $output = shell_exec($command);
    echo $output;
    
?>
