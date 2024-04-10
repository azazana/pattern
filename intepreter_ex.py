

class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        tokens = lex(expression, self.variables)
        return tokens

class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text
    class Type:
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        VARUABLES = 3
class Integer:
    def __init__(self, value):
        self.value = value
def lex(expression, variables):
    i = 0
    tokens = []
    while i <= len(expression):
        if expression[i] == '+':
            tokens.append(Token(Token.Type.PLUS, '+'))
        elif expression[i] == '-':
            tokens.append(Token(Token.Type.MINUS, '-'))
        elif expression[i] in variables:
            tokens.append(variables[expression[i]])
        else:
            digits = [expression[i]]
            for j in range(i + 1, len(expression)):
                if expression[j].isdigit():
                    digits.append(expression[j])
                    i += 1
                else:
                    tokens.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break

if __name__ == '__main__':
    ep = ExpressionProcessor()
    ep.variables['x'] = Integer(10)
    result = ep.calculate('1+2+3')
    print(result)
    result = ep.calculate('1+x+3')
    print(result)
    result = ep.calculate('1+2+x')
    print(result)
