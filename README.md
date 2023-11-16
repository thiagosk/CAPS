# CAPS

## EBNF:

**PROGRAM** = { STATEMENT };\
**BLOCK** = "DO", { STATEMENT }, "DOT" ;\
**ASSIGNMENT** = IDENTIFIER, "IS", BOOL EXPRESSION ;\
**STATEMENT** = ( PRINT | IF | FOR | VAR | ASSIGNMENT ) ;\
**PRINT** = "PRINT", BOOL EXPRESSION ;\
**IF** = "IF", BOOL EXPRESSION, BLOCK, ( λ | "ELSE", BLOCK ) ;\
**FOR** = "GIVEN", ASSIGNMENT, "WHILE", BOOL EXPRESSION, "WITH", ASSIGNMENT, BLOCK ;\
**VAR** = "VAR", IDENTIFIER, TYPE, ( λ | "IS", BOOL EXPRESSION ) ;\
**BOOL EXPRESSION** = BOOL TERM, { "OR", BOOL TERM } ;\
**BOOL TERM** = REL EXPRESSION, { "AND", REL EXPRESSION } ;\
**REL EXPRESSION** = EXPRESSION, { ( "EQUAL" | "GREATER" | "LESS" ), EXPRESSION } ;\
**EXPRESSION** = TERM, { ( "PLUS" | "MINUS" | "JOIN" ), TERM } ;\
**TERM** = FACTOR, { ( "TIMES" | "DIV" ), FACTOR } ;\
**FACTOR** = ( NUMBER | STRING | IDENTIFIER | ( "PLUS" | "MINUS" | "NOT" ), FACTOR | "DO", BOOL EXPRESSION, "DOT" | "SCAN" ) ;\
**IDENTIFIER** = LETTER, { LETTER | DIGIT } ;\
**TYPE** = ( "INT" | "STR" ) ;\
**STRING** = { LETTER | DIGIT | " " | "" } ;\
**NUMBER** = DIGIT, { DIGIT } ;\
**LETTER** = ( A | ... | Z ) ;\
**DIGIT** = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
