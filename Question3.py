# Passo 01 — Variável que conta as substrings.
# Passo 02 — Percorrer a ‘string’ s onde passamos por cada caractere para analisar se existem substrings ou não.
# Passo 03 — Percorrer s de trás para frente e ver se há alguma familiaridade que podemos contar como anagrama.
# Isso para não repetir iterações e aumentar os passos desnecessariamente.
# Passo 04 — Comparação com o dicionário d.
# Passo 05 — Adicionar ao resultado o número de substrings que já estão presentes e
# subtrair 1 para caso houver apenas uma ocorrência dessa substring não será um anagrama.
# Passo 06 — Entregar a quantidade


word = str(input("Informe uma palavra: "))
t = list(word)
print(t)


def AnagramasCount(s):
    res = 0  # PASSO 1
    for i in range(1, len(s)):  # PASSO 2
        d = {}
        for j in range(len(s) - i + 1):  # PASSO 3
            sub = ''.join(sorted(s[j:j + i]))
            if sub not in d:  # PASSO 4
                d[sub] = 1
            else:
                d[sub] += 1
            res += d[sub] - 1  # PASSO 5
    return res


print(AnagramasCount(word))  # PASSO 6
