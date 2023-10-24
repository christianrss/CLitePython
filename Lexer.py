import sys
from Token import Token, SetTokens
from TokenType import TokenType

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

    tokens = Token(TokenType.EOF, '<<EOF>>')

    setTokens = SetTokens()

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


    def next(self): # return next token
        while True:
            if self.isLetter(self.ch): # ident or keyword
                spelling = self.concat(self.letters + self.digits)
                return self.tokens.keyword(spelling)
            elif self.isDigit(self.ch): # int or float literal
                number = self.concat(self.digits)
                if (self.ch != '.'): # int literal
                    return self.tokens.mkIntLiteral(self.number)
                self.number += self.concat(self.digits)
                return self.tokens.mkFloatLiteral(self.number)
            else:
                match self.ch:
                    case ' ' | '\t' | '\r' | self.eolnCh:
                        self.ch = self.nextChar()
                        break
                    case '/': # divide or comment
                        self.ch = self.nextChar()
                        if self.ch != '/':
                            return self.setTokens.divideTok
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
                        return self.setTokens.eofTok
                    case '+':
                        self.ch = self.nextChar()
                        return self.setTokens.plusTok

                        # - * () {} ; , exercise
                    case '-':
                        self.ch = self.nextChar()
                        return self.setTokens.minusTok
                    case '*':
                        self.ch = self.nextChar()
                        return self.setTokens.multiplyTok
                    case '(':
                        self.ch = self.nextChar()
                        return self.setTokens.leftParentTok
                    case ')':
                        self.ch = self.nextChar()
                        return self.setTokens.rightParentTok
                    case '{':
                        self.ch = self.nextChar()
                        return self.setTokens.leftBraceTok
                    case '}':
                        self.ch = self.nextChar()
                        return self.setTokens.rightBraceTok
                    case ';':
                        self.ch = self.nextChar()
                        return self.setTokens.semicolonTok
                    case ',':
                        self.ch = self.nextChar()
                        return self.setTokens.commaTok
                    case '&':
                        self.check('&')
                        return self.setTokens.andTok
                    case '|':
                        self.check('|')
                        return self.setTokens.orTok
                    case '=':
                        return self.chkOpt('=', self.setTokens.assignTok, self.setTokens.eqeqTok)
                        # < > ! exercise
                    case '<':
                        return self.chkOpt('<', self.setTokens.ltTok, self.setTokens.lteqTok)
                    case '>':
                        return self.chkOpt('>', self.setTokens.glTok, self.setTokens.gteqTok)
                    case '!':
                        return self.chkOpt('!', self.setTokens.notTok, self.setTokens.noteqTok)
                    case _:
                        self.error(f'Illegal character {self.ch}')
        return Token(TokenType.EOF, '<<EOF>>')
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
            if set.find(self.ch) >=0:
                break
        return r

    def error(self, msg):
        print(f'{self.line}\n')
        print(f'Error: column {self.col} {msg}')
        sys.exit(1)