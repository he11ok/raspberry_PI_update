<?php
$host_name="127.0.0.1";
$user="RPIuse";
$psd="970111";

$conn = mysqli_connect($host_name,$user,$psd);

if(!$conn)
  {
    echo"MySQL database error";
  }
  else
  {
    echo "MySQL connection successfully!";
  }

$conn->close();


?>
