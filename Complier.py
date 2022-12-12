from Parser import * 
from lexer import *

f = open("/Users/musungedietongwe/Desktop/CODE/PLCFinalExam/lexx.txt", 'r')
text = f.read()
lexer = text.split()
stringLex = LEX(lexer)
sL1 = stringLex.lexChecker()
print(sL1)
rdaT = RDA(sL1)
rdaT.beginProg()
