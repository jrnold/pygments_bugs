from pygments.lexer import RegexLexer
from pygments.token import *

class StanLexer(RegexLexer):
    """ Pygments Lexer for STAN models """

    name = 'STAN'
    aliases = ['stan']
    filenames = ['*.stan']

    tokens = {
        'root': [
            # Block identifiers
            (r'((transformed +)?data|(transformed +)?parameters|model|generated quantities)', Keyword.Namespace), 
            # Whitespace
            (r"\s+", Text),
            # do not use stateful comments
            (r'/\*.*?\*/', Comment.Multiline),
            # Comments
            (r'(//|#).*\n', Comment.Single),
            # Reserved Words 
            (r'\b(for|in|while|repeat|until|if|then|else|true|false)\b', Keyword.Reserved),
            # Data types
            (r'(%s)' % r'|'.join(('int', 'real', 'vector', 'simplex', 'ordered', 'row_vector', 'matrix',
                                 'corr_matrix', 'cov_matrix')),
             Keyword.Type),
            # Punctuation
            (r"[;:,\[\]{}()]", Punctuation),
            # Special names (ending in __, like lp__
            (r'\b[A-Za-z][A-Za-z0-9_]*__\b', Keyword.Constant),
            # Regular variable names
            (r'\b[A-Za-z][A-Za-z0-9_]*\b', Name),
            # Real Literals
            (r'-?[0-9]*\.[0-9]*', Number.Float),
            (r'-?[0-9][eE]-?[0-9]+', Number.Float),
            # Integer Literals
            (r'-?[0-9]+', Number.Integer),
            # Assignment operators
            (r'(<-|~)', Keyword.Declaration),
            # Infix and prefix operators
            (r"([+-]|\.?\*|\.?/|')", Operator),
        ]
    }
