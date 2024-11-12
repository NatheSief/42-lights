from flask import Flask, render_template, request, jsonify
from capture import capture_screen_and_analyze
from grandma_controller import send_to_grandma

app = Flask(__name__)

# Page d'accueil avec formulaire pour entrer l'adresse IP
@app.route('/')
def index():
    return render_template('index.html')

# Page pour capturer l'écran et envoyer les couleurs dominantes
@app.route('/capture', methods=['POST'])
def capture():
    # Capture des couleurs dominantes
    dominant_colors = capture_screen_and_analyze()
    
    # Envoi des couleurs à la table GrandMA (simulé ici)
    grandma_ip = request.form.get('grandma_ip')
    if grandma_ip:
        send_to_grandma(dominant_colors, grandma_ip)
    
    return jsonify({"dominant_colors": dominant_colors})

if __name__ == '__main__':
    app.run(debug=True)
