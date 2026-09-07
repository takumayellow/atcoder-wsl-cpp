<?php
$a = intval(trim(fgets(STDIN)));
[$b, $c] = array_map('intval', explode(' ', trim(fgets(STDIN))));
$d = trim(fgets(STDIN));

echo ($a + $b + $c) . ' ' . $d;
?>
