#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include, using, this
from pygments.token import Text, Comment, Literal, Operator, Keyword, Name, String

class Defs():

    gpkeywords = {
        'elliptic_curves' : 
            [ 'ellL1', 'elladd', 'ellak', 'ellan', 'ellanalyticrank', 'ellap', 'ellbil', 'ellbsd', 'ellcard', 'ellchangecurve', 'ellchangepoint', 'ellchangepointinv', 'ellconvertname', 'elldivpol', 'elleisnum', 'elleta', 'ellfactorback', 'ellformaldifferential', 'ellformalexp', 'ellformallog', 'ellformalpoint', 'ellformalw', 'ellfromeqn', 'ellfromj', 'ellgenerators', 'ellglobalred', 'ellgroup', 'ellheegner', 'ellheight', 'ellheightmatrix', 'ellidentify', 'ellinit', 'ellintegralmodel', 'ellisdivisible', 'ellisogeny', 'ellisogenyapply', 'ellisomat', 'ellisoncurve', 'ellisotree', 'ellissupersingular', 'ellj', 'elllocalred', 'elllog', 'elllseries', 'ellminimaldisc', 'ellminimalmodel', 'ellminimaltwist', 'ellmoddegree', 'ellmodulareqn', 'ellmul', 'ellneg', 'ellnonsingularmultiple', 'ellorder', 'ellordinate', 'ellpadicL', 'ellpadicbsd', 'ellpadicfrobenius', 'ellpadicheight', 'ellpadicheightmatrix', 'ellpadiclambdamu', 'ellpadiclog', 'ellpadicregulator', 'ellpadics2', 'ellperiods', 'ellpointtoz', 'ellpow', 'ellratpoints', 'ellrootno', 'ellsea', 'ellsearch', 'ellsigma', 'ellsub', 'elltamagawa', 'elltaniyama', 'elltatepairing', 'elltors', 'elltwist', 'ellweilcurve', 'ellweilpairing', 'ellwp', 'ellxn', 'ellzeta', 'ellztopoint', 'genus2red', 'hyperellcharpoly', 'hyperellpadicfrobenius', 'hyperellratpoints' ],
        'default' : 
            [ 'TeXstyle', 'breakloop', 'colors', 'compatible', 'datadir', 'debug', 'debugfiles', 'debugmem', 'echo', 'factor_add_primes', 'factor_proven', 'format', 'graphcolormap', 'graphcolors', 'help', 'histfile', 'histsize', 'lines', 'linewrap', 'log', 'logfile', 'nbthreads', 'new_galois_format', 'output', 'parisize', 'parisizemax', 'path', 'plothsizes', 'prettyprinter', 'primelimit', 'prompt', 'prompt_cont', 'psfile', 'readline', 'realbitprecision', 'realprecision', 'recover', 'secure', 'seriesprecision', 'simplify', 'sopath', 'strictargs', 'strictmatch', 'threadsize', 'threadsizemax', 'timer' ],
        'programming' : 
            [ '_eval_mnemonic', 'addhelp', 'alarm', 'alias', 'allocatemem', 'apply', 'arity', 'break', 'breakpoint', 'call', 'dbg_down', 'dbg_err', 'dbg_up', 'dbg_x', 'default', 'errname', 'error', 'export', 'exportall', 'extern', 'externstr', 'fileclose', 'fileextern', 'fileflush', 'fileopen', 'fileread', 'filereadstr', 'filewrite', 'filewrite1', 'fold', 'for', 'forcomposite', 'fordiv', 'fordivfactored', 'forell', 'forfactored', 'forpart', 'forperm', 'forprime', 'forprimestep', 'forsquarefree', 'forstep', 'forsubgroup', 'forsubset', 'forvec', 'getabstime', 'getenv', 'getheap', 'getlocalbitprec', 'getlocalprec', 'getrand', 'getstack', 'gettime', 'getwalltime', 'global', 'if', 'iferr', 'inline', 'input', 'install', 'kill', 'listcreate', 'listinsert', 'listkill', 'listpop', 'listput', 'listsort', 'local', 'localbitprec', 'localprec', 'mapdelete', 'mapget', 'mapisdefined', 'mapput', 'my', 'next', 'parapply', 'pareval', 'parfor', 'parforprime', 'parforvec', 'parploth', 'parplothexport', 'parselect', 'parsum', 'parvector', 'print', 'print1', 'printf', 'printp', 'printsep', 'printsep1', 'printtex', 'quit', 'read', 'readstr', 'readvec', 'return', 'select', 'self', 'setrand', 'strchr', 'strexpand', 'strjoin', 'strprintf', 'strsplit', 'strtex', 'strtime', 'system', 'trap', 'type', 'unexport', 'unexportall', 'uninline', 'until', 'version', 'warning', 'whatnow', 'while', 'write', 'write1', 'writebin', 'writetex' ],
        'combinatorics' : 
            [ 'binomial', 'fibonacci', 'hammingweight', 'numbpart', 'numtoperm', 'partitions', 'permorder', 'permsign', 'permtonum', 'stirling' ],
        'conversions' : 
            [ 'Col', 'Colrev', 'List', 'Map', 'Mat', 'Mod', 'Pol', 'Polrev', 'Qfb', 'Ser', 'Set', 'Str', 'Vec', 'Vecrev', 'Vecsmall', 'binary', 'bitand', 'bitneg', 'bitnegimply', 'bitor', 'bitprecision', 'bittest', 'bitxor', 'ceil', 'centerlift', 'characteristic', 'component', 'conj', 'conjvec', 'denominator', 'digits', 'exponent', 'floor', 'frac', 'fromdigits', 'imag', 'length', 'lift', 'liftall', 'liftint', 'liftpol', 'norm', 'numerator', 'oo', 'padicprec', 'precision', 'random', 'real', 'round', 'serchop', 'serprec', 'simplify', 'sizebyte', 'sizedigit', 'truncate', 'valuation', 'varhigher', 'variable', 'variables', 'varlower' ],
        'modular_symbols' : 
            [ 'msatkinlehner', 'mscosets', 'mscuspidal', 'msdim', 'mseisenstein', 'mseval', 'msfarey', 'msfromcusp', 'msfromell', 'msfromhecke', 'msgetlevel', 'msgetsign', 'msgetweight', 'mshecke', 'msinit', 'msissymbol', 'mslattice', 'msnew', 'msomseval', 'mspadicL', 'mspadicinit', 'mspadicmoments', 'mspadicseries', 'mspathgens', 'mspathlog', 'mspetersson', 'mspolygon', 'msqexpansion', 'mssplit', 'msstar', 'mstooms' ],
        'sums' : 
            [ 'asympnum', 'asympnumraw', 'contfraceval', 'contfracinit', 'derivnum', 'intcirc', 'intfuncinit', 'intnum', 'intnumgauss', 'intnumgaussinit', 'intnuminit', 'intnumromb', 'laurentseries', 'limitnum', 'prod', 'prodeuler', 'prodeulerrat', 'prodinf', 'prodnumrat', 'solve', 'solvestep', 'sum', 'sumalt', 'sumdiv', 'sumdivmult', 'sumeulerrat', 'suminf', 'sumnum', 'sumnumap', 'sumnumapinit', 'sumnuminit', 'sumnumlagrange', 'sumnumlagrangeinit', 'sumnummonien', 'sumnummonieninit', 'sumnumrat', 'sumpos' ],
        'linear_algebra' : 
            [ 'algdep', 'charpoly', 'concat', 'dirpowers', 'forqfvec', 'lindep', 'matadjoint', 'matcompanion', 'matconcat', 'matdet', 'matdetint', 'matdetmod', 'matdiagonal', 'mateigen', 'matfrobenius', 'mathess', 'mathilbert', 'mathnf', 'mathnfmod', 'mathnfmodid', 'mathouseholder', 'matid', 'matimage', 'matimagecompl', 'matimagemod', 'matindexrank', 'matintersect', 'matinverseimage', 'matinvmod', 'matisdiagonal', 'matker', 'matkerint', 'matkermod', 'matmuldiagonal', 'matmultodiagonal', 'matpascal', 'matpermanent', 'matqr', 'matrank', 'matrix', 'matrixqz', 'matsize', 'matsnf', 'matsolve', 'matsolvemod', 'matsupplement', 'mattranspose', 'minpoly', 'norml2', 'normlp', 'powers', 'qfauto', 'qfautoexport', 'qfbil', 'qfeval', 'qfgaussred', 'qfisom', 'qfisominit', 'qfjacobi', 'qflll', 'qflllgram', 'qfminim', 'qfnorm', 'qforbits', 'qfparam', 'qfperfection', 'qfrep', 'qfsign', 'qfsolve', 'seralgdep', 'setbinop', 'setintersect', 'setisset', 'setminus', 'setsearch', 'setunion', 'trace', 'vecextract', 'vecprod', 'vecsearch', 'vecsort', 'vecsum', 'vector', 'vectorsmall', 'vectorv' ],
        'symbolic_operators' : 
            [ 'add', 'adde', 'and', 'call', 'coeff', 'compr', 'concat', 'deriv', 'div', 'dive', 'divent', 'divente', 'divround', 'divrounde', 'eq', 'fact', 'ge', 'gt', 'hist', 'id', 'le', 'lt', 'mm', 'mod', 'mode', 'mul', 'mule', 'ne', 'neg', 'not', 'or', 'pl', 'pound', 'pow', 'pp', 'range', 'shiftl', 'shiftle', 'shiftr', 'shiftre', 'slice', 'sub', 'sube', 'trans' ],
        'l_functions' : 
            [ 'lfun', 'lfunabelianrelinit', 'lfunan', 'lfunartin', 'lfuncheckfeq', 'lfunconductor', 'lfuncost', 'lfuncreate', 'lfundiv', 'lfunetaquo', 'lfungenus2', 'lfunhardy', 'lfuninit', 'lfunlambda', 'lfunmfspec', 'lfunmul', 'lfunorderzero', 'lfunqf', 'lfunrootres', 'lfunsympow', 'lfuntheta', 'lfunthetacost', 'lfunthetainit', 'lfuntwist', 'lfunzeros' ],
        'algebras' : 
            [ 'algadd', 'algalgtobasis', 'algaut', 'algb', 'algbasis', 'algbasistoalg', 'algcenter', 'algcentralproj', 'algchar', 'algcharpoly', 'algdegree', 'algdim', 'algdisc', 'algdivl', 'algdivr', 'alggroup', 'alggroupcenter', 'alghasse', 'alghassef', 'alghassei', 'algindex', 'alginit', 'alginv', 'alginvbasis', 'algisassociative', 'algiscommutative', 'algisdivision', 'algisdivl', 'algisinv', 'algisramified', 'algissemisimple', 'algissimple', 'algissplit', 'alglatadd', 'alglatcontains', 'alglatelement', 'alglathnf', 'alglatindex', 'alglatinter', 'alglatlefttransporter', 'alglatmul', 'alglatrighttransporter', 'alglatsubset', 'algmakeintegral', 'algmul', 'algmultable', 'algneg', 'algnorm', 'algpoleval', 'algpow', 'algprimesubalg', 'algquotient', 'algradical', 'algramifiedplaces', 'algrandom', 'algrelmultable', 'algsimpledec', 'algsplit', 'algsplittingdata', 'algsplittingfield', 'algsqr', 'algsub', 'algsubalg', 'algtableinit', 'algtensor', 'algtomatrix', 'algtrace', 'algtype' ],
        'member_functions' : 
            [ 'a1', 'a2', 'a3', 'a4', 'a6', 'area', 'b2', 'b4', 'b6', 'b8', 'bid', 'bnf', 'c4', 'c6', 'clgp', 'codiff', 'cyc', 'diff', 'disc', 'e', 'eta', 'f', 'fu', 'gen', 'group', 'index', 'j', 'mod', 'nf', 'no', 'omega', 'orders', 'p', 'pol', 'polabs', 'r1', 'r2', 'reg', 'roots', 'sign', 't2', 'tate', 'tu', 'zk', 'zkst' ],
        'graphic' : 
            [ 'plot', 'plotbox', 'plotclip', 'plotcolor', 'plotcopy', 'plotcursor', 'plotdraw', 'plotexport', 'ploth', 'plothexport', 'plothraw', 'plothrawexport', 'plothsizes', 'plotinit', 'plotkill', 'plotlines', 'plotlinetype', 'plotmove', 'plotpoints', 'plotpointsize', 'plotpointtype', 'plotrbox', 'plotrecth', 'plotrecthraw', 'plotrline', 'plotrmove', 'plotrpoint', 'plotscale', 'plotstring', 'psdraw', 'psploth', 'psplothraw' ],
        'number_fields' : 
            [ 'bnfcertify', 'bnfdecodemodule', 'bnfinit', 'bnfisintnorm', 'bnfisnorm', 'bnfisprincipal', 'bnfissunit', 'bnfisunit', 'bnflog', 'bnflogdegree', 'bnflogef', 'bnfnarrow', 'bnfsignunit', 'bnfsunit', 'bnrL1', 'bnrchar', 'bnrclassfield', 'bnrclassno', 'bnrclassnolist', 'bnrconductor', 'bnrconductorofchar', 'bnrdisc', 'bnrdisclist', 'bnrgaloisapply', 'bnrgaloismatrix', 'bnrinit', 'bnrisconductor', 'bnrisgalois', 'bnrisprincipal', 'bnrrootnumber', 'bnrstark', 'dirzetak', 'factornf', 'galoischardet', 'galoischarpoly', 'galoischartable', 'galoisconjclasses', 'galoisexport', 'galoisfixedfield', 'galoisgetgroup', 'galoisgetname', 'galoisgetpol', 'galoisidentify', 'galoisinit', 'galoisisabelian', 'galoisisnormal', 'galoispermtopol', 'galoissubcyclo', 'galoissubfields', 'galoissubgroups', 'idealadd', 'idealaddtoone', 'idealappr', 'idealchinese', 'idealcoprime', 'idealdiv', 'idealdown', 'idealfactor', 'idealfactorback', 'idealfrobenius', 'idealhnf', 'idealintersect', 'idealinv', 'idealismaximal', 'idealispower', 'ideallist', 'ideallistarch', 'ideallog', 'idealmin', 'idealmul', 'idealnorm', 'idealnumden', 'idealpow', 'idealprimedec', 'idealprincipalunits', 'idealramgroups', 'idealred', 'idealredmodpower', 'idealstar', 'idealtwoelt', 'idealval', 'matalgtobasis', 'matbasistoalg', 'modreverse', 'newtonpoly', 'nfalgtobasis', 'nfbasis', 'nfbasistoalg', 'nfcertify', 'nfcompositum', 'nfdetint', 'nfdisc', 'nfdiscfactors', 'nfeltadd', 'nfeltdiv', 'nfeltdiveuc', 'nfeltdivmodpr', 'nfeltdivrem', 'nfeltembed', 'nfeltmod', 'nfeltmul', 'nfeltmulmodpr', 'nfeltnorm', 'nfeltpow', 'nfeltpowmodpr', 'nfeltreduce', 'nfeltreducemodpr', 'nfeltsign', 'nfelttrace', 'nfeltval', 'nffactor', 'nffactorback', 'nffactormod', 'nfgaloisapply', 'nfgaloisconj', 'nfgrunwaldwang', 'nfhilbert', 'nfhnf', 'nfhnfmod', 'nfinit', 'nfisideal', 'nfisincl', 'nfisisom', 'nfislocalpower', 'nfkermodpr', 'nfmodpr', 'nfmodprinit', 'nfmodprlift', 'nfnewprec', 'nfpolsturm', 'nfroots', 'nfrootsof1', 'nfsnf', 'nfsolvemodpr', 'nfsplitting', 'nfsubfields', 'polcompositum', 'polgalois', 'polred', 'polredabs', 'polredbest', 'polredord', 'poltschirnhaus', 'rnfalgtobasis', 'rnfbasis', 'rnfbasistoalg', 'rnfcharpoly', 'rnfconductor', 'rnfdedekind', 'rnfdet', 'rnfdisc', 'rnfeltabstorel', 'rnfeltdown', 'rnfeltnorm', 'rnfeltreltoabs', 'rnfelttrace', 'rnfeltup', 'rnfequation', 'rnfhnfbasis', 'rnfidealabstorel', 'rnfidealdown', 'rnfidealfactor', 'rnfidealhnf', 'rnfidealmul', 'rnfidealnormabs', 'rnfidealnormrel', 'rnfidealprimedec', 'rnfidealreltoabs', 'rnfidealtwoelt', 'rnfidealup', 'rnfinit', 'rnfisabelian', 'rnfisfree', 'rnfislocalcyclo', 'rnfisnorm', 'rnfisnorminit', 'rnfkummer', 'rnflllgram', 'rnfnormgroup', 'rnfpolred', 'rnfpolredabs', 'rnfpolredbest', 'rnfpseudobasis', 'rnfsteinitz', 'subgrouplist' ],
        'operators' : 
            [ 'cmp', 'divrem', 'lex', 'max', 'min', 'shift', 'shiftmul', 'sign', 'vecmax', 'vecmin' ],
        'number_theoretical' : 
            [ 'addprimes', 'bestappr', 'bestapprPade', 'bestapprnf', 'bezout', 'bigomega', 'charconj', 'chardiv', 'chareval', 'chargalois', 'charker', 'charmul', 'charorder', 'charpow', 'chinese', 'content', 'contfrac', 'contfracpnqn', 'core', 'coredisc', 'dirdiv', 'direuler', 'dirmul', 'divisors', 'divisorslenstra', 'eulerphi', 'factor', 'factorback', 'factorcantor', 'factorff', 'factorial', 'factorint', 'factormod', 'factormodDDF', 'factormodSQF', 'ffcompomap', 'ffembed', 'ffextend', 'fffrobenius', 'ffgen', 'ffinit', 'ffinvmap', 'fflog', 'ffmap', 'ffmaprel', 'ffnbirred', 'fforder', 'ffprimroot', 'gcd', 'gcdext', 'hilbert', 'isfundamental', 'ispolygonal', 'ispower', 'ispowerful', 'isprime', 'isprimepower', 'ispseudoprime', 'ispseudoprimepower', 'issquare', 'issquarefree', 'istotient', 'kronecker', 'lcm', 'logint', 'moebius', 'nextprime', 'numdiv', 'omega', 'precprime', 'prime', 'primecert', 'primecertexport', 'primecertisvalid', 'primepi', 'primes', 'qfbclassno', 'qfbcompraw', 'qfbhclassno', 'qfbnucomp', 'qfbnupow', 'qfbpowraw', 'qfbprimeform', 'qfbred', 'qfbredsl2', 'qfbsolve', 'quadclassunit', 'quaddisc', 'quadgen', 'quadhilbert', 'quadpoly', 'quadray', 'quadregulator', 'quadunit', 'ramanujantau', 'randomprime', 'removeprimes', 'sigma', 'sqrtint', 'sqrtnint', 'sumdedekind', 'sumdigits', 'znchar', 'zncharconductor', 'znchardecompose', 'znchargauss', 'zncharinduce', 'zncharisodd', 'znchartokronecker', 'znchartoprimitive', 'znconreychar', 'znconreyconductor', 'znconreyexp', 'znconreylog', 'zncoppersmith', 'znlog', 'znorder', 'znprimroot', 'znstar' ],
        'gp2c' : 
            [ 'DEBUGLEVEL', 'clone', 'copy', 'unclone' ],
        'polynomials' : 
            [ 'O', 'bezoutres', 'deriv', 'derivn', 'diffop', 'eval', 'factorpadic', 'fft', 'fftinit', 'fftinv', 'intformal', 'padicappr', 'padicfields', 'polchebyshev', 'polclass', 'polcoef', 'polcoeff', 'polcyclo', 'polcyclofactors', 'poldegree', 'poldisc', 'poldiscfactors', 'poldiscreduced', 'polgraeffe', 'polhensellift', 'polhermite', 'polinterpolate', 'poliscyclo', 'poliscycloprod', 'polisirreducible', 'pollaguerre', 'pollead', 'pollegendre', 'polmodular', 'polrecip', 'polresultant', 'polresultantext', 'polroots', 'polrootsbound', 'polrootsff', 'polrootsmod', 'polrootspadic', 'polrootsreal', 'polsturm', 'polsubcyclo', 'polsylvestermatrix', 'polsym', 'poltchebi', 'polteichmuller', 'polzagier', 'serconvol', 'serlaplace', 'serreverse', 'subst', 'substpol', 'substvec', 'sumformal', 'taylor', 'thue', 'thueinit' ],
        'gp2c_internal' : 
            [ '_avma', '_badtype', '_cast', '_cgetg', '_const', '_formatcode', '_gc_needed', '_gerepileall', '_gerepileupto', '_maxprime', '_norange', '_prec', '_stack_lim', '_strtoclosure', '_tovec', '_typedef', '_wrap' ],
        'modular_forms' : 
            [ 'getcache', 'lfunmf', 'mfDelta', 'mfEH', 'mfEk', 'mfTheta', 'mfatkin', 'mfatkineigenvalues', 'mfatkininit', 'mfbasis', 'mfbd', 'mfbracket', 'mfcoef', 'mfcoefs', 'mfconductor', 'mfcosets', 'mfcuspisregular', 'mfcusps', 'mfcuspval', 'mfcuspwidth', 'mfderiv', 'mfderivE2', 'mfdescribe', 'mfdim', 'mfdiv', 'mfeigenbasis', 'mfeigensearch', 'mfeisenstein', 'mfembed', 'mfeval', 'mffields', 'mffromell', 'mffrometaquo', 'mffromlfun', 'mffromqf', 'mfgaloisprojrep', 'mfgaloistype', 'mfhecke', 'mfheckemat', 'mfinit', 'mfisCM', 'mfisequal', 'mfisetaquo', 'mfkohnenbasis', 'mfkohnenbijection', 'mfkohneneigenbasis', 'mflinear', 'mfmanin', 'mfmul', 'mfnumcusps', 'mfparams', 'mfperiodpol', 'mfperiodpolbasis', 'mfpetersson', 'mfpow', 'mfsearch', 'mfshift', 'mfshimura', 'mfslashexpansion', 'mfspace', 'mfsplit', 'mfsturm', 'mfsymbol', 'mfsymboleval', 'mftaylor', 'mftobasis', 'mftocoset', 'mftonew', 'mftraceform', 'mftwist' ],
        'transcendental' : 
            [ 'Catalan', 'Euler', 'I', 'Pi', 'abs', 'acos', 'acosh', 'agm', 'airy', 'arg', 'asin', 'asinh', 'atan', 'atanh', 'bernfrac', 'bernpol', 'bernreal', 'bernvec', 'besselh1', 'besselh2', 'besseli', 'besselj', 'besseljh', 'besselk', 'besseln', 'bessely', 'cos', 'cosh', 'cotan', 'cotanh', 'dilog', 'eint1', 'ellE', 'ellK', 'erfc', 'eta', 'eulerfrac', 'eulerpol', 'eulervec', 'exp', 'expm1', 'gamma', 'gammah', 'gammamellininv', 'gammamellininvasymp', 'gammamellininvinit', 'hypergeom', 'hyperu', 'incgam', 'incgamc', 'lambertw', 'lngamma', 'log', 'log1p', 'polylog', 'psi', 'rootsof1', 'sin', 'sinc', 'sinh', 'sqr', 'sqrt', 'sqrtn', 'tan', 'tanh', 'teichmuller', 'theta', 'thetanullk', 'weber', 'zeta', 'zetahurwitz', 'zetamult', 'zetamultall', 'zetamultconvert', 'zetamultinit' ],

    select = [ 'linear_algebra', 'symbolic_operators', 'conversions',
        'operators', 'number_theoretical', 'elliptic_curves', 'sums',
        'transcendental', 'default', 'graphic', 'number_fields', 'polynomials',
        'l_functions', 'modular_symbols', 'modular_forms' ]


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
