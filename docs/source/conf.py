import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Système Hydraulique'
copyright = '2025'
author = 'Your Name'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []
html_static_path = ['_static']

language = 'fr'
html_theme = 'sphinx_rtd_theme'