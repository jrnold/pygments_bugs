""" Pygments lexer for Stan

    :copyright: Copyright 2012 Jeffrey B. Arnold
    :license: BSD, see LICENSE for details.
"""
from pygments.lexer import RegexLexer, include
from pygments.token import *

RESERVED = ('for', 'in', 'while', 'repeat', 'until', 'if',
            'then', 'else', 'true', 'false', 'T')

BLOCKS = ('data', 'transformed data', 'parameters', 'transformed parameters',
          'model', 'generated quantities')

TYPES = ('int', 'real', 'vector', 'simplex', 'ordered', 'row_vector', 'matrix',
         'corr_matrix', 'cov_matrix')

def _regex_keywords(x):
    return r'\b(%s)\b' % r'|'.join(x)

class StanLexer(RegexLexer):
    """ Pygments Lexer for Stan models """
    # Currently pretty hackish.  A better version would make use of
    # states for the blocks.

    name = 'STAN'
    aliases = ['stan']
    filenames = ['*.stan']

    tokens = {
        'comments' : [
            # do not use stateful comments
            (r'(?s)/\*.*?\*/', Comment.Multiline),
            # Comments
            (r'(//|#).*$', Comment.Single),
            ],
        'root': [
            # Comments
            include('comments'),
            # Block identifiers
            (_regex_keywords(BLOCKS), Keyword.Namespace),
            # Whitespace
            (r"\s+", Text),
            # Block
            (r'{', Punctuation, 'block')
        ],
        'block' : [
            include('comments'),
            (r"\s+", Text),
            # Reserved Words
            (_regex_keywords(RESERVED), Keyword.Reserved),
            # Data types
            (_regex_keywords(TYPES), Keyword.Type),
            (r'{', Punctuation, 'block'),
            # Punctuation
            (r"[;:,\[\]()]", Punctuation),
            # Special names ending in __, like lp__
            (r'\b[A-Za-z][A-Za-z0-9_]*__\b', Keyword.Constant),
            # Regular variable names
            (r'\b[A-Za-z][A-Za-z0-9_]*\b', Name),
            # Real Literals
            (r'-?[0-9]+(\.[0-9]+)?[eE]-?[0-9]+', Number.Float),
            (r'-?[0-9]*\.[0-9]*', Number.Float),
            # Integer Literals
            (r'-?[0-9]+', Number.Integer),
            # Assignment operators
            (r'(<-|~)', Keyword.Declaration),
            # Infix and prefix operators
            (r"([+-]|\.?\*|\.?/|')", Operator),
            # Block
            (r'{', Punctuation, '#push'),
            (r'}', Punctuation, '#pop'),
            ]
        }
