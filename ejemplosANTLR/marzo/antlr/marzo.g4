grammar marzo;

program : function+;

function:
    'def' name=Variable '(' (Variable (',' Variable)* )? ')' 'as' statement #procedure
    ;


expression: 
    expression '+' expression       #suma
    | expression '-' expression     #resta
    | expression '<' expression     #menorque
    | '(' expression ')'            #parens
    | Variable '(' ( expression (',' expression)* )? ')'         #call
    | Numero                        #primaria
    | Variable                      #var
    | String                        #primaria_string
    ;

statement:
    'int' Variable                  #declaracion
    | Variable '=' expression       #asignacion
    | 'printint' '(' expression ')'    #printint
    | 'printstr' '(' expression ')'    #printstr
    | 'if' '(' expression ')' 'then' statement #if
    | 'if' '(' expression ')' 'then' statement 'else' statement #ifelse
    | 'while' '(' expression ')' statement      #while
    | '->' statement+ '<-'          #block
    | 'return' expression           #return
    ;

// A continuación los tokens (comienzan con mayúscula)
Numero : [0-9]+;
String : '"' ~["\r\n]* '"';
Variable : [a-zA-Z]+;
WS : [ \t\n\r]+ -> skip ;


