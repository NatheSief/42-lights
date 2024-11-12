import requests
import socket

def is_valid_ip(ip):
    """
    Vérifie si l'adresse IP est valide.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def send_to_grandma(dominant_colors, grandma_ip):
    """
    Envoie les couleurs dominantes à la table GrandMA via une API HTTP.
    Le paramètre `grandma_ip` correspond à l'IP de la table GrandMA.
    """
    # Vérification de la validité de l'adresse IP
    if not is_valid_ip(grandma_ip):
        print(f"L'adresse IP {grandma_ip} n'est pas valide.")
        return

    # Formater les couleurs dominantes en un format approprié pour la table GrandMA
    # Par exemple, on peut convertir les couleurs RGB en hexadécimal si nécessaire
    # Pour l'exemple, on envoie les couleurs sous forme de liste de tuples RGB
    colors_data = {
        "colors": [{"r": color[0], "g": color[1], "b": color[2]} for color in dominant_colors]
    }

    # URL de l'API GrandMA (exemple)
    grandma_url = f"http://{grandma_ip}/api/set_lights"

    # Envoyer la requête POST avec les couleurs au format JSON
    try:
        response = requests.post(grandma_url, json=colors_data)
        if response.status_code == 200:
            print("Commande envoyée avec succès à la table GrandMA.")
        else:
            print(f"Erreur lors de l'envoi des données à GrandMA: {response.status_code}")
            print(f"Réponse de l'API: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la communication avec GrandMA: {str(e)}")
