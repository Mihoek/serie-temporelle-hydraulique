.. _premiers-pas:

Premiers Pas
============

Ce guide vous aide à démarrer avec l’application d’analyse prédictive des systèmes hydrauliques, développée dans le cadre de la filière **Génie Mécanique et Systèmes Automatisés** à l’**Université de Technologie de Compiègne (UTC)**. Suivez ces étapes pour accéder aux données, lancer l’application Streamlit, et explorer ses fonctionnalités.

Accès aux Données et Modèles
----------------------------

Structure des Données sur Google Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les fichiers sont organisés dans les dossiers suivants sur Google Drive :

- **Models/** : Modèles entraînés (LSTM, GRU, MLP) au format `.h5` et `.joblib`.
- **Data_txt/** : Données brutes au format TXT.
- **Data_long/** : Données prétraitées au format CSV long.
- **Data_csv/** : Données traitées au format CSV.
-**Data_processed/** : Données traitées au format CSV et CSV Long.
Pour accéder aux fichiers :
1. Consultez les liens fournis dans :ref:`installation`.
2. Téléchargez les fichiers et placez-les dans :
   - `data/raw/` pour les fichiers TXT.
   - `data/processed/` pour les fichiers CSV et CSV Long.
   - `models/` pour les modèles.

Exemple de Chargement des Données
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pour charger les données CSV :

::

    import pandas as pd

    # Charger les données CSV
    data = pd.read_csv('data/processed/nom_fichier.csv')

    # Pour les données au format long
    data_long = pd.read_csv('data/processed/nom_fichier_long.csv')

Exemple de Chargement des Modèles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pour utiliser un modèle pré-entraîné :

::

    from tensorflow.keras.models import load_model

    # Charger le modèle LSTM
    model = load_model('models/model_lstm_se.h5')

Utilisation de l’Application
---------------------------

1. Lancer l’Application Streamlit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dans le terminal, avec l’environnement virtuel activé, exécutez :

::

    streamlit run app.py

L’application s’ouvrira dans votre navigateur par défaut (généralement à `http://localhost:8501`).

2. Explorer l’Interface
~~~~~~~~~~~~~~~~~~~~~~~
L’application propose plusieurs sections principales :

a. **Tableau de Bord**
   - Vue d’ensemble des données des capteurs.
   - Graphiques de tendances pour l’efficacité (SE) réelle et prédite.
   - Carte de chaleur des corrélations entre capteurs.

b. **Chatbot**
   - Assistant conversationnel en langage naturel.
   - Exemples de requêtes :
     - "Prédire SE avec 5.0, 5.0, 0, 0, 0.25, 100.0, 7.34, 3.1, 40, 20"
     - "Optimiser pour SE 95"
   - Fournit des prédictions SE ou des paramètres optimisés.

c. **Prédiction SE**
   - Entrez manuellement les valeurs des capteurs (`PS1`, `PS2`, `PS3`, `PS5`, `PS6`, `EPS1`, `FS1`, `FS2`, `TS1`, `CE`).
   - Obtenez des prédictions d’efficacité avec les modèles LSTM et GRU.
   - Comparez les résultats sous forme de graphique.

d. **Prédiction Inverse**
   - Définissez une efficacité cible (SE, en %).
   - Obtenez les valeurs recommandées des capteurs pour atteindre cette cible.

Dépannage
---------
Si vous rencontrez des problèmes, vérifiez les points suivants :

1. **Environnement virtuel** :
   - Assurez-vous que l’environnement est activé (`venv` doit apparaître dans le terminal).
   - Réinstallez les dépendances si nécessaire : `pip install -r requirements.txt`.

2. **Fichiers de données** :
   - Confirmez que les fichiers TXT, CSV, et CSV Long sont dans `data/raw/` et `data/processed/`.
   - Vérifiez que les noms correspondent à ceux attendus par `app.py`.

3. **Modèles** :
   - Assurez-vous que les fichiers de modèles sont dans `models/` et accessibles.
   - Vérifiez les chemins dans `app.py` (par exemple, `/content/drive/MyDrive/Projet_time_series/Models/`).

4. **Logs d’erreur** :
   - Consultez les messages d’erreur dans le terminal ou le dossier `logs/` (si configuré).
   - Exemple d’erreur courante : `FileNotFoundError` indique un fichier manquant.

5. **Dépendances** :
   - Vérifiez que toutes les bibliothèques sont installées : `pip list`.
   - Testez l’importation : `python -c "import pandas, numpy, tensorflow, streamlit"`.

.. note::
   Une démonstration complète de l’application est disponible dans la vidéo :download:`streamlit_demo.mp4 <_static/streamlit_demo.mp4>`, située dans le dossier `Demo` du dépôt GitHub. Lancez l’application avec `streamlit run app.py` pour explorer les fonctionnalités décrites.