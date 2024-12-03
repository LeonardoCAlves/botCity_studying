$exclude = @("venv", "bot_cotacaoDolar.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cotacaoDolar.zip" -Force