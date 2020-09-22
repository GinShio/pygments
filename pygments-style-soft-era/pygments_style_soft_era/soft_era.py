# -*- coding: utf-8 -*-
"""
    soft era
    Copyright (C) 2018-2020 Audrey Moon

    Author: Audrey Moon
    URL: <http://soft-aesthetic.club/soft-era.html>
    Version: 1.0.3
    Keywords: color, theme

    a light pastel syntax theme for cozy, cute coding & typing.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace


ITALIC = " italic"
BOLD = " bold"
UNDERLINE = " underline"

BACKGROUND = "#F9F5F5"
HIGHLIGHT = "#"

BASE = "#BE88D9"
ERROR = "#EC57B4"
COMMENT = "#A29697"
KEYWORD = "#82B4E3"
TYPE = "#CB8DD7"
FUNC = "#25B7B8"
CONST = "#DD698C"
VAR = "#A29ACB"
STR = "#414141"
DOC = "#9D9D9D"
NONE = ""


class SoftEraStyle(Style):
    """
    Port of the Soft Era color scheme. http://soft-aesthetic.club/soft-era.html
    """
    default_style = NONE
    background_color = BACKGROUND
    highlight_color = HIGHLIGHT

    styles = {
        Text: BASE,
        Whitespace: BASE,
        Error: ERROR,
        Other: BASE,
        Punctuation: BASE,

        Comment: COMMENT,
        Comment.Hashbang: COMMENT,
        Comment.Multiline: COMMENT,
        Comment.Preproc: FUNC,
        Comment.Single: COMMENT,
        Comment.Special: COMMENT + ITALIC,

        Keyword: KEYWORD,
        Keyword.Constant: KEYWORD + BOLD,
        Keyword.Declaration: TYPE + ITALIC,
        Keyword.Namespace: KEYWORD,
        Keyword.Pseudo: KEYWORD,
        Keyword.Reserved: KEYWORD,
        Keyword.Type: TYPE,

        Name: BASE,
        Name.Attribute: TYPE,
        Name.Builtin: KEYWORD + ITALIC,
        Name.Builtin.Pseudo: BASE,
        Name.Class: TYPE,
        Name.Constant: CONST,
        Name.Decorator: BASE,
        Name.Entity: BASE,
        Name.Exception: BASE,
        Name.Function: FUNC,
        Name.Label: BASE + ITALIC,
        Name.Namespace: BASE,
        Name.Other: BASE,
        Name.Tag: TYPE,
        Name.Variable: VAR,
        Name.Variable.Class: VAR,
        Name.Variable.Instance: VAR,
        Name.Variable.Global: VAR + ITALIC,

        Number: CONST,
        Number.Bin: CONST,
        Number.Float: CONST,
        Number.Hex: CONST,
        Number.Integer: CONST,
        Number.Integer.Long: CONST,
        Number.Oct: CONST,

        Operator: VAR,
        Operator.Word: VAR,

        Literal: BASE,
        Literal.Date: BASE,

        String: STR,
        String.Backtick: STR,
        String.Char: STR,
        String.Doc: DOC,
        String.Double: STR,
        String.Escape: STR,
        String.Heredoc: STR,
        String.Interpol: STR,
        String.Other: STR,
        String.Regex: STR,
        String.Single: STR,
        String.Symbol: STR,

        Generic: BASE,
        Generic.Deleted: "#E4846F",
        Generic.Emph: BASE + UNDERLINE,
        Generic.Error: BASE,
        Generic.Heading: BASE + BOLD,
        Generic.Inserted: BASE + BOLD,
        Generic.Output: BASE,
        Generic.Prompt: BASE,
        Generic.Strong: BASE,
        Generic.Subheading: BASE + BOLD,
        Generic.Traceback: BASE,
    }
