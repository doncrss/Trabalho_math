"""Situacao B: simulador de economia mensal."""

from decimal import Decimal, ROUND_CEILING, ROUND_HALF_UP


def _dinheiro(valor: Decimal) -> Decimal:
    return valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calcular_economia_mensal(
    renda_mensal: float | Decimal,
    gastos_fixos: float | Decimal,
    meta_financeira: float | Decimal,
) -> dict:
    """Calcula a economia mensal e os meses necessarios para atingir uma meta."""
    renda = _dinheiro(Decimal(str(renda_mensal)))
    gastos = _dinheiro(Decimal(str(gastos_fixos)))
    meta = _dinheiro(Decimal(str(meta_financeira)))

    if renda < 0 or gastos < 0 or meta < 0:
        raise ValueError("Renda, gastos e meta devem ser maiores ou iguais a zero.")

    economia = _dinheiro(renda - gastos)
    if meta == 0:
        meses = 0
    elif economia <= 0:
        meses = None
    else:
        meses = int((meta / economia).to_integral_value(rounding=ROUND_CEILING))

    return {
        "renda_mensal": renda,
        "gastos_fixos": gastos,
        "economia_mensal": economia,
        "meta_financeira": meta,
        "meses_necessarios": meses,
        "possivel_atingir_meta": meses is not None,
    }
