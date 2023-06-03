from app import cadastrar_aluno


def test_cadastro_aluno():
    assert cadastrar_aluno("Vitor Barreto", 26, "vitorbarreto@ufmg.br") == "Ok"

