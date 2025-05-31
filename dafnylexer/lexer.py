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

    valid_name = r"[\w']+"
    valid_name_captured = r"([\w']+)"

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
            (r'(;|::|:|\.\.|`)', Punctuation),
            (r'[{(\[,.\])}]', Punctuation),
            (r'(!!|!|\?)', Operator),
            (r'(==|!=|<=|>=|=|&&|[-<>+*/%])', Operator),
            (r'(in)\b', Operator),
            (r'(new)\b', Operator),
            (r'(this|old|print)\b', Name.Function.Magic),
            (r'(multiset)(\s*)(\()', bygroups(Name.Function.Magic, Text, Punctuation)),
            (r'(reads|modifies|ensures|requires|assert|assume|expect|invariant|decreases|constructor)\b', Keyword),
            (r'(if|then|else|while|returns|forall)\b', Keyword),
            (r'(function|method|predicate|lemma)(\s+\{[^\}]+\}\s+)'+valid_name_captured, bygroups(Keyword.Declaration, Text, Name.Function)),
            (r'(function|method|predicate|lemma)(\s+)'+valid_name_captured, bygroups(Keyword.Declaration, Text, Name.Function)),
            (r'(function|method|predicate|lemma)', Keyword.Declaration),
            (r'(trait|class|datatype)(\s+\{[^\}]+\}\s+)'+valid_name_captured, bygroups(Keyword.Declaration, Text, Name.Class)),
            (r'(trait|class|datatype)(\s+)'+valid_name_captured, bygroups(Keyword.Declaration, Text, Name.Class)),
            (r'(trait|class|datatype)', Keyword.Declaration),
            (r'(extends)(\s+)'+valid_name_captured, bygroups(Keyword, Text, Name.Class)),
            (r'(extends)', Keyword),
            (r'(var)(\s+)'+valid_name_captured, bygroups(Keyword.Declaration, Text, Name)), # actually Name.Variable.Instance, but that would be inconsistent, as we don't know this information on other occurrences
            (r'(var|ghost)\b', Keyword.Declaration),
            (r'(true|false)\b', Keyword.Constant),
            (r'(array|seq|set|multiset|int|nat|string|char)\b', Keyword.Type),
            (r'[0-9]+', Number.Integer),
            include('string'),

            (valid_name, Name),
        ]
    }
