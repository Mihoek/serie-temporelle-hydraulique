Premiers Pas
===========

Accès aux Données
---------------

Structure des Données sur Google Drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Les fichiers sont organisés comme suit:

* **Models/** : Modèles entraînés LSTM et GRU
* **Data_txt/** : Données brutes au format TXT
* **Data_long/** : Données prétraitées format long
* **Data_csv/** : Données traitées au format CSV

Utilisation de l'Application
--------------------------

1. Lancer l'Application
^^^^^^^^^^^^^^^^^^^^^
Dans le terminal::

    streamlit run app.py

2. Interface Principale
^^^^^^^^^^^^^^^^^^^^
L'application propose quatre sections:

a. **Tableau de Bord**
    * Vue d'ensemble des données
    * Graphiques de tendance
    * Corrélations entre capteurs

b. **Chatbot**
    * Assistant conversationnel
    * Questions en langage naturel
    * Exemples: "Prédire SE" ou "Optimiser SE"

c. **Prédiction SE**
    * Entrée des valeurs des capteurs
    * Prédiction d'efficacité
    * Comparaison LSTM/GRU

d. **Prédiction Inverse**
    * Définition d'efficacité cible
    * Paramètres recommandés

Dépannage
---------
1. Vérifier l'environnement virtuel
2. Vérifier les fichiers dans ``data/raw``
3. Vérifier les dépendances installées
4. Consulter les logs d'erreur