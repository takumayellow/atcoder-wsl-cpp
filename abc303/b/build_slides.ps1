param(
    [string]$Target = "indexing_slides.tex"
)

$ErrorActionPreference = "Stop"

function Clean-Intermediates {
    param([string]$BaseName)
    $exts = @("aux", "dvi", "fdb_latexmk", "fls", "log", "nav", "out", "snm", "toc", "vrb")
    foreach ($ext in $exts) {
        $path = "$BaseName.$ext"
        if (Test-Path $path) {
            Remove-Item $path -Force
        }
    }
}

if (-not (Test-Path $Target)) {
    throw "Target file not found: $Target"
}

$baseName = [System.IO.Path]::GetFileNameWithoutExtension($Target)
$latexmk = "C:\texlive\2024\bin\windows\latexmk.exe"

if (Test-Path $latexmk) {
    & $latexmk -pdfdvi $Target
    if ($LASTEXITCODE -eq 0) {
        & $latexmk -c $Target
        exit $LASTEXITCODE
    }
}

Write-Warning "latexmk failed or unavailable. Falling back to platex + dvipdfmx."

platex $Target
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
platex $Target
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
dvipdfmx "$baseName.dvi"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Clean-Intermediates -BaseName $baseName
