# Configuration file for Sphinx documentation builder

project = 'Math Textbook'
copyright = '2026'
author = 'Michael McCabe'
release = '1.0.0'
version = '1.0.0'

# Extensions for rich content and accessibility
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_design',
    'sphinx_tags',
    'sphinxcontrib.video',
    'numpydoc',
    'sphinx_accessibility',
    'sphinx_tabs.tabs',
    'sphinx_togglebutton',
    'sphinx_copybutton',
    'sphinxext.opengraph',
    'sphinxcontrib.tikz',
]

# MyST parser configuration for Markdown support
myst_enable_extensions = [
    'amsmath',
    'dollarmath',
    'linkify',
    'colon_fence',
    'deflist',
    'html_image',
    'replacements',
]

myst_fence_as_directive = ['mermaid', 'tikz']

# HTML output configuration
html_theme = 'sphinx_book_theme'

html_theme_options = {
    'show_toc_level': 1,
    'collapse_navigation': True,
    'show_prev_next': True,
    'use_repository_button': True,
    'use_issues_button': True,
    'repository_url': 'https://github.com/codmccabe/sphinxTemplate2.0',
    'repository_branch': 'main',
    'path_to_docs': 'doc',
    'home_page_in_toc': True,
    'footer_content_items': [],
    'announcement': '',
    # Accessibility options
    'navigation_with_keys': True,
    'extra_footer': '',
    'secondary_sidebar_items': ['page-toc'],
}

# Build configuration
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# Highlight configuration
highlight_language = 'python3'
pygments_style = 'sphinx'

# HTML output options
html_static_path = ['_static']
html_logo = None
html_favicon = None
html_use_opensearch = ''

# LaTeX output for PDF generation
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'preamble': r'''
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{unicode}
        \usepackage[utf8]{inputenc}
    ''',
    'fncychap': r'\usepackage[Bjornstyle]{fncychap}',
}

latex_documents = [
    (master_doc, 'textbook.tex', project, author, 'manual'),
]

# Intersphinx for cross-referencing
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    #'numpy': ('https://numpy.org/doc/stable', None),
    #'scipy': ('https://docs.scipy.org/doc/scipy', None),
    #'matplotlib': ('https://matplotlib.org/stable', None),
}

# Suppress certain warnings
suppress_warnings = ['app.add_config_value']

# TikZ configuration
tikz_tikzlibraries = 'arrows,automata,backgrounds,calc,fit,matrix,mindmap,patterns,petri,positioning,shapes,shapes.geometric,shapes.misc,trees'
tikz_latex_preamble = r'\usepackage{amsmath}\usepackage{amssymb}'
tikz_proc_suite = 'pdf2svg'
tikz_transparent = True
tikz_latex_engine = 'pdflatex'
# Ensure white background
tikz_latex_preamble += r'\pagecolor{white}\color{black}'

# Custom CSS and JS for improved accessibility and lightbox
def setup(app):
    app.add_css_file('custom_accessibility.css')
    app.add_css_file('https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css')
    app.add_js_file('https://cdn.jsdelivr.net/npm/glightbox/dist/js/glightbox.min.js')
    app.add_js_file('lightbox_init.js')
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }