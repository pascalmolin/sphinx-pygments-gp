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
