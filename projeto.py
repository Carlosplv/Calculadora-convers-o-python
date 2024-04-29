import os
os.system('cls')  # Limpa o console para iniciar com uma tela limpa.

# Nomes dos integrantes do projeto
integrantes = [
    "Carlos Furtado | RGM-537273418",
    "Leonardo Leone | RGM-38716143 ",
    "Pedro Souza | RGM-538083477",
    "Joao Perceco | RGM-38716046 ",
    "Gabriel Melo | RGM-538597861 "
]

# Nome do projeto
nome_projeto = "Projeto de Conversão de Decimal para Hexadecimal, Octal e Binário"

# Mensagem de apresentação do projeto
mensagem_apresentacao = f"""
{nome_projeto}
===============================
Este projeto foi desenvolvido por:
- {integrantes[0]}
- {integrantes[1]}
- {integrantes[2]}
- {integrantes[3]}
- {integrantes[4]}
"""

# Imprime a mensagem de apresentação no console
print(mensagem_apresentacao)

# Mensagem para a opção "SOBRE"
mensagem_sobre = """
SOBRE
===============================

INSTITUIÇÃO UNIVERSIDADE CRUZEIRO DO SUL, CAMPUS ANÁLIA FRANCO, BACHARELADO CIÊNCIAS DA COMPUTAÇÃO, 1° SEMESTRE.

Bem-vindo à Calculadora Inversora de Decimal para outras bases!
Esta ferramenta permite converter números decimais para Binário, Octal e Hexadecimal.

Foi desenvolvida como parte de um projeto universitário por:
- Carlos Furtado RGM-537273418
- Leonardo Leone RGM-38716143
- Pedro Souza RGM-538083477
- Joao Perceco RGM-38716046
- Gabriel Melo Botelho RGM-538597861    

Instruções de uso:
1. Para converter um número decimal, escolha uma das opções:
   - [1] Converter para Binário
   - [2] Converter para Octal
   - [3] Converter para Hexadecimal
2. Para sair, escolha a opção [5].

Esperamos que este projeto seja útil para você! Selecione uma opção para começar.
"""

print("CALCULADORA INVERSORA DE DECIMAL - OUTRAS BASES")  # Título do programa

# Loop principal para controlar a execução do programa
while True:
    # Solicita ao usuário que escolha uma opção do menu
    op = input("Digite uma opção: [1] BINÁRIO || [2] OCTAL || [3] HEXADECIMAL || [4] SOBRE || [5] SAIR: ")

    # Se a opção for "1", inicia a conversão para binário
    if op == '1':
        print("BINÁRIO [2]")

        # Solicita ao usuário um número decimal como entrada
        num_input = input("Digite um número decimal: ")

        # Continua perguntando até que uma entrada válida seja recebida
        while not (num_input.isdigit() or (num_input.startswith('-') and num_input[1:].isdigit())):
            # Se a entrada não for válida, informa o usuário
            print("Entrada inválida! Por favor, insira um número inteiro.")
            num_input = input("Digite um número decimal: ")

        # Converte a entrada para um número inteiro
        num = int(num_input)

        # Inicia a conversão para binário
        binario = ''
        temp_num = num  # Para preservar o valor original
        while temp_num != 0:
            # Adiciona o resto da divisão por 2 ao início da string
            binario = str(temp_num % 2) + binario
            temp_num //= 2  # Divide por 2 para obter o próximo bit

        # Exibe o resultado da conversão
        print(f"O número {num} em binário é: {binario}")

    # Se a opção for "2", inicia a conversão para octal
    elif op == '2':
        print("OCTAL [8]")

        num_input = input("Digite um número decimal: ")

        # Verifica se a entrada é um número inteiro válido
        while not (num_input.isdigit() or (num_input.startswith('-') and num_input[1:].isdigit())):
            print("Entrada inválida! Por favor, insira um número inteiro.")
            num_input = input("Digite um número decimal: ")

        # Converte para um número inteiro
        num = int(num_input)

        octal = ''
        temp_num = num  # Preserva o valor original
        while temp_num != 0:
            # Adiciona o resto da divisão por 8 ao início da string
            octal = str(temp_num % 8) + octal
            temp_num //= 8  # Divide por 8 para obter o próximo dígito

        print(f"O número {num} em octal é: {octal}")

    # Se a opção for "3", inicia a conversão para hexadecimal
    elif op == '3':
        print("HEXADECIMAL [16]")

        num_input = input("Digite um número decimal: ")

        # Verifica se a entrada é um número inteiro válido
        while not (num_input.isdigit() or (num_input.startswith('-') and num_input[1:].isdigit())):
            print("Entrada inválida! Por favor, insira um número inteiro.")
            num_input = input("Digite um número decimal: ")

        # Converte para um número inteiro
        num = int(num_input)

        hexadecimal = ''
        hex_chars = "0123456789ABCDEF"  # Conjunto de caracteres hexadecimais
        temp_num = num  # Preserva o valor original
        while temp_num != 0:
            # Adiciona o caractere correspondente ao resto da divisão por 16 ao início da string
            hexadecimal = hex_chars[temp_num % 16] + hexadecimal
            temp_num //= 16  # Divide por 16 para obter o próximo dígito

        print(f"O número {num} em hexadecimal é: {hexadecimal}")

    # Se a opção for "4", exibe informações sobre o projeto
    elif op == '4':
        print(mensagem_sobre)

    # Se a opção for "5", encerra o programa
    elif op == '5':
        print('---------- PROGRAMA ENCERRADO! OBRIGADO POR USAR NOSSA CALCULADORA ---------')
        break  # Sai do loop para encerrar o programa

    # Se a opção for inválida, pede para escolher entre [1] e [5]
    else:
        print("OPÇÃO INVÁLIDA. Escolha uma opção entre [1] e [5].")