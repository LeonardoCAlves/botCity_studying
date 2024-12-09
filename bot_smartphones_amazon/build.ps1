$exclude = @("venv", "bot_smartphones_amazon.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_smartphones_amazon.zip" -Force