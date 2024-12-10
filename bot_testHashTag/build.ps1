$exclude = @("venv", "bot_testHashTag.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_testHashTag.zip" -Force