Premiers Pas
============

Structure des Données
--------------------

Types de Capteurs
^^^^^^^^^^^^^^^^
* **PS1-PS6**: Capteurs de Pression
    * Plage normale: 0-10 Bar
    * Fréquence: 100 Hz
* **FS1-FS2**: Capteurs de Débit
    * Plage normale: 0-100 L/min
    * Fréquence: 10 Hz
* **TS1-TS4**: Capteurs de Température
    * Plage normale: 20-80°C
    * Fréquence: 1 Hz

Comment Utiliser l'Application
----------------------------

1. Lancer l'Application Streamlit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dans le terminal::

    streamlit run app.py

2. Utiliser l'Interface
^^^^^^^^^^^^^^^^^^^^
L'interface propose 4 sections:

a. **Tableau de Bord**
    * Vue d'ensemble des données
    * Graphiques de tendance
    * Corrélations entre capteurs

b. **Chatbot**
    * Assistant conversationnel
    * Posez des questions en langage naturel
    * Exemples: "Prédire SE" ou "Optimiser pour SE 95"

c. **Prédiction SE**
    * Entrez les valeurs des capteurs
    * Obtenez une prédiction d'efficacité
    * Comparez les résultats LSTM et GRU

d. **Prédiction Inverse**
    * Définissez une efficacité cible
    * Obtenez les paramètres recommandés

En Cas de Problème
-----------------
1. Vérifiez que l'environnement virtuel est activé
2. Assurez-vous que tous les fichiers de données sont bien dans le dossier ``data/raw``
3. Assurez-vous que toutes les bibliothèques sont installées
4. Consultez les logs d'erreur dans le dossier ``logs``

Accès aux Données et Modèles
============================

Structure des Données sur Google Drive
-------------------------------------

Les fichiers sont organisés comme suit:

📁 Projet_time_series/
├── 📁 Models/          # Modèles entraînés LSTM et GRU
├── 📄 Data_txt/        # Données brutes au format TXT
├── 📄 Data_long/       # Données prétraitées format long
└── 📄 Data_csv/        # Données traitées au format CSV

Comment Accéder aux Données
--------------------------

1. **Données Brutes** (Data_txt):
   * Format: Fichiers TXT
   * Dernière mise à jour: 21 mai 2025
   * Contient les mesures brutes des capteurs

2. **Données Longues** (Data_long):
   * Format: Format long pour analyse temporelle
   * Dernière mise à jour: 4 avril 2025
   * Optimisé pour l'analyse de séries temporelles

3. **Données CSV** (Data_csv):
   * Format: CSV pour faciliter l'importation
   * Dernière mise à jour: 3 avril 2025
   * Format recommandé pour débuter

4. **Modèles** (Models):
   * Contient les modèles LSTM et GRU entraînés

Utilisation des Données
---------------------

Pour charger les données::

    import pandas as pd
    
    # Charger les données CSV
    data = pd.read_csv('chemin/vers/Data_csv/nom_fichier.csv')
    
    # Pour les données au format long
    data_long = pd.read_csv('chemin/vers/Data_long/nom_fichier.csv')

Chargement des Modèles
---------------------

Pour utiliser les modèles pré-entraînés::

    from tensorflow.keras.models import load_model
    
    # Charger le modèle LSTM
    model = load_model('chemin/vers/Models/model_lstm.h5')

Démonstration Vidéo
------------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <video controls width="100%">
            <source src="../_static/media/demonstration-video.webm" type="video/webm">
            Votre navigateur ne prend pas en charge la lecture de vidéos.
        </video>
    </div>

La vidéo ci-dessus démontre:

1. **Démarrage**
   * Installation de l'environnement
   * Chargement des données
   * Lancement de l'application

2. **Fonctionnalités**
   * Navigation dans l'interface
   * Utilisation des modèles de prédiction
   * Visualisation des résultats

3. **Analyse**
   * Interprétation des graphiques
   * Utilisation des filtres
   * Export des résultats