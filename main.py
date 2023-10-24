import sys
from Lexer import Lexer
from Tokenizer import Tokenizer

if __name__ == '__main__':
    lexer = Lexer(sys.argv[1])
    tokenizer = Tokenizer()

    tok = lexer.next(tokenizer)

    while tok != tokenizer.eofTok:
        if tok != None:
            print(f'{tok.toString()}\n')
        tok = lexer.next(tokenizer)
