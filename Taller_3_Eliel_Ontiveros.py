def evaluar_expresion(expresion, valores):
    pila = []
    for token in expresion:
        if token == 'AND':
            operand2 = pila.pop()
            operand1 = pila.pop()
            resultado = operand1 and operand2
            pila.append(resultado)
        elif token == 'OR':
            operand2 = pila.pop()
            operand1 = pila.pop()
            resultado = operand1 or operand2
            pila.append(resultado)
        elif token == 'NOT':
            operand = pila.pop()
            resultado = not operand
            pila.append(resultado)
        else:
            pila.append(valores[token])
    return pila.pop()

def generar_tabla_verdad(expresion, variables):
    num_variables = len(variables)
    tabla = []
    
    for i in range(2 ** num_variables):
        valores = {}
        for j in range(num_variables):
            valores[variables[j]] = bool(i & (1 << (num_variables - 1 - j)))
        resultado = evaluar_expresion(expresion, valores)
        tabla.append((valores, resultado))
    
    return tabla

# Programa principal
expresion = ['A', 'B', 'AND', 'C', 'OR', 'NOT']  # Ejemplo de expresión: (A AND B) OR (NOT C)
variables = ['A', 'B', 'C']
tabla_verdad = generar_tabla_verdad(expresion, variables)

for entrada, resultado in tabla_verdad:
    print(entrada, resultado)
