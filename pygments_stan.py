""" Pygments lexer for Stan

    :copyright: Copyright 2012 Jeffrey B. Arnold
    :license: BSD, see LICENSE for details.
"""
from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Comment, Punctuation, Keyword, Name, \
     Operator, Number, Text

class StanLexer(RegexLexer):
    """ Pygments Lexer for Stan models """
    # Currently pretty hackish.  A better version would make use of
    # states for the blocks.

    name = 'STAN'
    aliases = ['stan']
    filenames = ['*.stan']

    _RESERVED = ('for', 'in', 'while', 'repeat', 'until', 'if',
                'then', 'else', 'true', 'false')

    _TYPES = ('int', 'real', 'vector', 'simplex', 'ordered', 'row_vector', 'matrix',
              'corr_matrix', 'cov_matrix')

    # STAN 1.0 Manual, Chapter 20
    _FUNCTIONS = ['T',
                  'abs', 'int_step', 'min', 'max',
                  'pi', 'e', 'sqrt2', 'log2', 'log10', 'nan', 'infinity',
                  'epsilon', 'negative_epsilon',
                  'if_else', 'step',
                  'fabs', 'fdim',
                  'fmin', 'fmax',
                  'fmod',
                  'floor', 'ceil', 'round', 'trunc',
                  'sqrt', 'cbrt', 'square', 'exp', 'exp2', 'expm1',
                  'log', 'log2', 'log10', 'pow', 'logit', 'inv_logit',
                  'inv_cloglog', 'hypot', 'cos', 'sin', 'tan', 'acos',
                  'asin', 'atan', 'atan2', 'cosh', 'sinh', 'tanh',
                  'acosh', 'asinh', 'atanh', 'erf', 'erfc', 'Phi',
                  'log_loss', 'tgamma', 'lgamma', 'lmgamma', 'lbeta',
                  'binomial_coefficient_log',
                  'fma', 'multiply_log', 'log1p', 'log1m', 'log1p_exp', 'log_sum_exp',
                  'rows', 'cols',
                  'dot_product', 'prod', 'mean', 'variance', 'sd',
                  'diagonal', 'diag_matrix', 'col', 'row',
                  'softmax', 'trace', 'determinant', 'inverse', 'eigenvalue',
                  'eigenvalues_sym', 'cholesky', 'singular_values',
                  '(log)?normal_p', 'exponential_p', 'gamma_p', 'weibull_p']
    _DISTRIBUTIONS = ['bernoulli', 'bernoulli_logit',
                      'beta_binomial', 'hypergeometric', 'categorical',
                      'ordered_logistic', 'negative_binomial', 'poisson',
                      'multinomial', 'normal', 'student_t',
                      'cauchy', 'double_exponential', 'logistic',
                      'lognormal', 'chi_square', 'inv_chi_square',
                      'scaled_inv_chi_square', 'exponential',
                      'gamma', 'inv_gamma', 'weibull', 'pareto',
                      'beta', 'uniform', 'dirichlet', 'multi_normal',
                      'multi_normal_cholesky', 'multi_student_t',
                      'wishart', 'inv_wishart', 'lkj_cov',
                      'lkj_corr_cholesky']

    def _regex_keywords(x):
        return r'\b(%s)\b' % r'|'.join(x)

    tokens = {
        'whitespace' : [
            (r"\s+", Text),
            ],
        'comments' : [
            # do not use stateful comments
            (r'(?s)/\*.*?\*/', Comment.Multiline),
            # Comments
            (r'(//|#).*$', Comment.Single),
            ],
        'root': [
            # Comments
            include('comments'),
            # block start
            include('whitespace'),
            # Block start
            (r'(?s)(%s)(\s*)({)' %
             r'|'.join(('data', r'transformed\s+?data',
                        'parameters', r'transformed\s+parameters',
                        'model', r'generated\s+quantities')),
             bygroups(Keyword.Namespace, Text, Punctuation), 'block')
        ],
        'block' : [
            include('comments'),
            include('whitespace'),
            # Reserved Words
            (_regex_keywords(_RESERVED), Keyword.Reserved),
            # Data types
            (_regex_keywords(_TYPES), Keyword.Type),
            # Punctuation
            (r"[;:,\[\]()]", Punctuation),
            # Builtin
            (r'(%s)(?=\s*\()'
             % r'|'.join(_FUNCTIONS
                         + _DISTRIBUTIONS 
                         + ['%s_log' % x for x in _DISTRIBUTIONS]),
             Name.Builtin),
            # Special names ending in __, like lp__
            (r'\b[A-Za-z][A-Za-z0-9_]*__\b', Name.Builtin.Pseudo),
            # Regular variable names
            (r'\b[A-Za-z][A-Za-z0-9_]*\b', Name),
            # Real Literals
            (r'-?[0-9]+(\.[0-9]+)?[eE]-?[0-9]+', Number.Float),
            (r'-?[0-9]*\.[0-9]*', Number.Float),
            # Integer Literals
            (r'-?[0-9]+', Number.Integer),
            # Assignment operators
            # SLexer makes these tokens Operators. 
            (r'(<-|~)', Operator),
            # Infix and prefix operators
            (r"(\+|-|\.?\*|\.?/|//')", Operator),
            # Block
            (r'{', Punctuation, '#push'),
            (r'}', Punctuation, '#pop'),
            ]
        }
