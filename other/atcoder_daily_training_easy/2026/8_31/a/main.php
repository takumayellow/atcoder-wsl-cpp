<?php
fscanf(STDIN, "%d %d %d %d", $v, $a, $b, $c);
$v = $v % ($a + $b + $c);
if ($v < $a) { echo "F"; }
else if ($a <= $v and $v < $a + $b) { echo "M"; }
else { echo "T"; }
?>
