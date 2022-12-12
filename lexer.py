import re
#regex for variable declaration
def isVariable(str):
    return re.search("[a-z]|[A-Z]|_ {6,8}", str)

#Lex class is lexical analyzer, checks if tokens are valid tokens
class LEX:
    def __init__(self, str):
        self.str = str
    def error(self):
        print("lexical error in code")
        exit()
    def lexChecker(self):
        lexemes = []
        for i in self.str:
            if i == "GO":
                lexemes.append('GO')
            elif i == "LP":
                lexemes.append('LP')
            elif i == "SW":
                lexemes.append('SW')
            elif i == "byte1":
                lexemes.append('byte1')
            elif i == "byte2":
                lexemes.append('byte2')
            elif i == "byte4":
                lexemes.append('byte4')
            elif i == "byte8":
                lexemes.append('byte8')
            elif i == "BJ":
                lexemes.append('BJ')
            elif i == "+":
                lexemes.append('+')
            elif i == "-":
                lexemes.append('-')
            elif i == "*":
                lexemes.append('*')
            elif i == "/":
                lexemes.append('/')
            elif i == "%":
                lexemes.append('%')
            elif i == ">":
                lexemes.append('>')
            elif i == ">=":
                lexemes.append('>=')
            elif i == "<":
                lexemes.append('<')
            elif i == "<=":
                lexemes.append('<=')
            elif i == "==":
                lexemes.append('==')
            elif i == "!=":
                lexemes.append('!=')
            elif i == "{":
                lexemes.append('{')
            elif i == "}":
                lexemes.append('}')
            elif i == "=":
                lexemes.append('=')
            elif i == ";":
                 lexemes.append(';')
            elif i == "STOP":
                lexemes.append('STOP')
            elif i == "(":
                lexemes.append('(')
            elif i == ")":
                lexemes.append(')')
            elif i == "&":
                lexemes.append('&')
            elif i == "true":
                lexemes.append('true')
            elif i == "|":
                lexemes.append('|')
            elif i.isnumeric():
                lexemes.append('int_lit')
            elif isVariable(i):
                lexemes.append('id')
            else:
                self.error()
        return lexemes
