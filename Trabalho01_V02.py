def operacao():
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        operador = input("Insira o operador (+, -, * ou /): ")
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("Não é possível dividir por zero")
                resultado = None
            else:
                resultado = num1 / num2
        else:
            print("Operador inválido")
            resultado = None
    except (ValueError, TypeError):
        print("Entrada inválida")
        resultado = None
    return resultado

resultado = operacao()
if resultado is not None:
    print("O resultado é:", resultado)

