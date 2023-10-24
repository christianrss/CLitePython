from enum import Enum

class TokenType(Enum):
    BOOL = 1
    CHAR = 2
    ELSE = 3
    FALSE = 4
    FLOAT = 5
    IF = 6
    INT = 7
    MAIN = 8
    TRUE = 9
    WHILE = 10
    EOF = 11
    LEFTBRACE = 12
    RIGHTBRACE = 13
    LEFTBRACKET = 14
    RIGHTBRACKET = 15
    LEFTPAREN = 16
    RIGHTPAREN = 17
    SEMICOLON = 18
    COMMA = 19
    ASSIGN = 20
    EQUALS = 21
    LESS = 22
    LESSEQUAL = 23
    GREATER = 24
    GREATEREQUAL = 25
    NOT = 26
    NOTEQUAL = 27
    PLUS = 28
    MINUS = 29
    MULTIPLY = 30
    DIVIDE = 31
    AND = 32
    OR = 33
    IDENTIFIER = 34
    INTLITERAL = 35
    FLOATLITERAL = 36
    CHARLITERAL = 37

