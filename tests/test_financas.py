import unittest
from decimal import Decimal

from financas import calcular_desconto, calcular_economia_mensal


class TestSituacaoA(unittest.TestCase):
    def test_aplica_15_por_cento_com_compra_acima_de_cem_e_cupom_valido(self):
        resultado = calcular_desconto(200, "PROMO15")
        self.assertEqual(resultado["valor_desconto"], Decimal("30.00"))
        self.assertEqual(resultado["valor_final"], Decimal("170.00"))
        self.assertTrue(resultado["desconto_aplicado"])

    def test_nao_aplica_desconto_com_cupom_invalido(self):
        resultado = calcular_desconto(200, "OUTRO")
        self.assertEqual(resultado["valor_final"], Decimal("200.00"))
        self.assertFalse(resultado["desconto_aplicado"])

    def test_nao_aplica_desconto_em_compra_de_cem_reais(self):
        resultado = calcular_desconto(100, "PROMO15")
        self.assertEqual(resultado["valor_final"], Decimal("100.00"))


class TestSituacaoB(unittest.TestCase):
    def test_calcula_meses_arredondando_para_cima(self):
        resultado = calcular_economia_mensal(3000, 2000, 2500)
        self.assertEqual(resultado["economia_mensal"], Decimal("1000.00"))
        self.assertEqual(resultado["meses_necessarios"], 3)

    def test_identifica_quando_meta_nao_pode_ser_atingida(self):
        resultado = calcular_economia_mensal(2000, 2000, 1000)
        self.assertFalse(resultado["possivel_atingir_meta"])
        self.assertIsNone(resultado["meses_necessarios"])

    def test_meta_zero_exige_zero_meses(self):
        resultado = calcular_economia_mensal(2000, 2000, 0)
        self.assertEqual(resultado["meses_necessarios"], 0)


if __name__ == "__main__":
    unittest.main()
