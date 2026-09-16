"""Regras de calculo para o trabalho de matematica financeira."""

from .descontos import calcular_desconto
from .economia import calcular_economia_mensal

__all__ = ["calcular_desconto", "calcular_economia_mensal"]
