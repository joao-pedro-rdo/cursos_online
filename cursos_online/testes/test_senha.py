from cursos_online.usuarios.usuario import Usuario

import pytest

# Casos de senhas válidas
senhas_validas = [
    "Senha123",  # 7 caracteres: 6 letras e 1 número
    "Senha1234567890",  # 15 caracteres: 10 letras e 5 números
    "Abc12345",  # 8 caracteres: 3 letras e 5 números
    "Senha123Senha123",  # 16 caracteres: 10 letras e 6 números
]

# Casos de senhas inválidas
senhas_invalidas = [
    "Senhao1",  # 7 caracteres: 6 letras e 1 número
    "Letrass",  # 7 caracteres: 7 letras
    "1234567",  # 7 caracteres: 7 números
    "Senha123456789010",  # 17 caracteres: 10 letras e 7 números
    "LetrasMuitasuiqup",  # 17 caracteres: 17 letras
    "12345678901234567",  # 17 caracteres: 17 números
    "Letlkdnmaslkdma",  # 15 caracteres: 15 letras
    "348573284732098",  # 15 números
    "Somentes",  # 8 caracteres: 8 letras
    "12345678",  # 8 caracteres: 8 números
    "A12",  # 3 caracteres: 1 letra e 2 números
    "Let",  # 3 caracteres: 3 letras
    "678",  # 3 caracteres: 3 números
    "",  # 0 caracteres: vazio
    "Senha123456789012387e34324",  # 26 caracteres: 19 letras e 7 números
    "MuitasLetrasSomenteLetras",  # 26 caracteres: 26 letras
    "12345678901234567890123456",  # 26 caracteres: 26 números
    "SomenteLe",  # 9 caracteres: 9 letras
    "123456789",  # 9 caracteres: 9 números
    "dkas d1651",  # valido com espaço
    "DDS,@FDLAD$%",  # valido com caracteres especiai
]


@pytest.mark.parametrize("senha", senhas_validas)
def test_senha_valida(senha):
    assert Usuario.validar_senha(senha) == True, f"A senha '{senha}' deveria ser válida"


@pytest.mark.parametrize("senha", senhas_invalidas)
def test_senha_invalida(senha):
    assert Usuario.validar_senha(senha) == False, f"A senha '{senha}' deveria ser inválida"
