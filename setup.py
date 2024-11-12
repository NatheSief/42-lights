from setuptools import setup, find_packages

setup(
    name="video_color_analyzer",  # Nom du package
    version="0.1.0",              # Version du package
    packages=find_packages(),     # Trouver tous les sous-dossiers avec __init__.py
    install_requires=[            # Liste des dépendances nécessaires
        "mss",
        "opencv-python",
        "scikit-learn",
        "numpy",
    ],
    description="Un package pour capturer l'écran et analyser les couleurs dominantes sur une matrice 5x5.",
    long_description=open('README.md').read(),  # Description longue à partir du fichier README.md
    long_description_content_type='text/markdown',
    author="Ton Nom",
    author_email="nsiefert@42.paris.fr",
    url="https://github.com/NatheSief/42-lights",  # Lien vers ton dépôt GitHub
    classifiers=[                  # Catégories de ton package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
