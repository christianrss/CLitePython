import sys
from Lexer import Lexer
from Token import Token, SetTokens
from TokenType import TokenType

if __name__ == '__main__':
    lexer = Lexer(sys.argv[1])
    tok = lexer.next()

    setTokens = SetTokens()

    while tok != setTokens.eofTok:
        print(f'{tok.toString()}\n')
        tok = lexer.next()
