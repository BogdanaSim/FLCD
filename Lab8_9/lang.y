%{
#include <stdio.h>
 int yylex(void);
int yyerror(char* s);
#include <stdlib.h>
#include <string.h>
#define YYDEBUG 1 
%}


%token ID
%token CONST

%token ARRAY
%token IF
%token ELSE
%token FOR
%token WHILE
%token EXEC
%token AND
%token OR
%token XOR
%token READ
%token WRITE
%token STR
%token NR
%token VAR

%token ASSIGNMENT
%token EQUAL
%token NOT_EQUAL
%token LOWER_OR_EQUAL
%token GREATER_OR_EQUAL 
%token LOWER_THAN
%token GREATER_THAN
%token NOT

%left '+' '-' '*' '/'

%token PLUS 
%token MINUS
%token DIV 
%token MUL 
%token MOD 


%token DOT 
%token COMMA 
%token SEMI_COLON
%token COLON
%token SPACE 
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET 
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET 

%token READ_OP
%token WRITE_OP 

%start program 

%%
program : EXEC compound_stmt
	;
declaration :  type ID
	    ;
type : VAR | NR | STR | ARRAY OPEN_RIGHT_BRACKET CONST CLOSED_RIGHT_BRACKET 
    ;
compound_stmt : OPEN_CURLY_BRACKET list_stmts CLOSED_CURLY_BRACKET
	 ;
list_stmts :  stmt stmt_temp
	 ;
stmt_temp : /*empty*/ | list_stmts
	 ;
stmt :  simple_stmt SEMI_COLON | struct_stmt
     ;
simple_stmt :  assignment_stmt | io_stmt | declaration
	 ; 
struct_stmt :  compound_stmt | if_stmt | while_stmt | for_stmt
	   ;
if_stmt :  IF OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET compound_stmt temp_if
       ;
temp_if : /*empty*/ | ELSE compound_stmt | ELSE IF OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET compound_stmt temp_if
        ;
for_stmt :  FOR OPEN_ROUND_BRACKET NR assignment_stmt SEMI_COLON OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET SEMI_COLON assignment_stmt CLOSED_ROUND_BRACKET compound_stmt
       ;	
while_stmt :  WHILE OPEN_ROUND_BRACKET boolean_condition CLOSED_ROUND_BRACKET compound_stmt
	  ;
assignment_stmt :  ID ASSIGNMENT expression
	   ;
expression : term2 term1
	   ;
term1 : PLUS term2 term1 | MINUS term2 term1 | /*empty*/
	    ;
term2 : factor2 factor1
	    ;
factor1 : MUL factor2 factor1 | DIV factor2 factor1 | MOD factor2 factor1 | /*empty*/ 
	  ;
factor2 : OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | CONST | ID | id_index
	  ;
id_index :  ID OPEN_RIGHT_BRACKET CONST CLOSED_RIGHT_BRACKET
		  ;
io_stmt :  READ OPEN_ROUND_BRACKET ID CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET ID CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET CONST CLOSED_ROUND_BRACKET
      ; 
condition : expression GREATER_THAN expression |
	 expression GREATER_OR_EQUAL expression | 
	 expression LOWER_THAN expression |
	 expression LOWER_OR_EQUAL expression | 
	 expression EQUAL expression |
	 expression NOT_EQUAL expression
	  ;
boolean_condition : condition boolean_condition_op
		  ;
boolean_condition_op : /*empty*/ | AND boolean_condition | OR boolean_condition | XOR boolean_condition
		 ; 
%%
int yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}
