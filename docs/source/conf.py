import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'Analyse Prédictive des Systèmes Hydrauliques'
copyright = '2025,Faten Saif Eddine, Ma Bilal'
author = 'Faten Saif Eddine, Ma Bilal'
release = '2.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

# Change theme to Read the Docs
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme customization
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
    # Navigation options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Additional HTML settings
html_logo = None  # Add your logo path if you have one
html_favicon = None  # Add your favicon path if you have one
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

language = 'fr'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Custom CSS
html_css_files = [
    'custom.css',
]