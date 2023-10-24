import sys
import Token
import Lexer

class Parser:

    def __init__(self, ts):
        lexer = ts
        token = lexer.next()

    def match(self, t):
        value = self.token.value()
        if self.token.type() == t:
            self.token = self.lexer.next()
        else:
            self.error(t)
        return value

    def error(self, tok):
        sys.exit(f'Syntax error: expecting: {tok}; saw: {self.token}')

