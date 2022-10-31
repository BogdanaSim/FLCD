import re


class Scanner:
    def __init__(self):
        self.__reserved_words = []
        self.__separators = []
        self.__operators = []
        self.read_tokens()

    def get_reserved_words(self):
        return self.__reserved_words

    def get_separators(self):
        return self.__separators

    def get_operators(self):
        return self.__operators

    def get_all(self):
        return self.__operators + self.__separators + self.__reserved_words

    def read_tokens(self):
        with open('scanner/token.in', 'r') as f:
            for i in range(13):
                operator = f.readline().strip()
                self.__operators.append(operator)
            for i in range(11):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.__separators.append(separator)
            for i in range(12):
                self.__reserved_words.append(f.readline().strip())

    def is_operator(self, elem):
        for o in self.__operators:
            if elem in o:
                return True
        return False

    def is_constant(self, elem):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.*\'$', elem) is not None

    def is_identifier(self, elem):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', elem) is not None

    def get_line_tokens(self, line):
        token = ''
        tokens = []
        i = 0
        while i < len(line):
            if line[i] == '\'':
                if len(token) > 0:
                    tokens.append(token)
                token = '\''
                end_string = False
                i += 1
                while i < len(line) and not end_string:
                    if line[i] == '\'':
                        end_string = True
                    token += line[i]
                    i += 1
                tokens.append(token)
                token = ''
            elif self.is_operator(line[i]):
                if len(token) > 0:
                    tokens.append(token)
                token = ''
                while i < len(line) and self.is_operator(line[i]):
                    token += line[i]
                    i += 1
                tokens.append(token)
                token = ''
            elif line[i] in self.__separators:
                if len(token) > 0:
                    tokens.append(token)
                token = line[i]
                i += 1
                tokens.append(token)
                token = ''

            else:
                token += line[i]
                i += 1
        if len(token) > 0:
            tokens.append(token)
        return tokens
