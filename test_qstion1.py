import Question1


def test_qst1():
    numero = 1
    caracteres_esperados = (numero + 1) * numero
    piramide = Question1.piramide_reversa(numero)

    assert len(piramide) == caracteres_esperados
