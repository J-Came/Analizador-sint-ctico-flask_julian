import ply.yacc as yacc
from lexer import tokens


def p_programa(p):
    'programa : expresiones'
    p[0] = p[1]

def p_expresiones(p):
    '''expresiones : expresion
                   | expresion expresiones'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]

def p_expresion(p):
    '''expresion : identificador ASIGNACION expresion
                 | expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULTIPLICACION expresion
                 | expresion DIVISION expresion
                 | PARENTESIS_ABIERTO expresion PARENTESIS_CERRADO
                 | identificador
                 | NUMERO'''
    if len(p) == 4:  # ASIGNACION o binaria
        p[0] = (p[1], p[2], p[3])  # (izquierda, operador, derecha)
    else:
        p[0] = p[1]  

def p_identificador(p):
    'identificador : IDENTIFICADOR'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f'Símbolo inesperado: {p.value} en la línea {p.lineno}')
    else:
        print('Error de sintaxis en EOF')


parser = yacc.yacc()

def analizar_sintaxis(codigo):
    return parser.parse(codigo)