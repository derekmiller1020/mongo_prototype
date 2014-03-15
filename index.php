<html>
<body>
<h1> Limit amount of messages </h1>
<h2><a href="?sort=1">1</a></h2>
<h2><a href="?sort=5">5</a></h2>
<h2><a href="?sort=10">10</a></h2>
<br><br>

<h1>Error Messages</h1>

</body>
</html>

<?php

$m = new MongoClient();

$db = $m->mongo;
$errors = $db->errors;
$cursor = $errors->find();
$cursor->sort(array('date' => -1));

if (isset($_GET['sort'])){
	$cursor->limit($_GET['sort']);
}

else {
	$cursor->limit(10);
}

foreach ($cursor as $document) {
	echo "<b>date:</b> " . $document["date"] . "<br>"; 
        echo "    <b> Error Message</b>: " . $document["error"] . "<br><br>";
}

?>
