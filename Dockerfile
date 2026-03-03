# Wir nehmen ein schlankes Python-Image
FROM python:3.9-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Kopiere die app.py von deinem Rechner in den Container
COPY app.py .

# Befehl, der ausgeführt wird, wenn der Container startet
# -u sorgt dafür, dass die Ausgabe sofort in der Konsole erscheint
CMD ["python", "-u", "app.py"]