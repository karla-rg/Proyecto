exp = '((4+3)*(2+8))'

def interpreta(exp):
    """Interpreta una expresión matemática que incluye *+() y
    números de un dígito. Devuelve el resultado.
    """
    # El algoritmo funciona con dos stacks
    ops, vals = [], []
    for t in list(exp):
        if t  == '(': continue
        elif t in '*+':
            ops.append(t)
        elif t == ')':
            op = ops.pop()
            a = vals.pop()
            b = vals.pop()
            # Aquí se EJECUTA la operación
            if op == '+':
                vals.append(a+b)
            elif op == '*':
                vals.append(a*b)
        else:
            # Aquí se EJECUTA la conversión de char a int
            vals.append(int(t))
        # print vals
    # En el tope de la pila queda el resultado
    return vals.pop()

# lambda simplemente crea una función, de tal modo que estas tres funciones
# no regresan el resultado de EJECUTAR la operación sino la FUNCIÓN que regresaría
# el resultado al aplicar la operación (gracias al lexical scope)
def numero(x): return lambda: int(x)
# Nótese que tanto suma como multiplicación reciben objetos ejecutables como parámetros
def suma(y, z): return lambda: y() + z()
def mult(y, z): return lambda: y() * z()

def compila(exp):
    """Compila una expresión matemática que incluye *+() y
    números de un dígito a objeto interno de python.
    Devuelve un objeto ejecutable (una función).
    """
    ops, vals = [], []
    for token in list(exp):
        if token  == '(': continue
        elif token in '*+':
            # Guardo una función en la pila
            if token == '+': ops.append(suma)
            elif token == '*': ops.append(mult)            
        elif token == ')':
            # Saco de la pila una función, la aplico y eso me regresa
            # un objeto ejecutable
            vals.append( ops.pop()(vals.pop(), vals.pop()) )
        else:
            # En el stack de valores guardo el objeto ejecutable
            # que me convierte el caracter como número
            vals.append(numero(token))        
    # En el tope de la pila queda un objeto que al ejecutarse calcula el resultado
    return vals.pop()

if __name__ == '__main__':
    print("Ejecutando intérprete... Resultado:")
    print(interpreta(exp))
    print("Ejecutando compilador... Resultado:")
    x = compila(exp)
    print(x)
    print("Ahora ejecuto el objeto que me regresó el compilador:")
    print(x())