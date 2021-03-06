#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include, using, this
from pygments.token import Text, Comment, Literal, Operator, Keyword, Name, String


class Defs():

    from .keywords import gpkeywords

    select = [ 'linear_algebra',
               #'symbolic_operators',
               'conversions',
               'operators',
               'number_theoretical',
               'elliptic_curves',
               'sums',
               'transcendental',
               'default',
               'graphic',
               'number_fields',
               'polynomials',
               'l_functions',
               'modular_symbols',
               'modular_forms'
               ]


class gpLexer(RegexLexer):
    name = 'gp'
    aliases = ['gp', 'GP']
    filenames = ['*.gp']

    """
    all gp keywords, generated by::

      perl get_gp_keywords <path-to-file src/funclist>

    """
    # white spaces and comments
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

    tokens = {
        'whitespace': [
          (r'\n', Text),
          (r'\s+', Text),
          (r'\\\\(\n|(.|\n)*?[^\\]\n)', Comment.Single),
          (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
          ],
        'root': [
          include('whitespace'),
          # directive
          (r'(\\(?:ps?|g|q|r|o|l))',Comment.Preproc),
          # string
          (r'"', String, 'string'),
          # function declaration
          #(r'[a-zA-Z_][a-zA-Z0-9_]*', Name.Function)
          (r'(\w+)(?:\s*)(\()(.*?)(\))(?:\s*)(=)', bygroups( Name.Function,
            Text, using(this), Text, Operator)),#, 'function'),
          # operators
          (r'(-|\+|\*|/|[=!]=?|[<>]=?|\&\&?|\|\|?)', Operator),
          # keywords
          (r'\b('+'|'.join(Defs.gpkeywords['programming'])+r')\b', Keyword),
          # built-in functions
          (r'\b('+'|'.join( sum( [Defs.gpkeywords[s] for s in Defs.select], []))+r')\b', Name.Builtin),

          #(r'', Text, 'statement'),
          (r'.', Text),
          ],
        'string': [
          include('whitespace'),
          (r'"', String, '#pop'),
          (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
          (r'[^\\"\n]+', String), # all other characters
          (r'\\\n', String), # line continuation
          (r'\\', String), # stray backslash
          ]
          ,
        #'function': [
        #  include('whitespace'),
        #  include('comments'),
        #  (';', Punctuation),
        #  (r'{', Keyword, '#push'),
        #  (r'}', Keyword, '#pop'),
        #  ]
        }


#class gpLexer(RegexLexer):
#  name = 'gp'
#  aliases = ['GP']
#  filenames = ['*.gp']
#
#  """ all gp keywords, grouped by gp subtopics 1-12 """
#  keywords = [
#      """ 0 : user-defined """
#      [],
#      """ 1 : operators """
#      ["cmp", "divrem", "lex", " max", "min", "shift", "shiftmul", "sign", "vecmax", "vecmin"],
#      """ 2 : conversions """
#      """ 3 : transcendental """
#      """ 4 : number theory """
#      """ 5 : elliptic curves """
#      """ 6 : number fields """
#      """ 7 : polynomials and power series """
#      """ 8 : linear algebra """
#      """ 9 : sums """
#      """ 10 : graphics """
#      """ 11-a : programming structures """
#      """ 11-b : programming others """
#      ]
#
#  # white spaces and comments
#  _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'
#
#  tokens = {
#      'whitespace': [
#        (r'\n', Text),
#        (r'\s+', Text),
#        (r'//(\n|(.|\n)*?[^\\]\n)', Comment.Single),
#        (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
#        ],
#      'statements': [
#        (r'"', String, 'string'),
#        ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
#        ],
#      'root': [
#        include('whitespace'),
#        # directive
#        (r'(\\(?:ps?|g|q|r|o|l))',Comment.Preproc),
#        # function declaration
#        (r'[a-zA-Z_][a-zA-Z0-9_]*', Name)
#        (r'(\w+)(\s*)\(.*?\)(=)',
#          bygroups( Name, Text, Keyword, Operator),
#          'function'),
#        (r'', Text, 'statement'),
#        ],
#      'statement': [
#
#        ]
#      'string': [
#        include('comments'),
#        (r'"', String, '#pop'),
#        (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
#        (r'[^\\"\n]+', String), # all other characters
#        (r'\\\n', String), # line continuation
#        (r'\\', String), # stray backslash
#        ]
#      'function': [
#        include('whitespace'),
#        include('comments'),
#        (';', Punctuation),
#        (r'{', Keyword, '#push'),
#        (r'}', Keyword, '#pop'),
#        ]
#      }
#
#
#
