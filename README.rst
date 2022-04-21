# pygments-gp-lexer

simple pygments lexer for Pari/GP http://pari.math.u-bordeaux.fr

## installation

::

  pip install .

or

::

  python setup.py install


## develop

To update the list of keywords::

  FUNCLIST=~/git/paridev/src/funclist
  perl get_gp_funclist.pl $FUNCLIST > gp_lexer/keywords.py

