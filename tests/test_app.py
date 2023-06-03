import app


def test_cadastro_aluno():
    assert app.cadastrar_aluno("Vitor Barreto", 26, "vitorbarreto@ufmg.br") == "Ok"

