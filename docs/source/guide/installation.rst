Installation
===========

Prérequis
---------
1. Python 3.10 ou supérieur
2. Git (pour cloner le projet)

Installation Étape par Étape
--------------------------

1. Cloner le projet::

    git clone https://github.com/Mihoek/serie-temporelle-hydraulique.git
    cd serie-temporelle-hydraulique

2. Créer un environnement virtuel::

    python -m venv venv
    
    # Sur Windows
    .\venv\Scripts\activate
    
    # Sur Linux/Mac
    source venv/bin/activate

3. Installer les dépendances::

    pip install -r requirements.txt

Vérification de l'Installation
---------------------------
Pour vérifier que tout est bien installé::

    python -c "import pandas; import numpy; import matplotlib; print('Installation réussie!')"