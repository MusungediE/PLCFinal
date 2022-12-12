class RDA:
    def __init__(self, tokens) :
        self.tokens = tokens
        self.current = 0
        self.currentToken = tokens[self.current]

    def beginProg(self):
        if self.currentToken == 'GO':
            self.getNextToken()
            self.stmt()
        else:
            self.error()

    def getNextToken(self):
        if self.current < len(self.tokens):
            self.current +=1
        self.currentToken = self.tokens[self.current]
    
    #<stmt> --> <switch>|<loop>|<block>|<var>
    def stmt(self):
        match self.currentToken:
            case 'SW':
                self.switch()
            case 'LP':
                self.loop()
            case 'id':
                self.var()
            case '{':
                self.block()
            case _:
                self.error()

    #<block> --> '{' <stmt> ';' '}'
    def block(self):
        if self.currentToken == '{':
            self.getNextToken()
            while self.currentToken == 'SW' or self.currentToken == 'LP' or self.currentToken == 'id' or self.currentToken == '{':
                self.stmt()
                if self.currentToken == ';':
                    self.getNextToken()
                    self.stmt()
                else:
                    self.error()
            if self.currentToken == '}':
                self.getNextToken()
            else:
                self.error()
        else:
            self.error()

    #<loop> --> 'LP' <boolexpr> <block>
    def loop(self):
        if self.currentToken == 'LP':
            self.getNextToken()
            if self.currentToken == '(':
                self.getNextToken()
                self.boolexpr()
                if self.currentToken == ')':
                    self.getNextToken()
                    self.block()
                else:
                    self.error()
            elif self.currentToken == 'int_lit':
                self.getNextToken()
                self.block()
            else:
                self.error()
            pass
        else:
            self.error()

    #<switch> --> 'SW' '(' <boolexpr> ')' <block>
    def switch(self):
        if self.currentToken == 'SW':
            self.getNextToken()
            if self.currentToken == '(':
                self.getNextToken()
                self.boolexpr()
                if self.currentToken == ')':
                    self.getNextToken()
                    self.block()
                    if self.currentToken == 'BJ':
                        self.getNextToken()
                        self.block()
                else:
                    self.error()
            else:
                self.error()
        else:
            self.error()

    #<var> --> 'id' (<type>|<assign>)
    def var(self):
        if self.currentToken == 'id':
            self.getNextToken()
            #<type> --> 'byte1'|'byte2'|'byte4'|'byte8'
            if self.currentToken == 'byte1'or self.currentToken =='byte2'or self.currentToken =='byte4'or self.currentToken =='byte8':
                self.getNextToken()
            #<assign> --> '=' <expr>
            elif self.currentToken == '=':
                self.getNextToken()
                self.expr()
            else:
                self.error()    
    
    #<expr> --> <term> {('*'|'/'|'%') <term>}
    def expr(self):
        self.term()
        while self.currentToken == '*' or self.currentToken == '/'or self.currentToken == '%':
            self.getNextToken()
            self.term()

    #<term> --> <factor> {('+'|'-') <factor>}
    def term(self):
        self.factor()
        while self.currentToken == '+' or self.currentToken == '-' :
            self.getNextToken()
            self.factor()

    #<factor> --> 'id'|'int_lit'|'(' <expr> ')'
    def factor(self):
        if self.currentToken == 'id' or self.currentToken == 'int_lit':
            self.getNextToken()
        elif self.currentToken == '(':
            self.getNextToken()
            self.expr()
            if self.currentToken == ')':
                self.getNextToken()
            else:
                self.error()
        else:
            self.error()
    
    #<boolexpr> --> <bor>{'AND' <bor>}
    def boolexpr(self):
        self.bor()
        while self.currentToken == '&':
            self.getNextToken()
            self.bor()

    #<bor> --> <beq> {'OR' <beq>}
    def bor(self):
        self.beq()
        while self.currentToken == '|':
            self.getNextToken()
            self.beq()

    #<beq> --> <brel> {('!='|'==') <brel>}
    def beq(self):
        self.brel()
        while self.currentToken == '!=' or self.currentToken == '==':
            self.getNextToken()
        self.brel()

    #<brel> --> <bexpr> {('<='|'>='|'>'|'<') <bexpr>}
    def brel(self):
        self.bexpr()
        while self.currentToken == '<=' or self.currentToken == '>=' or self.currentToken == '>' or self.currentToken == '<':
            self.getNextToken()
            self.bexpr()

    #<bexpr> --> <bterm> {('*'|'/'|'%') <bterm>}
    def bexpr(self):
        self.bterm()
        while self.currentToken == '*' or self.currentToken == '/' or self.currentToken == '%':
            self.getNextToken()
            self.bterm()

    

    #<bterm> --> <bfactor> {('+'|'-') <bfactor>}
    def bfactor(self):
        if self.currentToken == 'id' or self.currentToken == 'int_lit':
            self.getNextToken()
        elif self.currentToken == '(':
            self.getNextToken()
            self.bexpr()
            if self.currentToken == ')':
                self.getNextToken()
            else:
                self.error()
        else:
            self.error()
    #<bfactor> --> 'id'|'int_lit'|'bool_lit'
    def bterm(self):
        self.bfactor()
        while self.currentToken == '+' or self.currentToken == '-' :
            self.getNextToken()
            self.bfactor()

    
    
    #Error in syntax causes this method to run
    def error(self):
        print("Syntax Error in code")
        StopIteration