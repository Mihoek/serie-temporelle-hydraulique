

import os
import sys


sys.path.insert(0, os.path.abspath('../..'))


project = 'Analyse Prédictive des Systèmes Hydrauliques'
copyright = '2025, Jean Dupont, Marie Martin'
author = 'Jean Dupont, Marie Martin'
release = '1.0'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

html_theme = 'alabaster'
html_static_path = ['_static']


html_theme_options = {
    'description': 'Projet de prédiction des systèmes hydrauliques avec Streamlit',
    'github_user': 'Mihoek',
    'github_repo': 'serie-temporelle-hydraulique',
    'github_button': True,
}


language = 'fr'


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']