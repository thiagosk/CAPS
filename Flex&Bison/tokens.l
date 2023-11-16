%{
#include <stdio.h>
#include <stdlib.h>

#include "parser.tab.h"
%}

%%
[ \t\n]                 ;

"DO"                    {return OPEN;}
"DOT"                   {return CLOSE;}

"AND"                   {return AND;}
"OR"                    {return OR;}
"EQUAL"                 {return EQUAL;}
"NOT"                   {return NOT;}
"LESS"                  {return LESS;}
"GREATER"               {return GREATER;}

"PRINT"                 {return PRINT;}

"SCAN"                  {return SCAN;}

"IF"                    {return IF;}
"ELSE"                  {return ELSE;}

"GIVEN"                 {return GIVEN;}
"WHILE"                 {return WHILE;}
"WITH"                  {return WITH;}

"VAR"                   {return VAR;}

"IS"                    {return IS;}

"PLUS"                  {return PLUS;}
"MINUS"                 {return MINUS;}
"TIMES"                 {return MULTIPLY;}
"DIV"                   {return DIV;}
"JOIN"                  {return JOIN;}

[A-Z][A-Z0-9_]*         {return IDEN;}
"[a-zA-Z][a-zA-Z0-9_]"  {return STR;}
[0-9]+                  {return INT;}

.                       {printf("Unknown token!\n"); yyterminate();}
%%