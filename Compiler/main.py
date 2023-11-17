from node_code import *
from token_code import *

import sys
import re


class PrePro:
    def filter(string):
        return re.sub(r'#.*', '', string).strip()


class Parser:
    def __init__(self, code: str):
        self.tokenizer = Tokenizer(code, 0)
        self.signals = ["PLUS", "MINUS", "DIV", "TIMES", "OPEN", "CLOSE", "EQUAL", "\n", "OR", "AND", "IS", "PRINT", "GREATER", "LESS", "NOT", "IF", "ELSE", "DO", "DOT", "GIVEN", "WHILE", "WITH", "SCAN", "INT", "VAR", "STR", "JOIN", '"']

    def program(self):
        program = Program()
        while self.tokenizer.position != len(self.tokenizer.source):
            child = self.statement()
            if self.tokenizer.next.value == "\n":
                self.tokenizer.select_next()
            program.children.append(child)
        return program

    def statement(self):   
        if self.tokenizer.next.value == "PRINT":
            self.tokenizer.select_next()
            if self.tokenizer.next.value != "OPEN":
                raise ValueError(f"Print without parenthesis\nLast token: {self.tokenizer.next.value}")
            return Println(self.bool_expr())
        
        elif self.tokenizer.next.value == "IF":
            self.tokenizer.select_next() 
            condition = self.bool_expr()
            if self.tokenizer.next.value != "DO":
                raise ValueError(f"Did not open braces properly\nLast token: {self.tokenizer.next.value}")
            if_true = self.block()
            if self.tokenizer.next.value == "ELSE":
                self.tokenizer.select_next()
                if self.tokenizer.next.value != "DO":
                    raise ValueError(f"Did not open braces properly\nLast token: {self.tokenizer.next.value}")
                if_false = self.block()
            elif self.tokenizer.next.value == "\n":
                self.tokenizer.select_next()
                if self.tokenizer.next.value == "ELSE":
                    raise ValueError(f"Else in beginning of line\nLast token: {self.tokenizer.next.value}")
                else:
                    if_false = NoOp()
            elif self.tokenizer.next.value == "EOF":
                if_false = NoOp()
            else:
                raise ValueError(f"Expression after closing braces\nLast token: {self.tokenizer.next.value}")
            if self.tokenizer.next.value == "ELSE": 
                raise ValueError(f"Else out of nowhere\nLast token: {self.tokenizer.next.value}")
            return If(condition, if_true, if_false)
        
        elif self.tokenizer.next.value == "GIVEN":
            self.tokenizer.select_next() 
            init = self.assign()
            self.tokenizer.select_next() 
            cond = self.bool_expr()
            self.tokenizer.select_next() 
            inc = self.assign()
            do = self.block()
            return For(init, cond, inc, do)

        elif self.tokenizer.next.value == "VAR":
            self.tokenizer.select_next() 
            if self.tokenizer.next.value not in self.signals:
                iden = Iden(self.tokenizer.next.value)
                self.tokenizer.select_next() 
                type_variable = self.tokenizer.next.value
                self.tokenizer.select_next() 
                if self.tokenizer.next.value == "IS":
                    self.tokenizer.select_next() 
                    return VarDec(type_variable, iden, self.bool_expr())
                return VarDec(type_variable, iden)
            else:
                raise ValueError(f"Variable name equal to some signal\nLast token: {self.tokenizer.next.value}")
        
        elif self.tokenizer.next.value not in self.signals:
            return self.assign()
        
        elif self.tokenizer.next.value == "DO":
            raise ValueError(f"Braces out of nowhere\nLast token: {self.tokenizer.next.value}")
        
        else:
            return NoOp()
        
    def block(self):
        self.tokenizer.select_next()
        self.tokenizer.select_next()
        while self.tokenizer.next.value != "DOT":
            tree = self.statement()
            self.tokenizer.select_next()
        self.tokenizer.select_next()
        return tree

    def assign(self):
        if self.tokenizer.next.value[0].isdigit():
            raise ValueError(f"Variable can not start with number\nLast token: {self.tokenizer.next.value}")
        left_value = Iden(self.tokenizer.next.value)
        self.tokenizer.select_next()
        if self.tokenizer.next.value != "IS":
            raise ValueError(f"Not = after iden\nLast token: {self.tokenizer.next.value}")
        self.tokenizer.select_next()
        return Assingment(left_value, self.bool_expr())

    def bool_expr(self):
        tree = self.bool_term()
        while self.tokenizer.next.value in ["OR"]:
            signal = self.tokenizer.next.value
            self.tokenizer.select_next()
            tree = BinOp(signal, tree, self.bool_term())
        return tree

    def bool_term(self):
        tree = self.rel_expr()
        while self.tokenizer.next.value in ["AND"]:
            signal = self.tokenizer.next.value
            self.tokenizer.select_next()
            tree = BinOp(signal, tree, self.rel_expr())
        return tree
    
    def rel_expr(self):
        tree = self.parse_expression()
        while self.tokenizer.next.value in ["EQUAL", "GREATER", "LESS"]:
            signal = self.tokenizer.next.value
            self.tokenizer.select_next()
            tree = BinOp(signal, tree, self.parse_expression())
        return tree
        
    def parse_expression(self):
        tree = self.parse_term()
        while self.tokenizer.next.value in ["PLUS", "MINUS", "JOIN"]:
            signal = self.tokenizer.next.value
            self.tokenizer.select_next()
            tree = BinOp(signal, tree, self.parse_term())
        return tree

    def parse_term(self):
        tree = self.parse_factor()
        while self.tokenizer.next.value in ["DIV", "TIMES"]:
            signal = self.tokenizer.next.value
            self.tokenizer.select_next()
            tree = BinOp(signal, tree, self.parse_factor())
        return tree
    
    def parse_factor(self):
        if self.tokenizer.next.value.isdigit():
            number = int(self.tokenizer.next.value)
            self.tokenizer.select_next()
            return IntVal(number)
        
        elif self.tokenizer.next.value[0] == '"':
            value = self.tokenizer.next.value[1:-1]
            self.tokenizer.select_next() 
            return StrVal(value)
        
        elif self.tokenizer.next.value not in self.signals:
            value = self.tokenizer.next.value
            self.tokenizer.select_next()
            return Iden(value)
        
        elif self.tokenizer.next.value in ["PLUS", "MINUS", "NOT"]:
            signal = self.tokenizer.next.value
            self.tokenizer.select_next()
            return UnOp(signal, self.parse_factor())
            
        elif self.tokenizer.next.value in ["OPEN", "CLOSE"]:
            if self.tokenizer.next.value == "OPEN":
                self.tokenizer.select_next()
                tree = self.bool_expr()
                if self.tokenizer.next.value == "CLOSE":
                    self.tokenizer.select_next()
                    return tree
                raise ValueError(f"Did not close parenthesis!\nLast token: {self.tokenizer.next.value}")
        
        elif self.tokenizer.next.value == "SCAN":
            self.tokenizer.select_next()
            return Input()
            
    def run(self):
        self.tokenizer.select_next()
        program = self.program()
        if self.tokenizer.next.value == "EOF":
            return program
        raise ValueError(f"Last tolken is different than 'EOF'!\nLast token: {self.tokenizer.next.value}")


def main():

    with open(sys.argv[1], 'r') as f:
        input = f.read()

    input_without_comments = PrePro.filter(input)

    symbol_table = SymbolTable()
    root = Parser(input_without_comments).run().evaluate(symbol_table)


if __name__ == "__main__":
    main()
