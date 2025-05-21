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
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']