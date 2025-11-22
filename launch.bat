@echo off
echo === Lancement du serveur Flask ===

:: Active ton venv (si tu en as un)
if exist venv (
    echo Activation de l'environnement virtuel...
    call venv\Scripts\activate
)

echo Installation des dependances...
pip install -r requirements.txt

echo Demarrage de l'application...
set PORT=5000
python app.py

pause
