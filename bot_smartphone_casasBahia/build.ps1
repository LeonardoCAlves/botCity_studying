$exclude = @("venv", "bot_smartphone_casasBahia.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_smartphone_casasBahia.zip" -Force