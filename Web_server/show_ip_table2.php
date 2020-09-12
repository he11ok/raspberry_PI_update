<?php
$mysqli = new mysqli("localhost", "RPIuse", "970111", "test");

/* check connection */
if ($mysqli->connect_errno) {
    printf("Connect failed: %s\n", $mysqli->connect_error);
    exit();
}

/* Select queries return a resultset */
if ($result = $mysqli->query("SELECT * FROM ip_address")) {
    printf("Select returned %d rows.\n", $result->num_rows);
    echo "<br><br>";


    while ($row = mysqli_fetch_row($result)) {
    	printf("%s %s %s\n", $row[0],$row[1],$row[2]);
	echo "<br>";
    }
    echo "<br>";
    while ($fieldinfo = mysqli_fetch_field($result)) {

	    printf("Key name: %s", $fieldinfo->name);
	    echo "<br>";
	    printf("Max length: %d",$fieldinfo->max_length);
   	    echo "<br>";
    }
    /* free result set */
    $result->close();
}


$mysqli->close();
?>
