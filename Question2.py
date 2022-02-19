# QUESTÃO 2 - DESAFIO DA CAPGEMINI - 2022

"""
Débora inscreveu-se numa rede social para se manter em contato com os seus amigos.
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte.
O "site" considera uma senha forte quando ela satisfaz alguns critérios.
Débora digitou uma 'string' aleatória no campo de senha, porém ela não tem certeza se é uma senha forte.
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados
para uma string qualquer ser considerada segura.
"""


# PASSO 1 - Contagem de caracteres total.
# PASSO 2 - Contagem de letras minúsculas.
# PASSO 3 - Contagem de letras maiúsculas.
# PASSO 4 - Contagem de dígitos.
# PASSO 5 - Contagem de caracteres especiais.


def valid_senha(s):
    minusc, maiusc, espec, dig = 0, 0, 0, 0
    # Contagem de caracteres total.
    if len(s) >= 6:
        for i in s:

            # Contagem de letras minúsculas.
            if i.islower():
                minusc += 1

            # Contagem de letras maiúsculas.
            if i.isupper():
                maiusc += 1

            # Contagem de dígitos.
            if i.isdigit():
                dig += 1

            # Contagem de caracteres especiais.
            if i == '@' or i == '$' or i == '_' or i == '!' or i == '#' or i == '%' or i == '&' or i == '*' or i == '+':
                espec += 1
    if (minusc >= 1 and maiusc >= 1 and espec >= 1 and dig >= 1 and
            minusc + espec + maiusc + dig == len(s)):
        return True
    else:
        return False
