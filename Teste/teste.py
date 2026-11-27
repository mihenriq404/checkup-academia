import unittest

from conhecimento import (
    MAPEAMENTO_FATOS,
    REGRAS,
    gerar_fatos_iniciais
)
from inferencia import inferir
from explicacao import explicar_resultado


class TestSistemaEspecialista(unittest.TestCase):

    def criar_perfil_valido(self):
        perfil = {}

        for campo, opcoes in MAPEAMENTO_FATOS.items():
            perfil[campo] = next(iter(opcoes))

        return perfil

    def test_todas_as_regras_de_recomendacao(self):
        regras_recomendacao = [
            regra
            for regra in REGRAS
            if str(regra.get("conclusao", "")).startswith("plano_")
        ]

        self.assertGreaterEqual(len(regras_recomendacao), 20)

        for regra in regras_recomendacao:
            with self.subTest(regra=regra["id"]):
                fatos = set(regra["condicoes"])
                resultado = inferir(fatos)

                self.assertEqual(
                    resultado["plano"],
                    regra["conclusao"]
                )

                self.assertIsNotNone(
                    resultado["regra_recomendacao"]
                )

    def test_sem_conclusao_com_fatos_vazios(self):
        resultado = inferir(set())

        self.assertIsNone(resultado["plano"])
        self.assertIsNone(resultado["regra_recomendacao"])

    def test_perfil_valido_gera_fatos(self):
        perfil = self.criar_perfil_valido()

        fatos = gerar_fatos_iniciais(perfil)

        self.assertIn("perfil_completo", fatos)
        self.assertGreater(len(fatos), 1)

    def test_resposta_invalida_no_perfil(self):
        perfil = self.criar_perfil_valido()
        primeiro_campo = next(iter(MAPEAMENTO_FATOS))

        perfil[primeiro_campo] = "Resposta inválida"

        with self.assertRaises(ValueError):
            gerar_fatos_iniciais(perfil)

    def test_explicacao_apresenta_recomendacao(self):
        regra = next(
            regra
            for regra in REGRAS
            if str(regra.get("conclusao", "")).startswith("plano_")
        )

        resultado = inferir(set(regra["condicoes"]))
        explicacao = explicar_resultado(resultado)

        self.assertIn("Recomendação:", explicacao)
        self.assertIn("Regras ativadas:", explicacao)

    def test_explicacao_sem_recomendacao(self):
        resultado = inferir(set())
        explicacao = explicar_resultado(resultado)

        self.assertIn(
            "Não foi possível recomendar",
            explicacao
        )


if __name__ == "__main__":
    unittest.main()
