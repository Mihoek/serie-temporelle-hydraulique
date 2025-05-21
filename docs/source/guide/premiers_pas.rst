Premiers Pas
===========

Structure des Données
-------------------
Les données sont organisées par type de capteur:

* PS1-PS6: Pression (100 Hz)
* FS1-FS2: Débit (10 Hz)
* TS1-TS4: Température (1 Hz)
* VS1: Vibrations (1 Hz)

Chemin d'Accès aux Données
----------------------
Les données sont dans les liens suivant: 
* raw data(txt) :https://drive.google.com/drive/folders/1D6pebeI1JvbhwtHqNgVoNZM2hLTcaI9k?usp=sharing
* csv data :https://drive.google.com/drive/folders/1ZtwsmsefogTsO0_kr_PFlmX0hW0a6sMa?usp=drive_link


Comment Démarrer
--------------

1. Préparer les données::

    python scripts/prepare_data.py

2. Visualiser les premières analyses::

    python scripts/visualize.py

3. Lancer une prédiction::

    python scripts/predict.py

Exemples de Base
--------------

.. code-block:: python

    from hydraulique import load_data, analyze_sensor
    
    # Charger les données d'un capteur
    data = load_data('PS1')
    
    # Analyser un capteur
    analyze_sensor('PS1', cycle_id=0)