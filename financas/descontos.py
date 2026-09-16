"""Situacao A: calculadora de desconto com cupom promocional."""

from decimal import Decimal, ROUND_HALF_UP

VALOR_MINIMO_DESCONTO = Decimal("50.00")
PERCENTUAL_DESCONTO = Decimal("0.15")
CUPONS_VALIDOS = {
    "PROMO15",
    "PROMO10",
    "DESCONTO15",
    "ECONOMIZE15",
    "CLIENTE15",
    "OFERTA15",
}


def dinheiro(valor: Decimal) -> Decimal:
    return valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calcular_desconto(valor_compra: float | Decimal, cupom: str) -> dict:
    """Calcula o valor final de uma compra com o cupom promocional."""
    valor = dinheiro(Decimal(str(valor_compra)))
    if valor < 0:
        raise ValueError("O valor da compra nao pode ser negativo.")

    cupom_informado = cupom.strip().upper()
    cupom_valido = cupom_informado in CUPONS_VALIDOS
    desconto_aplicado = valor > VALOR_MINIMO_DESCONTO and cupom_valido
    desconto = dinheiro(valor * PERCENTUAL_DESCONTO) if desconto_aplicado else Decimal("0.00")
    valor_final = dinheiro(valor - desconto)

    return {
        "valor_original": valor,
        "cupom_valido": cupom_valido,
        "desconto_aplicado": desconto_aplicado,
        "percentual_desconto": PERCENTUAL_DESCONTO if desconto_aplicado else Decimal("0.00"),
        "valor_desconto": desconto,
        "valor_final": valor_final,
    }
