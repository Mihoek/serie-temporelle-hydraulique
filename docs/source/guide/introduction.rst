Introduction
============

Qu'est-ce qu'un Système Hydraulique?
------------------------------------
Un système hydraulique utilise un fluide sous pression pour transmettre de l'énergie et réaliser des travaux mécaniques. Ces systèmes sont essentiels dans de nombreuses applications industrielles.

Composants Principaux
^^^^^^^^^^^^^^^^^^^
1. **Pompe Hydraulique**: Fournit un débit constant de fluide sous pression
2. **Cylindre/Moteur Hydraulique**: Convertit l'énergie hydraulique en mouvement mécanique
3. **Vannes**: Contrôlent la direction et la pression du fluide
4. **Réservoir**: Stocke et restitue le fluide
5. **Filtre**: Maintient la propreté du fluide

Description des Capteurs
^^^^^^^^^^^^^^^^^^^^^^
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
------------------
1. Analyser les données des capteurs hydrauliques
2. Prédire l'efficacité du système (SE)
3. Optimiser les paramètres pour une meilleure performance


Démonstration de l'Application
-----------------------------
Une capture vidéo de l'application Streamlit illustre les fonctionnalités du projet, incluant le tableau de bord, les prédictions d'efficacité, et l'interface du chatbot. Consultez la section :ref:`demonstration-video` dans les "Premiers Pas" pour visionner la vidéo.