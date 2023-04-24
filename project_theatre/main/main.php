<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>HCIS Theatre Booking System</title>
</head>
<body>
	Hello!
	<?php
		$ip = $_SERVER["REMOTE_ADDR"];
		$cmd = "python3 ip_check.py ".$ip;
		$check = exec($cmd);

		if ($check == 'failed'){
			{
			echo "<script language='javascript'>window.location='../buffer_login/ip_no_access.html'</script>";
			}
		}
		
	?>
</body>
</html>