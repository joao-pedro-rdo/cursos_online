from cursos_online.usuarios.usuario import Usuario


# Testes de classes de equivalência e análise de valor limite
def test_senha_minima_valida():
    # Limite inferior válido (8 caracteres)
    assert Usuario.validar_senha("Senha123") == True


def test_senha_maxima_valida():
    # Limite superior válido (16 caracteres)
    assert Usuario.validar_senha("Senha1234567890") == True


def test_senha_abaixo_limite_inferior():
    # Logo abaixo do limite inferior (7 caracteres)
    assert Usuario.validar_senha("Senha1") == False


def test_senha_acima_limite_superior():
    # Logo acima do limite superior (17 caracteres)
    assert Usuario.validar_senha("Senha123456789010") == False


def test_senha_sem_numero_no_limite():
    # Senha no limite inferior, mas sem número (inválida)
    assert Usuario.validar_senha("Somentes") == False


def test_senha_sem_letra_no_limite():
    # Senha no limite inferior, mas sem letra (inválida)
    assert Usuario.validar_senha("12345678") == False


def test_senha_minima_aceitavel():
    # Testando uma senha válida exatamente com 8 caracteres
    assert Usuario.validar_senha("Abc12345") == True


def test_senha_maxima_aceitavel():
    # Testando uma senha válida exatamente com 16 caracteres
    assert Usuario.validar_senha("Senha123Senha123") == True


def test_senha_curta():
    # Menos de 8 caracteres
    assert Usuario.validar_senha("Abc12") == False


def test_senha_longa():
    # Mais de 16 caracteres
    assert Usuario.validar_senha("Senha1234567890123") == False
