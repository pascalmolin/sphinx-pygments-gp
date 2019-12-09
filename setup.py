# -*- coding: utf-8 -*-
"""
Setup for gp Pygments Lexer
"""
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name='pygments-gp-lexer',
    version='1.1',
    author = 'Pascal Molin',
    author_email='molin.maths@gmail.com',
    url="https://github.com/pascalmolin/pygments-gp-lexer/",
    description="gp syntax for pygments",
    long_description=long_description,
    packages = setuptools.find_packages(),
    entry_points=
    """
    [pygments.lexers]
    gplexer = gp_lexer:gpLexer
    """
    ,
    license='MIT',
)
