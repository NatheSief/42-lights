# Utiliser une image Python de base
FROM python:3.11-slim

# Installer les dépendances système nécessaires à OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier tous les fichiers du projet dans le conteneur
COPY . /app

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port pour Flask
EXPOSE 5000

# Ajouter un script d'entrée pour démarrer l'application
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Lancer l'application via le script start.sh
CMD ["/app/start.sh"]
