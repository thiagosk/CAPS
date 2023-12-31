# CAPS
CAPS IS A PROGRAMMING LANGUAGE CREATED TO MINIMIZE HAND MOVEMENTS DURING CODING, WITH A PRIMARY FOCUS ON ENHANCING COMFORT.

FOR THAT **MOST OF THE SIGNALS WILL BE TYPED** (DON'T WORRY, IT IS ALL VERY INTUITIVE) AND, OF COURSE, **ALL THE WORDS MUST BE IN CAPITAL LETTERS**, TO AVOID THE NEED TO SHIFT BETWEEN CASES. 

SO POSITION YOUR HANDS COMFORTABLY ON THE KEYBOARD, AND ENJOY THE SEAMLESS CODING EXPERIENCE THAT ONLY CAPS PROVIDES.

### BRIEF DOCUMENTATION:

**VARIABLES:**

INPUT
```
VAR X INT
VAR Y INT = 100
X IS 10

VAR A STR
VAR B STR = "I LOVE CAPS"
A IS "CAPS IS LAZY"
```

**CONDITIONS:**

INPUT
```
IF X EQUALS 10 DO
  PRINT OPEN A CLOSE
DOT ELSE DO
  PRINT OPEN B CLOSE
DOT
```

OUTPUT
```
CAPS IS LAZY
```

> [!NOTE]
> COMPARING TO GoLang:
>
> "DO" = "{"
>
> "DOT" = "}"
>
> "OPEN" = "("
>
> "CLOSE" = ")"

**LOOPS:**

INPUT
```
GIVEN I IS 0 WHILE I LESS 5 WITH I IS I PLUS 1 DO
  PRINT OPEN X PLUS I CLOSE
DOT
```

OUTPUT
```
10
11
12
13
```

> [!NOTE]
> COMPARING TO GoLang `for`, "GIVEN" IS THE INIT PART, "WHILE" IS THE CONDITION AND "WITH" IS THE INCREMENT 

### HOW TO RUN IT?
  1. GO TO THE _Compiler_ FOLDER
  2. CODE IN A _.txt_ FILE
  3. IN THE TERMINAL RUN `python main.py NAME_OF_FILE.txt`

> [!IMPORTANT]
> THERE IS AN EXAMPLE/TEST IN THE _Compiler_ FOLDER CALLED _input.txt_, WHERE ALL OF THE FUNCTIONALITIES ARE PRESENTED

### EBNF:

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
**FACTOR** = ( NUMBER | STRING | IDENTIFIER | ( "PLUS" | "MINUS" | "NOT" ), FACTOR | "OPEN", BOOL EXPRESSION, "CLOSE" | "SCAN" ) ;\
**IDENTIFIER** = LETTER, { LETTER | DIGIT } ;\
**TYPE** = ( "INT" | "STR" ) ;\
**STRING** = { LETTER | DIGIT | " " | "" } ;\
**NUMBER** = DIGIT, { DIGIT } ;\
**LETTER** = ( A | ... | Z ) ;\
**DIGIT** = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

![Alt text](images/meme.png)