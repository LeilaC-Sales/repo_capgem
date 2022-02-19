import Question2


def test_senha_sem_caract_especial():
    senha = "Ajf580"
    valid = Question2.valid_senha(senha)
    assert not valid


def test_senha_correta():
    senha = "Ajf58#"
    valid = Question2.valid_senha(senha)
    assert valid
