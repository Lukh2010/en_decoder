@echo off
echo --- Update wird geprueft (GitHub Registry) ---
docker pull ghcr.io/lukh2010/base64-en-decoder:main

echo.
echo --- Starte Base64 Tool ---
echo.

:: -it: interaktiv mit Terminal
:: --rm: loescht den Container-Muelleimer nach dem Beenden automatisch
docker run -it --rm ghcr.io/lukh2010/base64-en-decoder:main

echo.
echo Programm beendet.
pause