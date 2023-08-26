# Definición de la función para evaluar una expresión lógica en notación polaca inversa
def evaluar_expresion(expresion, valores):
    pila = []  # Se utiliza una pila para realizar el cálculo
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
            pila.append(valores[token])  # Si no es un operador, es una variable, se agrega su valor a la pila
    return pila.pop()  # Al final, queda el resultado en la pila

# Definición de la función para generar la tabla de verdad de una expresión lógica
def generar_tabla_verdad(expresion, variables):
    num_variables = len(variables)
    tabla = []
    
    # Se generan todas las combinaciones posibles de valores para las variables
    for i in range(2 ** num_variables):
        valores = {}
        for j in range(num_variables):
            valores[variables[j]] = bool(i & (1 << (num_variables - 1 - j)))
        resultado = evaluar_expresion(expresion, valores)  # Se evalúa la expresión con los valores actuales
        tabla.append((valores, resultado))  # Se agrega la entrada (valores) y el resultado a la tabla
    
    return tabla

# Programa principal
expresion = ['A', 'B', 'AND', 'C', 'OR', 'NOT']  # Ejemplo de expresión: (A AND B) OR (NOT C)
variables = ['A', 'B', 'C']
tabla_verdad = generar_tabla_verdad(expresion, variables)

# Se imprime la tabla de verdad generada
for entrada, resultado in tabla_verdad:
    print(entrada, resultado)

#No pude asistir a la clase de hoy debido a unos problemas personales, pero aqui esta mi trabajo