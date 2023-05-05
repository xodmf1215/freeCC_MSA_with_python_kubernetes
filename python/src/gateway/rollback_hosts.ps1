(Get-Content -Path "C:\Windows\System32\drivers\etc\hosts") | Where-Object { $_ -notmatch "^127.0.0.1 mp3converter.com" } | Set-Content -Path "C:\Windows\System32\drivers\etc\hosts"
