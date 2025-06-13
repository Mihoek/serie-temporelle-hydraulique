
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'serie-temporelle-hydraulique'
copyright = '2025, Mihoek'
author = 'Mihoek'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath',  
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', '_static/media']  

# Configuration pour les fichiers statiques
html_extra_path = ['_static/media'] 
html_context = {
    'css_files': [
        '_static/css/custom.css',  
    ],
}
