class Token:
    def __init__(self, type: str, value: int):
        self.type = type
        self.value = value


class Tokenizer:
    def __init__(self, source: str, position: int):
        self.source = source
        self.position = position
        self.next = Token(type(source), source)

    def no_lower_cases(self, token):
        if (type(token)==str) & (token.isdigit()==False):
            if token.isupper()==False:
                raise ValueError("!!!NO LOWER CASES!!!")
    
    def select_next(self):
        if self.position == len(self.source):
            self.next = Token(type("EOF"), "EOF")
            return 0
        
        token = ""
        while self.position < len(self.source):
            char = self.source[self.position]
            size_of_token = len(token.strip())

            if char in ["\n"]:
                if size_of_token == 0:
                    self.next = Token(type(char), char) # save signal
                    self.position += 1
                    return 0
                else:
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0


            elif char == '"':
                if size_of_token == 0:
                    for i in range(self.position+1, len(self.source)):
                        if self.source[i] == '"':
                            end = i
                            break
                    token_str = self.source[self.position:end+1]
                    self.next = Token(type(token_str), token_str) # save signal
                    self.position += len(token_str)
                    return 0
                else:
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                
            elif char == "P":
                token_print = self.source[self.position:self.position+5]
                token_plus = self.source[self.position:self.position+4]
                if (token_print == "PRINT") & (size_of_token == 0):
                    self.next = Token(type(token_print), token_print)
                    self.position += len(token_print)
                    return 0
                elif (token_plus == "PLUS") & (size_of_token == 0):
                    self.next = Token(type(token_plus), token_plus)
                    self.position += len(token_plus)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_print == "PRINT") | (token_plus == "PLUS")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1
        
            elif char == "I":
                token_if = self.source[self.position:self.position+2]
                token_int = self.source[self.position:self.position+3]
                token_is = self.source[self.position:self.position+2]
                if (token_if == "IF") & (size_of_token == 0):
                    self.next = Token(type(token_if), token_if) # save signal
                    self.position += len(token_if)
                    return 0
                elif (token_int == "INT") & (size_of_token == 0):
                    self.next = Token(type(token_int), token_int) # save signal
                    self.position += len(token_int)
                    return 0
                elif (token_is == "IS") & (size_of_token == 0):
                    self.next = Token(type(token_is), token_is) # save signal
                    self.position += len(token_is)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_if == "IF") | (token_int == "INT") | (token_is == "IS")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1
                
            elif char == "E":
                token_else = self.source[self.position:self.position+4]
                token_equal = self.source[self.position:self.position+5]
                if (token_else == "ELSE") & (size_of_token == 0):
                    self.next = Token(type(token_else), token_else)
                    self.position += len(token_else)
                    return 0
                elif (token_equal == "EQUAL") & (size_of_token == 0):
                    self.next = Token(type(token_equal), token_equal)
                    self.position += len(token_equal)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_else == "ELSE") | (token_equal == "EQUAL")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1
                
            elif char == "F":
                token_for = self.source[self.position:self.position+3]
                if (token_for == "FOR") & (size_of_token == 0):
                    self.next = Token(type(token_for), token_for)
                    self.position += len(token_for)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_for == "FOR"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "V":
                token_var = self.source[self.position:self.position+3]
                if (token_var == "VAR") & (size_of_token == 0):
                    self.next = Token(type(token_var), token_var)
                    self.position += len(token_var)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_var == "VAR"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "S":
                token_str = self.source[self.position:self.position+3]
                token_scan = self.source[self.position:self.position+4]
                if (token_str == "STR") & (size_of_token == 0):
                    self.next = Token(type(token_str), token_str)
                    self.position += len(token_str)
                    return 0
                elif (token_scan == "SCAN") & (size_of_token == 0):
                    self.next = Token(type(token_scan), token_scan)
                    self.position += len(token_scan)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_str == "STR") | (token_scan == "SCAN")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "O":
                token_or = self.source[self.position:self.position+2]
                token_open = self.source[self.position:self.position+4]
                if (token_or == "OR") & (size_of_token == 0):
                    self.next = Token(type(token_or), token_or)
                    self.position += len(token_or)
                    return 0
                elif (token_open == "OPEN") & (size_of_token == 0):
                    self.next = Token(type(token_open), token_open)
                    self.position += len(token_open)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_or == "OR") | (token_open == "OPEN")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "A":
                token_and = self.source[self.position:self.position+3]
                if (token_and == "AND") & (size_of_token == 0):
                    self.next = Token(type(token_and), token_and)
                    self.position += len(token_and)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_and == "AND"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "M":
                token_minus = self.source[self.position:self.position+5]
                if (token_minus == "MINUS") & (size_of_token == 0):
                    self.next = Token(type(token_minus), token_minus)
                    self.position += len(token_minus)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_minus == "MINUS"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "T":
                token_times = self.source[self.position:self.position+5]
                if (token_times == "TIMES") & (size_of_token == 0):
                    self.next = Token(type(token_times), token_times)
                    self.position += len(token_times)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_times == "TIMES"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "D":
                token_div = self.source[self.position:self.position+3]
                token_do = self.source[self.position:self.position+2]
                token_dot = self.source[self.position:self.position+3]
                if (token_div == "DIV") & (size_of_token == 0):
                    self.next = Token(type(token_div), token_div)
                    self.position += len(token_div)
                    return 0
                elif (token_dot == "DOT") & (size_of_token == 0):
                    self.next = Token(type(token_dot), token_dot)
                    self.position += len(token_dot)
                    return 0
                elif (token_do == "DO") & (size_of_token == 0):
                    self.next = Token(type(token_do), token_do)
                    self.position += len(token_do)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_div == "DIV") | (token_do == "DO") | (token_dot == "DOT")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "C":
                token_close = self.source[self.position:self.position+5]
                if (token_close == "CLOSE") & (size_of_token == 0): 
                    self.next = Token(type(token_close), token_close)
                    self.position += len(token_close)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_close == "CLOSE"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "L":
                token_less = self.source[self.position:self.position+4]
                if (token_less == "LESS") & (size_of_token == 0):
                    self.next = Token(type(token_less), token_less)
                    self.position += len(token_less)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_less == "LESS"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "G":
                token_greater = self.source[self.position:self.position+7]
                token_given = self.source[self.position:self.position+5]
                if (token_greater == "GREATER") & (size_of_token == 0):
                    self.next = Token(type(token_greater), token_greater)
                    self.position += len(token_greater)
                    return 0
                elif (token_given == "GIVEN") & (size_of_token == 0):
                    self.next = Token(type(token_given), token_given)
                    self.position += len(token_given)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_greater == "GREATER") | (token_given == "GIVEN")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "N":
                token_not = self.source[self.position:self.position+3]
                if (token_not == "NOT") & (size_of_token == 0):
                    self.next = Token(type(token_not), token_not)
                    self.position += len(token_not)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_not == "NOT"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "J":
                token_join = self.source[self.position:self.position+4]
                if (token_join == "JOIN") & (size_of_token == 0):
                    self.next = Token(type(token_join), token_join)
                    self.position += len(token_join)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & (token_join == "JOIN"):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            elif char == "W":
                token_while = self.source[self.position:self.position+5]
                token_with = self.source[self.position:self.position+4]
                if (token_while == "WHILE") & (size_of_token == 0):
                    self.next = Token(type(token_while), token_while)
                    self.position += len(token_while)
                    return 0
                elif (token_with == "WITH") & (size_of_token == 0):
                    self.next = Token(type(token_with), token_with)
                    self.position += len(token_with)
                    return 0
                elif (size_of_token == 0):
                    token += char # keep building token
                    self.position += 1
                elif (size_of_token != 0) & ((token_while == "WHILE") | (token_with == "WITH")):
                    self.no_lower_cases(token.strip())
                    self.next = Token(type(token.strip()), token.strip()) # save int|str
                    return 0

                else:
                    token += char # keep building token
                    self.position += 1

            else:
                token += char # keep building token
                self.position += 1

        self.no_lower_cases(token.strip())
        self.next = Token(type(token.strip()), token.strip()) # save last int|str
        return 0



class SymbolTable:
    def __init__(self):
        self.dictionary = {}

    def getter(self, key: str):
        return self.dictionary[key]
    
    def setter(self, key: str, value, type_variable: str):
        if key in self.dictionary:
            if self.dictionary[key][1] == type_variable:
                self.dictionary[key] = (value, type_variable)
            else:
                raise ValueError("Overwriting variable with different type of value")
        else:
            self.dictionary[key] = (value, type_variable)


