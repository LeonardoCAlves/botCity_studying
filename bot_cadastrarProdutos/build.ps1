$exclude = @("venv", "bot_cadastrarProdutos.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cadastrarProdutos.zip" -Force