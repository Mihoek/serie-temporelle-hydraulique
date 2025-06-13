Introduction
============

Qu'est-ce qu'un Système Hydraulique?
------------------------------------
Un système hydraulique utilise un fluide sous pression pour transmettre de l'énergie et réaliser des travaux mécaniques. Ces systèmes sont essentiels dans de nombreuses applications industrielles.

Composants Principaux
^^^^^^^^^^^^^^^^^^^
* **Pompe Hydraulique**: Fournit un débit constant de fluide sous pression
* **Cylindre/Moteur Hydraulique**: Convertit l'énergie hydraulique en mouvement mécanique
* **Vannes**: Contrôlent la direction et la pression du fluide
* **Réservoir**: Stocke et restitue le fluide
* **Filtre**: Maintient la propreté du fluide

Description des Capteurs
^^^^^^^^^^^^^^^^^^^^^^
+------------+------------------------+------------+-----------------+
| Capteur    | Description           | Fréquence  | Points/Cycle   |
+============+========================+============+=================+
| PS1-PS6    | Pression (Bar)        | 100 Hz     | 6000           |
+------------+------------------------+------------+-----------------+
| EPS1       | Puissance pompe (kW)  | 100 Hz     | 6000           |
+------------+------------------------+------------+-----------------+
| FS1-FS2    | Débit (L/min)        | 10 Hz      | 600            |
+------------+------------------------+------------+-----------------+
| TS1-TS4    | Température (°C)      | 1 Hz       | 60             |
+------------+------------------------+------------+-----------------+
| VS1        | Vibrations (mm/s)     | 1 Hz       | 60             |
+------------+------------------------+------------+-----------------+
| CE         | Efficacité thermique  | 1 Hz       | 60             |
+------------+------------------------+------------+-----------------+
| SE         | Rendement global (%)  | 1 Hz       | 60             |
+------------+------------------------+------------+-----------------+

Objectifs du Projet
-----------------
* **Analyse**: Analyser les données des capteurs hydrauliques
* **Prédiction**: Prédire l'efficacité du système (SE)
* **Optimisation**: Optimiser les paramètres pour une meilleure performance
