import sys
from Token import Token

class Lexer:

    isEof = False
    ch = ' '
    input = ''
    line = ''
    lineno = 0
    col = 1
    letters = 'acbdefghijklmnopqrstuvwxyz'\
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    digits = '0123456789'
    eolnCh = '\n'
    eofCh = '\004'

    tokenizer = None

    #tokens = Token(TokenType.EOF, '<<EOF>>')

    #setTokens = SetTokens()

    #tokens = Token(None, None)

    def __init__(self, filename):
        try:
            self.input = open(filename, "r")
        except Exception as err:
            print(f'{err}')
            sys.exit(1)

    def nextChar(self): # retorna o proximo caracter
        if self.ch == self.eofCh:
            self.error('Attempt to read past end of file')
        self.col += 1
        if self.col >= len(self.line):
            try:
                self.line = self.input.readline()
            except Exception as err:
                sys.exit(err)
            if len(self.line) == 0: # final do arquivo
                self.line = f'{self.eofCh}'
            else:
                self.lineno += 1
                self.line += self.eolnCh
            self.col = 0
        return self.line[self.col]


    def next(self, tokenizer): # return next token
        self.tokenizer = tokenizer
        while True:
            if self.isLetter(self.ch): # ident or keyword
                spelling = self.concat(self.letters + self.digits)
                return self.tokenizer.tokens.keyword(spelling)
            elif self.isDigit(self.ch): # int or float literal
                number = self.concat(self.digits)
                if (self.ch != '.'): # int literal
                    return self.tokenizer.tokens.mkIntLiteral(self.number)
                self.number += self.concat(self.digits)
                return self.tokenizer.tokens.mkFloatLiteral(self.number)
            else:
                match self.ch:
                    case ' ' | '\t' | '\r' | self.eolnCh:
                        self.ch = self.nextChar()
                        break
                    case '/': # divide or comment
                        self.ch = self.nextChar()
                        if self.ch != '/':
                            return self.tokens.divideTok
                        # comment
                        while True:
                            self.ch = self.nextChar()
                            if (self.ch == self.eolnCh):
                                break
                        self.ch = self.nextChar()
                        break
                    case '\'': # char literal
                        ch1 = self.nextChar()
                        self.nextChar() # get '
                        self.ch = self.nextChar()
                        return Token.mkCharLiteral(f'{ch1}')
                    case self.eofCh:
                        return self.tokenizer.eofTok
                    case '+':
                        self.ch = self.nextChar()
                        return self.tokenizer.plusTok

                        # - * () {} ; , exercise
                    case '-':
                        self.ch = self.nextChar()
                        return self.tokenizer.minusTok
                    case '*':
                        self.ch = self.nextChar()
                        return self.tokenizer.multiplyTok
                    case '(':
                        self.ch = self.nextChar()
                        return self.tokenizer.leftParentTok
                    case ')':
                        self.ch = self.nextChar()
                        return self.tokenizer.rightParentTok
                    case '{':
                        self.ch = self.nextChar()
                        return self.tokenizer.leftBraceTok
                    case '}':
                        self.ch = self.nextChar()
                        return self.tokenizer.rightBraceTok
                    case ';':
                        self.ch = self.nextChar()
                        return self.tokenizer.semicolonTok
                    case ',':
                        self.ch = self.nextChar()
                        return self.tokenizer.commaTok
                    case '&':
                        self.check('&')
                        return self.tokenizer.andTok
                    case '|':
                        self.check('|')
                        return self.tokenizer.orTok
                    case '=':
                        return self.chkOpt('=', self.tokenizer.assignTok, self.tokenizer.eqeqTok)
                        # < > ! exercise
                    case '<':
                        return self.chkOpt('<', self.tokenizer.ltTok, self.tokenizer.lteqTok)
                    case '>':
                        return self.chkOpt('>', self.tokenizer.glTok, self.tokenizer.gteqTok)
                    case '!':
                        return self.chkOpt('!', self.tokenizer.notTok, self.tokenizer.noteqTok)
                    case _:
                        self.error(f'Illegal character {self.ch}')
        #return Token(TokenType.EOF, '<<EOF>>')
    def isLetter(self, c):
        return c.isalpha()

    def isDigit(self, c):
        return c.isnumeric()

    def check(self, c):
        self.ch = self.nextChar()
        if self.ch != c:
            self.error(f'Illegal character, expecting {c}')
        self.ch = self.nextChar()

    def chkOpt(self, c, one, two):
        return None # exercicio

    def concat(self, set):
        r = ''
        while True:
            r += self.ch
            self.ch = self.nextChar()
            if set.find(self.ch) == -1:
                break
        return r

    def error(self, msg):
        print(f'{self.line}\n')
        print(f'Error: column {self.col} {msg}')
        sys.exit(1)