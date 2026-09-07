<?php
$x = (int)(fgets(STDIN));
$ans = ($x + 1) % 3;
if ($ans == 0) {$ans += 3;}

echo $ans;

