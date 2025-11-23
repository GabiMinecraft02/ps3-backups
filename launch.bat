@echo off
:loop
cls
echo Lancement du serveur Flask...
REM Active ton venv si besoin
call venv\Scripts\activate.bat
python app.py
echo.
set /p choice="Le serveur s'est arrêté. Relancer ? (o/n) : "
if /i "%choice%"=="o" goto loop
echo Fermeture du script.
pause
