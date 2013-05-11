# -*- coding: utf-8 -*-
"""
Setup for gp Pygments Lexer
"""
from setuptools import setup
 
setup(
    name='gp Pygments Lexer',
    version='1.0',
    author = 'molinp@math.jussieu.fr',
    packages=['gp_lexer'],
    entry_points="""
    [pygments.lexers]
    gplexer = gp_lexer:gpLexer
    """
)

setup(
    name='LaTeX Pygments formatter',
    version='1.0',
    author = 'molinp@math.jussieu.fr',
    packages=['latex_formatter'],
    entry_points="""
    [pygments.formatters]
    latex_formatter = latex_formatter:LatexFormatter
    """
)
