# Wir nehmen ein schlankes Python-Image
FROM python:3.11-slim-bookworm
ENV DEBIAN_FRONTEND=noninteractive
# Update OS packages to mitigate known vulnerabilities, install ca-certificates, and clean cache
# Use a newer, supported Debian base (bookworm) to reduce known high vulnerabilities in older images
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y --no-install-recommends ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Kopiere die app.py von deinem Rechner in den Container
COPY b64_tool.py .

# Befehl, der ausgeführt wird, wenn der Container startet
# -u sorgt dafür, dass die Ausgabe sofort in der Konsole erscheint
CMD ["python", "-u", "b64_tool.py"]