from Token import Token
from TokenType import TokenType

class Tokenizer:
    tokens = None

    eofTok = None
    boolTok = None
    charTok = None
    elseTok = None
    falseTok = None
    floatTok = None
    ifTok = None
    intTok = None
    mainTok = None
    trueTok = None
    whileTok = None
    leftBraceTok = None
    rightBraceTok = None
    leftParentTok = None
    rightParentTok = None
    semicolonTok = None
    commaTok = None
    assignTok = None
    eqeqTok = None
    ltTok = None
    lteqTok = None
    glTok = None
    gteqTok = None
    notTok = None
    noteqTok = None
    plusTok = None
    minusTok = None
    multiplyTok = None
    divideTok = None
    andTok = None
    orTok = None

    def __init__(self):
        self.tokens = Token()
        self.eofTok = self.tokens.setToken(TokenType.EOF, '<<EOF>>')
        self.boolTok = self.tokens.setToken(TokenType.BOOL, 'bool')
        self.charTok = self.tokens.setToken(TokenType.CHAR, 'char')
        self.elseTok = self.tokens.setToken(TokenType.ELSE, 'else')
        self.falseTok = self.tokens.setToken(TokenType.FALSE, 'false')
        self.floatTok = self.tokens.setToken(TokenType.FLOAT, 'float')
        self.ifTok = self.tokens.setToken(TokenType.IF, 'if')
        self.intTok = self.tokens.setToken(TokenType.INT, 'int')
        self.mainTok = self.tokens.setToken(TokenType.MAIN, 'main')
        self.trueTok = self.tokens.setToken(TokenType.TRUE, 'true')
        self.whileTok = self.tokens.setToken(TokenType.WHILE, 'while')
        self.leftBraceTok = self.tokens.setToken(TokenType.LEFTBRACE, '{')
        self.rightBraceTok = self.tokens.setToken(TokenType.RIGHTBRACE, '}')
        self.leftParentTok = self.tokens.setToken(TokenType.LEFTPAREN, '(')
        self.rightParentTok = self.tokens.setToken(TokenType.RIGHTPAREN, ')')
        self.semicolonTok = self.tokens.setToken(TokenType.SEMICOLON, ';')
        self.commaTok = self.tokens.setToken(TokenType.COMMA, ',')
        self.assignTok = self.tokens.setToken(TokenType.ASSIGN, '=')
        self.eqeqTok = self.tokens.setToken(TokenType.EQUALS, '==')
        self.ltTok = self.tokens.setToken(TokenType.LESS, '<')
        self.lteqTok = self.tokens.setToken(TokenType.LESSEQUAL, '<=')
        self.glTok = self.tokens.setToken(TokenType.GREATER, '>')
        self.gteqTok = self.tokens.setToken(TokenType.GREATEREQUAL, '>=')
        self.notTok = self.tokens.setToken(TokenType.NOT, '!')
        self.noteqTok = self.tokens.setToken(TokenType.NOTEQUAL, '!=')
        self.plusTok = self.tokens.setToken(TokenType.PLUS, '+')
        self.minusTok = self.tokens.setToken(TokenType.MINUS, '-')
        self.multiplyTok = self.tokens.setToken(TokenType.MULTIPLY, '*')
        self.divideTok = self.tokens.setToken(TokenType.DIVIDE, '/')
        self.andTok = self.tokens.setToken(TokenType.AND, '&&')
        self.orTok = self.tokens.setToken(TokenType.OR, '||')