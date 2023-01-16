
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     ID = 258,
     CONST = 259,
     ARRAY = 260,
     IF = 261,
     ELSE = 262,
     FOR = 263,
     WHILE = 264,
     EXEC = 265,
     AND = 266,
     OR = 267,
     XOR = 268,
     READ = 269,
     WRITE = 270,
     STR = 271,
     NR = 272,
     VAR = 273,
     ASSIGNMENT = 274,
     EQUAL = 275,
     NOT_EQUAL = 276,
     LOWER_OR_EQUAL = 277,
     GREATER_OR_EQUAL = 278,
     LOWER_THAN = 279,
     GREATER_THAN = 280,
     NOT = 281,
     PLUS = 282,
     MINUS = 283,
     DIV = 284,
     MUL = 285,
     MOD = 286,
     DOT = 287,
     COMMA = 288,
     SEMI_COLON = 289,
     COLON = 290,
     SPACE = 291,
     OPEN_CURLY_BRACKET = 292,
     CLOSED_CURLY_BRACKET = 293,
     OPEN_ROUND_BRACKET = 294,
     CLOSED_ROUND_BRACKET = 295,
     OPEN_RIGHT_BRACKET = 296,
     CLOSED_RIGHT_BRACKET = 297,
     READ_OP = 298,
     WRITE_OP = 299
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


