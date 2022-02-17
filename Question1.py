# Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
# A base e altura da escada devem ser iguais ao valor de n.
# A última linha não deve conter nenhum espaço.

# PASSO 1 — Loop para criação de colunas
# PASSO 2 — Criação de espaços
# PASSO 3 — Criação de símbolos

totColunas = int(input("Digite um valor: "))

for coluna in range(1, totColunas + 1):  # PASSO 1
    # Criação de espaços
    for espc in range(1, (totColunas - coluna) + 1):  # PASSO 2
        print(" ", end="")

    # display de *
    for simbolo in range(1, coluna + 1):  # PASSO 3
        print("*", end="")  # Qualquer outro símbolo pode ser utilizado. Basta fazer a alteração nas aspas.

    print()