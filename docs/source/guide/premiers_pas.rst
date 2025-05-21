Premiers Pas
===========

Structure des Données
-------------------
Les données sont organisées par type de capteur:

* **PS1-PS6**: Capteurs de Pression (échantillonnage à 100 Hz)
    * Unité: Bar
    * Plage normale: 0-10 Bar
* **FS1-FS2**: Capteurs de Débit (échantillonnage à 10 Hz)
    * Unité: m³/h
    * Plage normale: 0-100 m³/h
* **TS1-TS4**: Capteurs de Température (échantillonnage à 1 Hz)
    * Unité: °C
    * Plage normale: 20-80°C
* **VS1**: Capteur de Vibrations (échantillonnage à 1 Hz)
    * Unité: mm/s
    * Plage normale: 0-10 mm/s

Chemin d'Accès aux Données
----------------------
Avant de commencer, vous devez télécharger les données:

1. Accédez aux liens suivants:
    * `Données brutes (format txt) <https://drive.google.com/drive/folders/1D6pebeI1JvbhwtHqNgVoNZM2hLTcaI9k?usp=sharing>`_
    * `Données traitées (format csv) <https://drive.google.com/drive/folders/1ZtwsmsefogTsO0_kr_PFlmX0hW0a6sMa?usp=drive_link>`_

2. Téléchargez tous les fichiers
3. Placez les fichiers téléchargés dans le dossier ``data/raw`` de votre projet

Prérequis
---------
Avant de commencer, assurez-vous d'avoir:

1. Python 3.8 ou supérieur installé sur votre ordinateur
2. Les bibliothèques nécessaires installées. Pour cela, ouvrez un terminal et tapez::

    pip install -r requirements.txt

Comment Démarrer
--------------

1. **Préparation des données**:
    
    Ouvrez un terminal dans le dossier du projet et tapez::

        python scripts/prepare_data.py

    Cette étape va:
    * Convertir les données brutes en format CSV
    * Nettoyer les données aberrantes
    * Créer des fichiers prêts à l'analyse

2. **Visualisation des analyses**:

    Dans le même terminal, tapez::

        python scripts/visualize.py

    Cela va générer:
    * Des graphiques de tendance pour chaque capteur
    * Des corrélations entre les différentes mesures
    * Les graphiques seront sauvegardés dans le dossier ``results/figures``

3. **Lancement des prédictions**:

    Toujours dans le terminal::

        python scripts/predict.py

    Cette commande va:
    * Analyser les tendances historiques
    * Générer des prédictions pour les prochaines 24h
    * Sauvegarder les résultats dans ``results/predictions``

En Cas de Problème
----------------
Si vous rencontrez des erreurs:

1. Vérifiez que tous les fichiers de données sont bien dans le dossier ``data/raw``
2. Assurez-vous que toutes les bibliothèques sont installées
3. Consultez les logs d'erreur dans le dossier ``logs``
4. Contactez le support technique à: support@hydraulique.com