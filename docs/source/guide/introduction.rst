Introduction
============

Ce projet a été développé par **Faten Saif Eddine** et **Ma Bilal** dans le cadre de la filière **Intelligence Artificielle et technologie de donnes** à l'**ENSAM**, sous la supervision du **Prof. Tawfik Masrour**. Il vise à analyser et prédire l’efficacité des systèmes hydrauliques à l’aide de modèles d’apprentissage automatique.

Qu’est-ce qu’un Système Hydraulique ?
------------------------------------
Un système hydraulique utilise un fluide sous pression pour transmettre de l’énergie et effectuer des travaux mécaniques. Ces systèmes sont essentiels dans de nombreuses applications industrielles, telles que les machines-outils, les équipements de construction, et les systèmes aéronautiques.

Composants Principaux
~~~~~~~~~~~~~~~~~~~~~
1. **Pompe Hydraulique** : Fournit un débit constant de fluide sous pression.
2. **Cylindre/Moteur Hydraulique** : Convertit l’énergie hydraulique en mouvement mécanique.
3. **Vannes** : Contrôlent la direction et la pression du fluide.
4. **Réservoir** : Stocke et restitue le fluide.
5. **Filtre** : Maintient la propreté du fluide.

Description des Capteurs
~~~~~~~~~~~~~~~~~~~~~~~
Les capteurs suivants sont utilisés pour surveiller le système :

+----------------+-------------------------+---------------+------------------+
| **Capteur**    | **Description**         | **Fréquence** | **Points/Cycle** |
+----------------+-------------------------+---------------+------------------+
| **PS1-PS6**    | Pression (Bar)          | 100 Hz        | 6000             |
| **EPS1**       | Puissance pompe (kW)    | 100 Hz        | 6000             |
| **FS1-FS2**    | Débit (L/min)           | 10 Hz         | 600              |
| **TS1-TS4**    | Température (°C)        | 1 Hz          | 60               |
| **VS1**        | Vibrations (mm/s)       | 1 Hz          | 60               |
| **CE**         | Efficacité thermique (%)| 1 Hz          | 60               |
| **SE**         | Rendement global (%)    | 1 Hz          | 60               |
+----------------+-------------------------+---------------+------------------+

Objectifs du Projet
-------------------
1. Analyser les données des capteurs pour comprendre le comportement du système.
2. Prédire l’efficacité globale (SE) à l’aide de modèles LSTM et GRU.
3. Optimiser les paramètres des capteurs pour atteindre une efficacité cible.
4. Détecter les anomalies potentielles dans les données.

.. note::
   Une démonstration visuelle de l’application Streamlit est disponible dans la vidéo :download:`streamlit_demo.webm <_static/streamlit_demo.webm>`. Consultez la section :ref:`premiers-pas` pour lancer l’application et explorer ses fonctionnalités.