from flask import Flask, render_template, request
import threading
import time
from capture import capture_screen_and_analyze, extract_dominant_color
from grandma_controller import send_to_grandma

app = Flask(__name__)

# Fonction pour analyser le flux vidéo et envoyer les couleurs à la GrandMA
def analyze_video():
    while True:
        # Capture l'écran et analyse la couleur dominante
        image = capture_screen_and_analyze()
        dominant_color = extract_dominant_color(image)
        
        # Envoie la couleur dominante à la table GrandMA
        send_to_grandma(dominant_color)
        
        # Pause de 0.5 seconde pour éviter une surcharge du processeur
        time.sleep(0.5)

# Route principale pour afficher la page
@app.route('/')
def index():
    return render_template('index.html')

# Route pour saisir l'adresse IP de la GrandMA
@app.route('/set-ip', methods=['POST'])
def set_ip():
    ip = request.form.get('ip_address')
    # Logique pour configurer l'adresse IP de la GrandMA
    # (Il faudrait probablement sauvegarder cette IP dans un fichier ou variable)
    print(f"Adresse IP de la GrandMA : {ip}")
    return "IP enregistrée avec succès."

# Route pour saisir le chemin du fichier vidéo (ou URL)
@app.route('/set-video', methods=['POST'])
def set_video():
    video_source = request.form.get('video_source')
    # Logique pour traiter la source vidéo (local ou en ligne)
    print(f"Source vidéo : {video_source}")
    return "Source vidéo enregistrée avec succès."
@app.route('/stop', methods=['POST'])
def stop_program():
    """Arrêter le programme Flask proprement."""
    try:
        # Arrêter le programme en utilisant sys.exit() pour arrêter le programme Python proprement
        print("Arrêt du programme...")
        sys.exit("Arrêt demandé via API")
        return {"message": "Le programme s'arrête."}, 200
    except Exception as e:
        print(f"Erreur lors de l'arrêt du programme : {e}")
        return {"message": "Erreur lors de l'arrêt."}, 500

if __name__ == "__main__":
    # Démarrer l'analyse vidéo dans un thread séparé
    video_thread = threading.Thread(target=analyze_video)
    video_thread.daemon = True  # Le thread se termine quand l'application Flask se termine
    video_thread.start()

    # Lancer l'application Flask
    app.run(host='0.0.0.0', port=5000)
