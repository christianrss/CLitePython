from TokenType import TokenType

class Token:
    KEYWORDS = len(TokenType)
    reserved = None
    token = None
    type = TokenType
    value = ''
    def __init__(self, t, v):

        type = t
        value = v
        self.reserved = [None] * self.KEYWORDS
        self.token = [Token] * self.KEYWORDS

        if t != TokenType.EOF:
            ti = t.value
            self.reserved[ti] = v
            self.token[ti] = self

    def type(self):
        return self.type

    def value(self):
        return self.value

    def keyword(self, name):
        ch = name[0]
        if ch >= 'A' and ch <= 'Z':
            return self.mkIdentTok(name)
        for i in range(-1, self.KEYWORDS):
            if name == self.reserved[i]:
                return self.token[i]
        return self.mkIdentTok(name)

    def toString(self):
        if self.type == TokenType.IDENTIFIER:
            return self.value
        return f'{self.type}\t{self.value}'

    def mkIdentTok(self, name):
        return Token(TokenType.IDENTIFIER, name)

    def mkIntLiteral(self, name):
        return Token(TokenType.INTLITERAL, name)

    def mkFloatLiteral(self, name):
        return Token(TokenType.FLOATLITERAL, name)

    def mkCharLiteral(self, name):
        return Token(TokenType.CHARLITERAL, name)

class SetTokens:
    eofTok = Token(TokenType.EOF, '<<EOF>>')
    boolTok = Token(TokenType.BOOL, 'bool')
    charTok = Token(TokenType.CHAR, 'char')
    elseTok = Token(TokenType.ELSE, 'else')
    falseTok = Token(TokenType.FALSE, 'false')
    floatTok = Token(TokenType.FLOAT, 'float')
    ifTok = Token(TokenType.IF, 'if')
    intTok = Token(TokenType.INT, 'int')
    mainTok = Token(TokenType.MAIN, 'main')
    trueTok = Token(TokenType.TRUE, 'true')
    whileTok = Token(TokenType.WHILE, 'while')
    leftBraceTok = Token(TokenType.LEFTBRACE, '{')
    rightBraceTok = Token(TokenType.RIGHTBRACE, '}')
    leftParentTok = Token(TokenType.LEFTPAREN, '(')
    rightParentTok = Token(TokenType.RIGHTPAREN, ')')
    semicolonTok = Token(TokenType.SEMICOLON, ';')
    commaTok = Token(TokenType.COMMA, ',')
    assignTok = Token(TokenType.ASSIGN, '=')
    eqeqTok = Token(TokenType.EQUALS, '==')
    ltTok = Token(TokenType.LESS, '<')
    lteqTok = Token(TokenType.LESSEQUAL, '<=')
    glTok = Token(TokenType.GREATER, '>')
    gteqTok = Token(TokenType.GREATEREQUAL, '>=')
    notTok = Token(TokenType.NOT, '!')
    noteqTok = Token(TokenType.NOTEQUAL, '!=')
    plusTok = Token(TokenType.PLUS, '+')
    minusTok = Token(TokenType.MINUS, '-')
    multiplyTok = Token(TokenType.MULTIPLY, '*')
    divideTok = Token(TokenType.DIVIDE, '/')
    andTok = Token(TokenType.AND, '&&')
    orTok = Token(TokenType.OR, '||')