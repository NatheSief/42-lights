import mss
import numpy as np
import cv2
from sklearn.cluster import KMeans

def extract_dominant_color(image, n_colors=1):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    return kmeans.cluster_centers_[0]

def capture_screen_and_analyze():
    taille_matrice = 10
    with mss.mss() as sct:
        monitor = sct.monitors[1]

        screenshot = sct.grab(monitor)
        image = np.array(screenshot)

        resized_image = cv2.resize(image, (taille_matrice, taille_matrice), interpolation=cv2.INTER_LINEAR)

        dominant_colors = [extract_dominant_color(resized_image[i//taille_matrice, j//taille_matrice]) for i in range(taille_matrice) for j in range(taille_matrice)]

        return dominant_colors
