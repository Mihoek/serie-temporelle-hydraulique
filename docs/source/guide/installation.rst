Installation
============

Prérequis Techniques
-------------------
1. **Python 3.13+** : Téléchargeable sur `python.org <https://www.python.org/downloads/>`_
2. **Git** : Téléchargeable sur `git-scm.com <https://git-scm.com/downloads>`_
3. **VS Code** (recommandé) : Téléchargeable sur `code.visualstudio.com <https://code.visualstudio.com/download>`_

Installation Pas à Pas
---------------------

1. Téléchargement du Projet
^^^^^^^^^^^^^^^^^^^^^^^^^^
Ouvrez un terminal (PowerShell sur Windows) et tapez::

    git clone https://github.com/Mihoek/serie-temporelle-hydraulique.git
    cd serie-temporelle-hydraulique

2. Création de l'Environnement Virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sur Windows::

    python -m venv venv
    .\venv\Scripts\activate

Sur Linux/Mac::

    python -m venv venv
    source venv/bin/activate

3. Installation des Dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Une fois l'environnement activé::

    pip install -r requirements.txt

4. Téléchargement des Données
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
a. Accédez aux liens Google Drive:
   * `Données brutes (TXT) <https://drive.google.com/drive/folders/1D6pebeI1JvbhwtHqNgVoNZM2hLTcaI9k>`_
   * `Données traitées (CSV) <https://drive.google.com/drive/folders/1ZtwsmsefogTsO0_kr_PFlmX0hW0a6sMa>`_

b. Créez les dossiers nécessaires::

    mkdir -p data/raw data/processed

c. Placez les fichiers téléchargés dans ``data/raw``

5. Configuration de la Vidéo de Démonstration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pour inclure la vidéo de démonstration::

    mkdir -p docs/source/_static/media
    cp chemin/vers/votre/video.mp4 docs/source/_static/media/streamlit_demo.mp4

Vérification de l'Installation
----------------------------
Pour vérifier l'installation::

    python -c "import pandas, numpy, tensorflow, streamlit; print('Installation réussie!')"