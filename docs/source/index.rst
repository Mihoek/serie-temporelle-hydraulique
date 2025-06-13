Analyse des Séries Temporelles Hydrauliques
=========================================

Guide complet pour l'analyse prédictive des systèmes hydrauliques.

.. toctree::
   :maxdepth: 2
   :caption: Guide d'Utilisation

   guide/introduction
   guide/installation
   guide/premiers_pas
   guide/analyse

.. toctree::
   :maxdepth: 2
   :caption: Référence Technique

   reference/structure_donnees
   reference/api
   reference/modeles   Introduction
   ===========
   
   Qu'est-ce qu'un Système Hydraulique?
   ----------------------------------
   Un système hydraulique utilise un fluide sous pression pour transmettre de l'énergie et réaliser des travaux mécaniques. Ces systèmes sont essentiels dans de nombreuses applications industrielles.
   
   Composants Principaux
   ^^^^^^^^^^^^^^^^^^
   1. **Pompe Hydraulique**: Fournit un débit constant de fluide sous pression
   2. **Cylindre/Moteur Hydraulique**: Convertit l'énergie hydraulique en mouvement mécanique
   3. **Vannes**: Contrôlent la direction et la pression du fluide
   4. **Réservoir**: Stocke et restitue le fluide
   5. **Filtre**: Maintient la propreté du fluide
   
   Description des Capteurs
   ^^^^^^^^^^^^^^^^^^^^^
   | **Capteur**  | **Description** | **Fréquence** | **Points/Cycle** |
   |--------------|-----------------|---------------|------------------|
   | **PS1-PS6**  | Pression (Bar) | 100 Hz | 6000 |
   | **EPS1**     | Puissance pompe (kW) | 100 Hz | 6000 |
   | **FS1-FS2**  | Débit (L/min) | 10 Hz | 600 |
   | **TS1-TS4**  | Température (°C) | 1 Hz | 60 |
   | **VS1**      | Vibrations (mm/s) | 1 Hz | 60 |
   | **CE**       | Efficacité thermique (%) | 1 Hz | 60 |
   | **SE**       | Rendement global (%) | 1 Hz | 60 |
   
   Objectifs du Projet
   -----------------
   1. Analyser les données des capteurs hydrauliques
   2. Prédire l'efficacité du système (SE)
   3. Optimiser les paramètres pour une meilleure performance
   4. Détecter les anomalies potentielles   Installation
   ===========
   
   Prérequis Techniques
   ------------------
   1. **Python 3.13+** : Téléchargeable sur `python.org <https://www.python.org/downloads/>`_
   2. **Git** : Téléchargeable sur `git-scm.com <https://git-scm.com/downloads>`_
   3. **VS Code** (recommandé) : Téléchargeable sur `code.visualstudio.com <https://code.visualstudio.com/download>`_
   
   Installation Pas à Pas
   --------------------
   
   1. Téléchargement du Projet
   ^^^^^^^^^^^^^^^^^^^^^^^^
   Ouvrez un terminal (PowerShell sur Windows) et tapez::
   
       git clone https://github.com/Mihoek/serie-temporelle-hydraulique.git
       cd serie-temporelle-hydraulique
   
   2. Création de l'Environnement Virtuel
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   Sur Windows::
   
       python -m venv venv
       .\venv\Scripts\activate
   
   Sur Linux/Mac::
   
       python -m venv venv
       source venv/bin/activate
   
   3. Installation des Dépendances
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
   Une fois l'environnement activé::
   
       pip install -r requirements.txt
   
   4. Téléchargement des Données
   ^^^^^^^^^^^^^^^^^^^^^^^^^
   a. Accédez aux liens Google Drive:
      * `Données brutes (TXT) <https://drive.google.com/drive/folders/1D6pebeI1JvbhwtHqNgVoNZM2hLTcaI9k?usp=sharing>`_
      * `Données traitées (CSV) <https://drive.google.com/drive/folders/1ZtwsmsefogTsO0_kr_PFlmX0hW0a6sMa?usp=drive_link>`_
      * `Données traitées (CSV_Long) <https://drive.google.com/drive/folders/1KiaSdowspB8fJP9vV1ujai_RWeYAlkQg?usp=drive_link>`_
   
   b. Créez les dossiers nécessaires::
   
       mkdir -p data/raw data/processed
   
   c. Placez les fichiers téléchargés dans ``data/raw``
   
   Vérification de l'Installation
   ---------------------------
   Tapez dans le terminal::
   
       python -c "import pandas; import numpy; print('Installation réussie!')"