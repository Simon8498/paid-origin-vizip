# Copy skill bundle from github-upload to project .cursor/skills (after you edit files here)
$UploadRoot = Split-Path $PSScriptRoot -Parent
$ProjectRoot = Split-Path $UploadRoot -Parent
$Src = Join-Path $UploadRoot ".cursor\skills\cima-analytics-planner"
$Dst = Join-Path $ProjectRoot ".cursor\skills\cima-analytics-planner"
if (-not (Test-Path $Src)) { throw "Source not found: $Src" }
New-Item -ItemType Directory -Force -Path $Dst | Out-Null
Copy-Item -Path (Join-Path $Src "*") -Destination $Dst -Recurse -Force
Write-Host "Synced skill to $Dst"
