#Apresentação ao Usuário.
print("Olá, este é um programa que pode calcular a soma, subtração, multiplicação e divisão de dois números!\nVamos digitar os números!\n\n")

# Primeiro numero para o calculo.
n1 = float(input("Digite o primeiro número para o cálculo: "))

# Segundo numero para o calculo.
n2 = float(input("Digite o Segundo número para o cálculo: "))

# Informe o Usuário qual operador ele deverá escolher.
sinais = str(input("Diga qual operador você deseja para a realização do cálculo: \n +\n -\n *\n /\n Escolha um dos operadores acima: "))

#Condições:
if sinais == "+":
    operadores = n1 + n2
    
elif sinais == "-":
    operadores = n1 - n2
    
elif sinais == "*":
    operadores = n1 * n2
    
elif sinais == "/":
    if n2 == 0:
        print("\nNão é possível fazer a divisão por 0, digite novamente!")
        quit()
    else:
        operadores = n1 / n2
        
#Condição se o usuário digitar o formato incorreto.
else:
    print("\nOpção invalida, execute novamente o cálculo!")
    quit()
print(" O calculo de %.2f %s %.2f = %.2f" %(n1,sinais,n2,operadores))

