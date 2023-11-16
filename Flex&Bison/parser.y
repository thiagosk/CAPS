%{
#include <stdio.h>
#include <stdlib.h> 
void yyerror(const char *s) { printf("ERRO: %s\n", s); }
%}


%token OPEN CLOSE AND OR EQUAL NOT LESS GREATER PRINT SCAN IF ELSE GIVEN WHILE WITH VAR IS PLUS MINUS MULTIPLY DIV JOIN IDEN STR INT


%start program

%%
program : statements
        ;

statements  : statement | statements statement
            ;

block   : OPEN statements CLOSE
        ;

assignment  : IDEN IS bool_expression
            ;

statement   : assignment | print_statement | if_statement | for_statement | var_statement
            ;

print_statement     : PRINT bool_expression
                    ;

if_statement    : IF bool_expression block | IF bool_expression block ELSE block
                ;

for_statement   : GIVEN assignment WHILE bool_expression WITH assignment block
                ;

var_statement   : VAR IDEN type | VAR IDEN type IS bool_expression
                ;

bool_expression : bool_term OR bool_term
                ;

bool_term   : rel_expression AND rel_expression
            ;

rel_expression  : expression EQUAL expression | expression GREATER expression | expression LESS expression
                ;

expression  : term PLUS term | term MINUS term | term JOIN term
            ;

term    : factor MULTIPLY factor | factor DIV factor
        ;

factor  : INT | STR | IDEN | PLUS factor | MINUS factor | NOT factor | OPEN bool_expression CLOSE | SCAN
        ;

type    : INT | STR 
        ;
%%