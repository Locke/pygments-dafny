# -*- coding: utf-8 -*-
"""
    pygments.lexers.dafny
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Dafny.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import *

__all__ = ['DafnyLexer']


class DafnyLexer(RegexLexer):
    """
    For Dafny source code.
    """

    name = 'Dafny'
    aliases = ['dafny']
    filenames = ['*.dfy']
    mimetypes = []

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    valid_name = r'[\w_]+'

    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
        ],
        'string': [
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ],
        'root': [
            include('commentsandwhitespace'),
            (r'(:=)', Operator),
            (r'(\|)', Operator),
            (r'(;|::|:|\.\.)', Punctuation),
            (r'[{(\[,.\])}]', Punctuation),
            (r'(==|!=|<=|>=|=|&&|[-<>+*/%])', Operator),
            (r'(in)\b', Operator),
            (r'(old)\b', Name.Function.Magic),
            (r'(modifies|ensures|requires|assert|invariant)\b', Keyword),
            (r'(if|then|else|while|return|forall)\b', Keyword),
            (r'(function|method|trait|class|datatype|predicate|lemma)(\s+)(\w+)', bygroups(Keyword.Declaration, Text, Name.Function)),
            (r'(function|method|trait|class|datatype|predicate|lemma)', Keyword.Declaration),
            (r'(var)(\s+)(\w+)', bygroups(Keyword.Declaration, Text, Name)), # actually Name.Variable.Instance, but that would be inconsistent, as we don't know this information on other occurrences
            (r'(true|false)\b', Keyword.Constant),
            (r'(array|seq|set|multiset|int|nat|string|char)\b', Keyword.Type),
            (r'[0-9]+', Number.Integer),
            include('string'),

            (valid_name, Name),
        ]
    }
