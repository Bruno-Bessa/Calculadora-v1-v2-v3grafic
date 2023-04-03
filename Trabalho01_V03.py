import customtkinter as tk


#Para importar o customtkinter vá até o terminal e digite "pip install customkinter"
#Use o comando "import customtkinter as tk(Use o 'as tk' para abreviar)"

#Função da operação a se retornar
def operacao():
    try:
        numero_1 = float(entry_numero_1.get())
        numero_2 = float(entry_numero_2.get())
        operador = entry_operador.get()
        if operador == "+":
            resultado = numero_1 + numero_2
        elif operador == "-":
            resultado = numero_1 - numero_2
        elif operador == "*":
            resultado = numero_1 * numero_2
        elif operador == "/":
            if numero_2 == 0:
                resultado = None
            else:
                resultado = numero_1 / numero_2
        else:
            resultado = None
    except (ValueError, TypeError):
        resultado = None
    return resultado
''' Estou usando o sistema try except(ValueError, TypeError): para anular qualquer tipo de mensagem de erro, usando o resultado: none caso tenha alguma ausencia de valor '''
#Funcão de calcular utilizando a função operacao / usando if is not none se caso verdade se não ele vai exibir operador invalido.
def calcular():
    resultado = operacao()
    if resultado is not None:
        label_resultado.configure(text="Resultado: " + str(resultado))
    else:
        label_resultado.configure(text="Operador inválido")

# Criação de janela
janela = tk.CTk()
janela.title("Calculadora")



# Criação dos textos na interface gráfica.
label_numero_1 = tk.CTkLabel(janela, text="Digite o Primeiro Número:")
entry_numero_1 = tk.CTkEntry(janela)
label_operador = tk.CTkLabel(janela, text="Digite o Operador (+, -, * ou /):")
entry_operador = tk.CTkEntry(janela)
label_numero_2 = tk.CTkLabel(janela, text="Digite o Segundo Numero:")
entry_numero_2 = tk.CTkEntry(janela)
button_calcular = tk.CTkButton(janela, text="Calcular", command=calcular)
label_resultado = tk.CTkLabel(janela)

# Posição dos textos e janelas para ficar uniforme.
label_numero_1.grid(row=0, column=0)
entry_numero_1.grid(row=0, column=1)
label_operador.grid(row=1, column=0)
entry_operador.grid(row=1, column=1)
label_numero_2.grid(row=2, column=0)
entry_numero_2.grid(row=2, column=1)
button_calcular.grid(row=3, column=0, columnspan=2)
label_resultado.grid(row=4, column=0, columnspan=2)

# Para continuar rodando a interface gráfica criada(janela)
janela.mainloop()
