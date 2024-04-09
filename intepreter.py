from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input):
    result = []
    i = 0
    while i < len(input):
        if input[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1
    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryExpression()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1

    return result


def calc(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    input = '(13+4)-(12+1)'
    calc(input)
