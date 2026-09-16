import unittest

from fastapi.testclient import TestClient

from api import app


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cliente = TestClient(app)

    def test_rota_de_desconto(self):
        resposta = self.cliente.post(
            "/desconto",
            json={"valor_compra": 200, "cupom": "PROMO15"},
        )
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["valor_final"], 170.0)

    def test_rota_de_economia(self):
        resposta = self.cliente.post(
            "/economia",
            json={
                "renda_mensal": 3000,
                "gastos_fixos": 2000,
                "meta_financeira": 2500,
            },
        )
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["meses_necessarios"], 3)

    def test_rejeita_valor_negativo(self):
        resposta = self.cliente.post(
            "/desconto",
            json={"valor_compra": -10, "cupom": "PROMO15"},
        )
        self.assertEqual(resposta.status_code, 422)


if __name__ == "__main__":
    unittest.main()
