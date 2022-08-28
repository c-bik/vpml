from dql_lex import lexer


def test_lexer():
    test_str = """
MATCH SENTENCE
WHEN
TYPE IS "FOO"
VALUE IS "bar" WITHIN MAX 3
(
    TYPE IN ( "FOO", "BAR", "BAZ")
    OR VALUE IN ( "foo", "bar", "baz" )
) WITHIN MAX 5
SELECT PARAGRAPH
    """
    lexer.input(test_str)

    expected = [
        ("MATCH", "MATCH", 2, 1),
        ("SENTENCE", "SENTENCE", 2, 7),
        ("WHEN", "WHEN", 3, 16),
        ("TYPE", "TYPE", 4, 21),
        ("IS", "IS", 4, 26),
        ("STRING", "FOO", 4, 29),
        ("VALUE", "VALUE", 5, 35),
        ("IS", "IS", 5, 41),
        ("STRING", "bar", 5, 44),
        ("WITHIN", "WITHIN", 5, 50),
        ("MAX", "MAX", 5, 57),
        ("NUMBER", 3, 5, 61),
        ("LPAREN", "(", 6, 63),
        ("TYPE", "TYPE", 7, 69),
        ("IN", "IN", 7, 74),
        ("LPAREN", "(", 7, 77),
        ("STRING", "FOO", 7, 79),
        ("COMMA", ",", 7, 84),
        ("STRING", "BAR", 7, 86),
        ("COMMA", ",", 7, 91),
        ("STRING", "BAZ", 7, 93),
        ("RPAREN", ")", 7, 98),
        ("OR", "OR", 8, 104),
        ("VALUE", "VALUE", 8, 107),
        ("IN", "IN", 8, 113),
        ("LPAREN", "(", 8, 116),
        ("STRING", "foo", 8, 118),
        ("COMMA", ",", 8, 123),
        ("STRING", "bar", 8, 125),
        ("COMMA", ",", 8, 130),
        ("STRING", "baz", 8, 132),
        ("RPAREN", ")", 8, 138),
        ("RPAREN", ")", 9, 140),
        ("WITHIN", "WITHIN", 9, 142),
        ("MAX", "MAX", 9, 149),
        ("NUMBER", 5, 9, 153),
        ("SELECT", "SELECT", 10, 155),
        ("PARAGRAPH", "PARAGRAPH", 10, 162),
    ]

    actual = [
        (tok.type, tok.value, tok.lineno, tok.lexpos)
        for tok in lexer
    ]

    assert expected == actual
