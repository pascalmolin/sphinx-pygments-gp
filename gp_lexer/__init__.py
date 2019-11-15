#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include, using, this
from pygments.token import Text, Comment, Literal, Operator, Keyword, Name, String

class Defs():

  gpkeywords = {
    'linear_algebra' : 
    [ 'algdep', 'charpoly', 'concat', 'forqfvec', 'lindep', 'listcreate',
      'listinsert', 'listkill', 'listpop', 'listput', 'listsort', 'matadjoint',
      'matcompanion', 'matconcat', 'matdet', 'matdetint', 'matdiagonal',
      'mateigen', 'matfrobenius', 'mathess', 'mathilbert', 'mathnf',
      'mathnfmod', 'mathnfmodid', 'matid', 'matimage', 'matimagecompl',
      'matindexrank', 'matintersect', 'matinverseimage', 'matisdiagonal',
      'matker', 'matkerint', 'matmuldiagonal', 'matmultodiagonal', 'matpascal',
      'matrank', 'matrix', 'matrixqz', 'matsize', 'matsnf', 'matsolve',
      'matsolvemod', 'matsupplement', 'mattranspose', 'minpoly', 'qfgaussred',
      'qfjacobi', 'qflll', 'qflllgram', 'qfminim', 'qfperfection', 'qfrep',
      'qfsign', 'setbinop', 'setintersect', 'setisset', 'setminus',
      'setsearch', 'setunion', 'trace', 'vecextract', 'vecsearch', 'vecsort',
      'vector', 'vectorsmall', 'vectorv' ],
    'symbolic_operators' : 
    [ 'add', 'adde', 'and', 'call', 'coeff', 'compr', 'concat', 'deriv', 'div',
      'dive', 'divent', 'divente', 'divround', 'divrounde', 'eq', 'fact', 'ge',
      'gt', 'hist', 'id', 'le', 'lt', 'mm', 'mod', 'mode', 'mul', 'mule', 'ne',
      'neg', 'not', 'or', 'pl', 'pound', 'pow', 'pp', 'range', 'shiftl',
      'shiftle', 'shiftr', 'shiftre', 'slice', 'sub', 'sube', 'trans' ],
    'conversions' : 
    [ 'Col', 'List', 'Mat', 'Mod', 'Pol', 'Polrev', 'Qfb', 'Ser', 'Set', 'Str',
      'Strchr', 'Strexpand', 'Strprintf', 'Strtex', 'Vec', 'Vecrev',
      'Vecsmall', 'binary', 'bitand', 'bitneg', 'bitnegimply', 'bitor',
      'bittest', 'bitxor', 'ceil', 'centerlift', 'component', 'conj',
      'conjvec', 'denominator', 'digits', 'floor', 'frac', 'hammingweight',
      'imag', 'length', 'lift', 'norm', 'norml2', 'numerator', 'numtoperm',
      'padicprec', 'permtonum', 'precision', 'random', 'real', 'round',
      'simplify', 'sizebyte', 'sizedigit', 'truncate', 'valuation', 'variable'
      ],
    'programming' : 
    [ '_eval_mnemonic', 'addhelp', 'alarm', 'alias', 'allocatemem', 'apply',
      'break', 'breakpoint', 'dbg_down', 'dbg_err', 'dbg_up', 'dbg_x',
      'default', 'errname', 'error', 'extern', 'externstr', 'for',
      'forcomposite', 'fordiv', 'forell', 'forpart', 'forprime', 'forstep',
      'forsubgroup', 'forvec', 'getenv', 'getheap', 'getrand', 'getstack',
      'gettime', 'global', 'if', 'iferr', 'iferrname', 'input', 'install',
      'kill', 'local', 'my', 'next', 'print', 'print1', 'printf', 'printsep',
      'printtex', 'quit', 'read', 'readvec', 'return', 'select', 'setrand',
      'system', 'trap', 'type', 'until', 'version', 'warning', 'whatnow',
      'while', 'write', 'write1', 'writebin', 'writetex' ],
    'operators' : 
    [ 'cmp', 'divrem', 'lex', 'max', 'min', 'shift', 'shiftmul', 'sign',
      'vecmax', 'vecmin' ],
    'number_theoretical' : 
    [ 'addprimes', 'bestappr', 'bestapprPade', 'bezout', 'bezoutres',
      'bigomega', 'binomial', 'chinese', 'content', 'contfrac', 'contfracpnqn',
      'core', 'coredisc', 'dirdiv', 'direuler', 'dirmul', 'divisors',
      'eulerphi', 'factor', 'factorback', 'factorcantor', 'factorff',
      'factorial', 'factorint', 'factormod', 'ffgen', 'ffinit', 'fflog',
      'ffnbirred', 'fforder', 'ffprimroot', 'fibonacci', 'gcd', 'hilbert',
      'isfundamental', 'ispolygonal', 'ispower', 'ispowerful', 'isprime',
      'isprimepower', 'ispseudoprime', 'issquare', 'issquarefree', 'istotient',
      'kronecker', 'lcm', 'moebius', 'nextprime', 'numbpart', 'numdiv',
      'omega', 'partitions', 'polrootsff', 'precprime', 'prime', 'primepi',
      'primes', 'qfbclassno', 'qfbcompraw', 'qfbhclassno', 'qfbnucomp',
      'qfbnupow', 'qfbpowraw', 'qfbprimeform', 'qfbred', 'qfbsolve',
      'quadclassunit', 'quaddisc', 'quadgen', 'quadhilbert', 'quadpoly',
      'quadray', 'quadregulator', 'quadunit', 'randomprime', 'removeprimes',
      'sigma', 'sqrtint', 'stirling', 'sumdedekind', 'sumdigits',
      'zncoppersmith', 'znlog', 'znorder', 'znprimroot', 'znstar' ],
    'gp2c' : 
    [ 'DEBUGLEVEL', 'clone', 'copy', 'unclone' ],
    'elliptic_curves' : 
    [ 'ellL1', 'elladd', 'ellak', 'ellan', 'ellanalyticrank', 'ellap',
        'ellbil', 'ellcard', 'ellchangecurve', 'ellchangepoint',
        'ellconvertname', 'elldivpol', 'elleisnum', 'elleta', 'ellffinit',
        'ellfromj', 'ellgenerators', 'ellglobalred', 'ellgroup', 'ellheegner',
        'ellheight', 'ellheightmatrix', 'ellidentify', 'ellinit',
        'ellisoncurve', 'ellj', 'elllocalred', 'elllog', 'elllseries',
        'ellminimalmodel', 'ellmodulareqn', 'ellmul', 'ellneg', 'ellorder',
        'ellordinate', 'ellpointtoz', 'ellpow', 'ellrootno', 'ellsearch',
        'ellsigma', 'ellsub', 'elltaniyama', 'elltatepairing', 'elltors',
        'ellweilpairing', 'ellwp', 'ellzeta', 'ellztopoint' ],
    'sums' : 
    [ 'derivnum', 'intcirc', 'intfouriercos', 'intfourierexp', 'intfouriersin',
        'intfuncinit', 'intlaplaceinv', 'intmellininv', 'intmellininvshort',
        'intnum', 'intnuminit', 'intnuminitgen', 'intnumromb', 'intnumstep',
        'prod', 'prodeuler', 'prodinf', 'solve', 'sum', 'sumalt', 'sumdiv',
        'suminf', 'sumnum', 'sumnumalt', 'sumnuminit', 'sumpos' ],
    'transcendental' : 
    [ 'Catalan', 'Euler', 'I', 'Pi', 'abs', 'acos', 'acosh', 'agm', 'arg',
        'asin', 'asinh', 'atan', 'atanh', 'bernfrac', 'bernpol', 'bernreal',
        'bernvec', 'besselh1', 'besselh2', 'besseli', 'besselj', 'besseljh',
        'besselk', 'besseln', 'cos', 'cosh', 'cotan', 'dilog', 'eint1', 'erfc',
        'eta', 'exp', 'gamma', 'gammah', 'hyperu', 'incgam', 'incgamc',
        'lngamma', 'log', 'polylog', 'psi', 'sin', 'sinh', 'sqr', 'sqrt',
        'sqrtn', 'tan', 'tanh', 'teichmuller', 'theta', 'thetanullk', 'weber',
        'zeta' ],
    'default' : 
    [ 'TeXstyle', 'breakloop', 'colors', 'compatible', 'datadir', 'debug',
        'debugfiles', 'debugmem', 'echo', 'factor_add_primes', 'factor_proven',
        'format', 'graphcolormap', 'graphcolors', 'help', 'histfile',
        'histsize', 'lines', 'linewrap', 'log', 'logfile', 'new_galois_format',
        'output', 'parisize', 'path', 'prettyprinter', 'primelimit', 'prompt',
        'prompt_cont', 'psfile', 'readline', 'realprecision', 'recover',
        'secure', 'seriesprecision', 'simplify', 'sopath', 'strictmatch',
        'timer' ],
    'graphic' : 
    [ 'plot', 'plotbox', 'plotclip', 'plotcolor', 'plotcopy', 'plotcursor',
        'plotdraw', 'ploth', 'plothraw', 'plothsizes', 'plotinit', 'plotkill',
        'plotlines', 'plotlinetype', 'plotmove', 'plotpoints', 'plotpointsize',
        'plotpointtype', 'plotrbox', 'plotrecth', 'plotrecthraw', 'plotrline',
        'plotrmove', 'plotrpoint', 'plotscale', 'plotstring', 'psdraw',
        'psploth', 'psplothraw' ],
    'number_fields' : 
    [ 'bnfcertify', 'bnfcompress', 'bnfdecodemodule', 'bnfinit',
        'bnfisintnorm', 'bnfisnorm', 'bnfisprincipal', 'bnfissunit',
        'bnfisunit', 'bnfnarrow', 'bnfsignunit', 'bnfsunit', 'bnrL1',
        'bnrclassno', 'bnrclassnolist', 'bnrconductor', 'bnrconductorofchar',
        'bnrdisc', 'bnrdisclist', 'bnrinit', 'bnrisconductor',
        'bnrisprincipal', 'bnrrootnumber', 'bnrstark', 'dirzetak', 'factornf',
        'galoisexport', 'galoisfixedfield', 'galoisgetpol', 'galoisidentify',
        'galoisinit', 'galoisisabelian', 'galoisisnormal', 'galoispermtopol',
        'galoissubcyclo', 'galoissubfields', 'galoissubgroups', 'idealadd',
        'idealaddtoone', 'idealappr', 'idealchinese', 'idealcoprime',
        'idealdiv', 'idealfactor', 'idealfactorback', 'idealfrobenius',
        'idealhnf', 'idealintersect', 'idealinv', 'ideallist', 'ideallistarch',
        'ideallog', 'idealmin', 'idealmul', 'idealnorm', 'idealnumden',
        'idealpow', 'idealprimedec', 'idealramgroups', 'idealred', 'idealstar',
        'idealtwoelt', 'idealval', 'matalgtobasis', 'matbasistoalg',
        'modreverse', 'newtonpoly', 'nfalgtobasis', 'nfbasis', 'nfbasistoalg',
        'nfdetint', 'nfdisc', 'nfeltadd', 'nfeltdiv', 'nfeltdiveuc',
        'nfeltdivmodpr', 'nfeltdivrem', 'nfeltmod', 'nfeltmul',
        'nfeltmulmodpr', 'nfeltnorm', 'nfeltpow', 'nfeltpowmodpr',
        'nfeltreduce', 'nfeltreducemodpr', 'nfelttrace', 'nfeltval',
        'nffactor', 'nffactorback', 'nffactormod', 'nfgaloisapply',
        'nfgaloisconj', 'nfhilbert', 'nfhnf', 'nfhnfmod', 'nfinit',
        'nfisideal', 'nfisincl', 'nfisisom', 'nfkermodpr', 'nfmodprinit',
        'nfnewprec', 'nfroots', 'nfrootsof1', 'nfsnf', 'nfsolvemodpr',
        'nfsubfields', 'polcompositum', 'polgalois', 'polred', 'polredabs',
        'polredbest', 'polredord', 'poltschirnhaus', 'rnfalgtobasis',
        'rnfbasis', 'rnfbasistoalg', 'rnfcharpoly', 'rnfconductor',
        'rnfdedekind', 'rnfdet', 'rnfdisc', 'rnfeltabstorel', 'rnfeltdown',
        'rnfeltreltoabs', 'rnfeltup', 'rnfequation', 'rnfhnfbasis',
        'rnfidealabstorel', 'rnfidealdown', 'rnfidealhnf', 'rnfidealmul',
        'rnfidealnormabs', 'rnfidealnormrel', 'rnfidealreltoabs',
        'rnfidealtwoelt', 'rnfidealup', 'rnfinit', 'rnfisabelian', 'rnfisfree',
        'rnfisnorm', 'rnfisnorminit', 'rnfkummer', 'rnflllgram',
        'rnfnormgroup', 'rnfpolred', 'rnfpolredabs', 'rnfpseudobasis',
        'rnfsteinitz', 'subgrouplist', 'zetak', 'zetakinit' ],
    'gp2c_internal' : 
    [ '_avma', '_badtype', '_cast', '_cgetg', '_const', '_formatcode',
        '_gerepileall', '_gerepileupto', '_maxprime', '_stack_lim',
        '_strtoclosure', '_tovec', '_typedef', '_wrap' ],
    'polynomials' : 
    [ 'O', 'deriv', 'diffop', 'eval', 'factorpadic', 'intformal', 'padicappr',
        'padicfields', 'polchebyshev', 'polcoeff', 'polcyclo',
        'polcyclofactors', 'poldegree', 'poldisc', 'poldiscreduced',
        'polgraeffe', 'polhensellift', 'polhermite', 'polinterpolate',
        'poliscyclo', 'poliscycloprod', 'polisirreducible', 'pollead',
        'pollegendre', 'polrecip', 'polresultant', 'polroots', 'polrootsmod',
        'polrootspadic', 'polsturm', 'polsubcyclo', 'polsylvestermatrix',
        'polsym', 'poltchebi', 'polzagier', 'serconvol', 'serlaplace',
        'serreverse', 'subst', 'substpol', 'substvec', 'sumformal', 'taylor',
        'thue', 'thueinit' ],
    'member_functions' : 
    [ 'a1', 'a2', 'a3', 'a4', 'a6', 'area', 'b2', 'b4', 'b6', 'b8', 'bid',
        'bnf', 'c4', 'c6', 'clgp', 'codiff', 'cyc', 'diff', 'disc', 'e', 'eta',
        'f', 'fu', 'futu', 'gen', 'group', 'index', 'j', 'mod', 'nf', 'no',
        'omega', 'orders', 'p', 'pol', 'r1', 'r2', 'reg', 'roots', 'sign',
        't2', 'tate', 'tu', 'tufu', 'w', 'zk', 'zkst' ],
    }

  select = [ 'linear_algebra', 'symbolic_operators', 'conversions',
      'operators', 'number_theoretical', 'elliptic_curves', 'sums',
      'transcendental', 'default', 'graphic', 'number_fields', 'polynomials' ]


class gpLexer(RegexLexer):
  name = 'gp'
  aliases = ['gp', 'GP']
  filenames = ['*.gp']

  """
  all gp keywords, generated by
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
