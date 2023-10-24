from TokenType import TokenType

class TokenData:
    type = TokenType
    value = ''

    def __init__(self, t, v):
        self.type = t
        self.value = v

    def type(self):
        return self.type

    def value(self):
        return self.value

    def toString(self):
        if self.type == TokenType.IDENTIFIER:
            return self.value
        return f'{self.type}\t{self.value}'

class Token:
    KEYWORDS = len(TokenType)
    reserved = [None] * KEYWORDS
    token = [None] * KEYWORDS
    type = TokenType
    value = ''

    def setToken(self, t, v):
        if t != TokenType.EOF:
            ti = t.value
            self.reserved[ti] = v
            self.token[ti] = TokenData(t, v)
            return self.token[ti]
        else:
            return TokenData(t, v)

    def keyword(self, name):
        ch = name[0]
        if ch >= 'A' and ch <= 'Z':
            return self.mkIdentTok(name)
        for i in range(1, self.KEYWORDS):
            if name == self.reserved[i]:
                return self.token[i]
        return self.mkIdentTok(name)

    def mkIdentTok(self, name):
        return self.setToken(TokenType.IDENTIFIER, name)

    def mkIntLiteral(self, name):
        return self.setToken(TokenType.INTLITERAL, name)

    def mkFloatLiteral(self, name):
        return self.setToken(TokenType.FLOATLITERAL, name)

    def mkCharLiteral(self, name):
        return self.setToken(TokenType.CHARLITERAL, name)