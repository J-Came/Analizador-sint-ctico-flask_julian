import ply.lex as lex

# Definición de los tokens
tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'PARENTESIS_ABIERTO',
    'PARENTESIS_CERRADO',
    'LLAVE_ABIERTO',
    'LLAVE_CERRADO',
    'PUNTO_Y_COMA',
    'ASIGNACION',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',
    'UMINUS',
    'PAR_ABIERTO',
    'PAR_CERRADO',
    'CORCHETE_ABIERTO',
    'CORCHETE_CERRADO',
    'COMILLAS_DOBLES',
    'ENTERO',
    'Y_LOGICO',
    'O_LOGICO',
    'NO_LOGICO',
    'MENOR_QUE',
    'MAYOR_QUE',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'IGUAL',
    'DISTINTO',
    'FLOTANTE',
]

# Palabras reservadas
reservadas = {
    'main': 'MAIN',
    'for': 'FOR',
    'if': 'IF',
    'while': 'WHILE',
    'return': 'RETURN',
}

# Tipos de dato
tipos_dato = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'void': 'VOID'
}

tokens += list(reservadas.values()) + list(tipos_dato.values())

t_ASIGNACION = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'
t_UMINUS = r'-'
t_PAR_ABIERTO = r'\('
t_PAR_CERRADO = r'\)'
t_CORCHETE_ABIERTO = r'\['
t_CORCHETE_CERRADO = r'\]'
t_LLAVE_ABIERTO = r'\{'
t_LLAVE_CERRADO = r'\}'
t_COMILLAS_DOBLES = r'\"'
t_ENTERO = r'\d+'
t_Y_LOGICO = r'&&'
t_O_LOGICO = r'\|\|'
t_NO_LOGICO = r'!'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_FLOTANTE = r'\d+\.\d+'

t_ignore = ' \t'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    elif t.value in tipos_dato:
        t.type = tipos_dato[t.value]
    return t

def t_NUMERO(t):
    r'\d+|\d+\.\d+'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caracter no válido '{t.value[0]}'")
    t.lexer.skip(1)

# Creación del lexer
lexer = lex.lex()

def analizar_codigo(codigo):
    lineas = codigo.split('\n')
    resultado = []

    for i, linea in enumerate(lineas, start=1):  # Agregar un índice a las líneas
        lexer.input(linea)  # Analizar cada línea por separado
        tokens_linea = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_linea.append((tok.type, tok.value))
        resultado.append((i, tokens_linea))  # Cambiar a una tupla (índice, tokens)

    return resultado