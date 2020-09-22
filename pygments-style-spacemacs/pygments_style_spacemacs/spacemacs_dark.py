# -*- coding: utf-8 -*-
"""
    Spacemacs Dark
    Copyright (C) 2015-2018 Nasser Alshammari

    Author: Nasser Alshammari
    URL: <https://github.com/nashamri/spacemacs-theme>
    Version: 0.1
    Keywords: color, theme

    This is a color theme for spacemacs <https://github.com/syl20bnr/spacemacs>.
    It comes with two versions, dark and light and should work well in
    a 256 color terminal.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace


ITALIC = " italic"
BOLD = " bold"
UNDERLINE = " underline"

BACKGROUND = "#292b2e"
HIGHLIGHT = "#444155"

BASE = "#b2b2b2"
ERROR = "#e0211d"
COMMENT = "#2aa1ae"
KEYWORD = "#4f97d7"
TYPE = "#ce537a"
FUNC = "#bc6ec5"
CONST = "#a45bad"
VAR = "#7590db"
STR = "#2d9574"
DOC = "#9f8766"
NONE = ""


class SpacemacsDarkStyle(Style):
    """
    Port of the Spacemacs Dark color scheme. https://github.com/nashamri/spacemacs-theme
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
        Generic.Deleted: "#8b080b",
        Generic.Emph: BASE + UNDERLINE,
        Generic.Error: BASE,
        Generic.Heading: BASE + BOLD,
        Generic.Inserted: BASE + BOLD,
        Generic.Output: "#44475a",
        Generic.Prompt: BASE,
        Generic.Strong: BASE,
        Generic.Subheading: BASE + BOLD,
        Generic.Traceback: BASE,
    }
