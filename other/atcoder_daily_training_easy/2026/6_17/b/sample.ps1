$a, $b, $c = [Console]::ReadLine().Trim() -split '\s+' | ForEach-Object { [int]$_ }
if ($a -eq $b -or $b -eq $c -or $a -eq $c) { 'Yes' } else { 'No' }
