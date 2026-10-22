# 1行目 "a b c" を読む
$line = [Console]::ReadLine()

# 空白で分割して整数に変換する
$tokens = $line.Split(' ')
$a = [int]$tokens[0]
$b = [int]$tokens[1]
$c = [int]$tokens[2]

# どれか2辺が等しければ二等辺三角形
if ($a -eq $b -or $b -eq $c -or $c -eq $a) {
    Write-Output "Yes"
}
else {
    Write-Output "No"
}
