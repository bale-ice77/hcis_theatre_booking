<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Requesting Server</title>
	<style>
		p{
			display: inline;
		}
	</style>
</head>
<body>
	<p>Redirecting... please do not refresh the page or use the back button on your browser and hang on tight</p>
	<br><br>
	<p>Checking ID</p>
		<?php 
			$ip = $_SERVER["REMOTE_ADDR"];
			echo $ip;
			echo $_POST["ID"].'...';
			$ID = $_POST["ID"];
			$cmd = "python3 login_request.py ".$ID." ".$ip." 2>&1";
			$check = system($cmd, $fh);
			echo (','.'  '.'environmental security'.' ' .$check);
			if ($check == 'granted'){
				{
				echo "<script language='javascript'>window.location='../main/main.php'</script>";
				}
			}
			if ($check == 'denied'){
				{
				echo "<script language='javascript'>window.location='../login_1.php'</script>";
				}
			}
			if ($check == 'banned'){
				{
				echo "<script language='javascript'>window.location='../buffer_login/ip_ban.html'</script>";
				}
			}
		?>
</body>
</html>