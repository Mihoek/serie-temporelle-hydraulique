Analyse Prédictive de Systèmes Hydrauliques
Ce projet utilise des techniques avancées d'analyse de séries temporelles pour surveiller et prédire l'efficacité des systèmes hydrauliques. Il propose une application interactive basée sur Streamlit, intégrant des modèles d'apprentissage automatique (LSTM, GRU, MLP) pour prédire l'efficacité système (SE) et optimiser les paramètres des capteurs. Une capture vidéo de l'application est disponible pour démontrer ses fonctionnalités.
Table des Matières

Fonctionnalités
Prérequis
Installation
Utilisation
Documentation
Contribution
Contact

Fonctionnalités

Prédiction de l'efficacité (SE) : Utilisation de modèles LSTM et GRU pour prédire l'efficacité à partir des données de capteurs.
Prédiction inverse : Optimisation des valeurs des capteurs pour atteindre une efficacité cible.
Tableau de bord interactif : Visualisation des tendances et corrélations des capteurs via Streamlit.
Chatbot NLP : Interface conversationnelle pour interagir avec l'application en langage naturel.
Documentation complète : Guide détaillé hébergé sur ReadTheDocs.

Prérequis

Python 3.13 ou supérieur
Git
Environnement virtuel (recommandé)
Accès aux données et modèles hébergés sur Google Drive (voir Documentation)
Dépendances listées dans requirements.txt

Installation

Clonez le dépôt :
git clone https://github.com/Mihoek/serie-temporelle-hydraulique.git
cd serie-temporelle-hydraulique


Créez et activez un environnement virtuel :
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


Installez les dépendances :
pip install -r requirements.txt


Téléchargez les données et modèles depuis Google Drive (voir Documentation pour les liens).

(Optionnel) Placez la capture vidéo de démonstration (streamlit_demo.mp4) dans docs/source/_static/media/ pour la documentation.


Utilisation

Lancez l'application Streamlit :
streamlit run app.py


Explorez les fonctionnalités via l'interface :

Tableau de Bord : Visualisez les données des capteurs et les prédictions SE.
Chatbot : Posez des questions comme "Prédire SE avec 5.0, 5.0, 0, 0, 0.25, 100.0, 7.34, 3.1, 40, 20" ou "Optimiser pour SE 95".
Prédiction SE : Entrez manuellement les valeurs des capteurs pour prédire SE.
Prédiction Inverse : Définissez une cible SE pour obtenir les paramètres recommandés.


Consultez la capture vidéo streamlit_demo.mp4 pour une démonstration des fonctionnalités (disponible dans l'application ou la documentation).


Pour plus de détails, reportez-vous à la Documentation.
Documentation
La documentation complète est disponible sur ReadTheDocs. Elle inclut :

Une introduction aux systèmes hydrauliques.
Des instructions détaillées pour l'installation.
Un guide d'utilisation avec des exemples.
Une intégration de la capture vidéo de l'application Streamlit.

Contribution
Les contributions sont les bienvenues ! Pour proposer des améliorations :

Forkez le dépôt.
Créez une branche pour vos modifications (git checkout -b feature/amélioration).
Soumettez une pull request avec une description claire.

Veuillez respecter les conventions de codage et ajouter des tests si possible.
Contact
Pour toute question ou suggestion, contactez Mihoek ou ouvrez une issue sur le dépôt GitHub.

Dernière mise à jour : 13 juin 2025
