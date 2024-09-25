from cursos_online.usuarios.usuario import Usuario

import pytest

# Casos de e-mails válidos
emails_validos = [
    "usuario@dominio.com",
    "usuario123@dominio.com.br",
    "nome.sobrenome@empresa.org",
    "usuario+tag@dominio.co.uk",
    "email123_456@dominio.net",
    "email@sub.dominio.com",
]

# Casos de e-mails inválidos
emails_invalidos = [
    "usuario@.com",  # Falta o domínio antes do '.'
    "usuario@dominio",  # Falta o sufixo do domínio (como .com, .org)
    "usuario@@dominio.com",  # Duplo '@'
    "@dominio.com",  # Falta a parte antes do '@'
    "usuario@dominio..com",  # Dois pontos consecutivos
    "usuario@dominio,com",  # Uso de vírgula em vez de ponto
    "usuario@dominio com",  # Espaço no e-mail
    "usuario@dominio_com",  # Substituindo '.' por '_'
]


@pytest.mark.parametrize("email", emails_validos)
def test_valida_email_valido(email):
    assert Usuario.valida_email(email) == True, f"O e-mail {email} deveria ser válido"


@pytest.mark.parametrize("email", emails_invalidos)
def test_valida_email_invalido(email):
    assert Usuario.valida_email(email) == False, f"O e-mail {email} deveria ser inválido"
