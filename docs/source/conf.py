# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from datetime import date

project = "Enterprise Architecture"
copyright = f"{date.today().year}, 深圳市精艺信息技术有限公司"
author = "Advisor"
release = f"{date.today().strftime('%Y.%m.%d')}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.mermaid",
]
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

source_suffix = {
    ".md": "markdown",
}
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "zh_CN"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = "企业架构"
html_theme_options = {
    "home_page_in_toc": True,
    "use_sidenotes": True,
}

# -- Options for Mermaid output -------------------------------------------------
# https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/

mermaid_version = "10.9.1"
html_js_files = [
   "js/mermaid.js",
]
