"""API FastAPI para as situacoes de matematica financeira."""

from decimal import Decimal
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from financas import calcular_desconto, calcular_economia_mensal

app = FastAPI(
    title="Calculadora Financeira",
    description="API para desconto promocional e simulacao de economia mensal.",
    version="1.0.0",
)


class DescontoRequest(BaseModel):
    valor_compra: Decimal = Field(
        ...,
        ge=0,
        description="Valor total da compra. Use um valor acima de R$ 50,00.",
        examples=[200],
    )
    cupom: str = Field(..., description="Cupom promocional. Use PROMO15.", examples=["PROMO15"])


class EconomiaRequest(BaseModel):
    renda_mensal: Decimal = Field(..., ge=0)
    gastos_fixos: Decimal = Field(..., ge=0)
    meta_financeira: Decimal = Field(..., ge=0)


def converter_decimais(resultado: dict) -> dict:
    """Converte Decimal para numero antes de enviar a resposta JSON."""
    return {
        chave: float(valor) if isinstance(valor, Decimal) else valor
        for chave, valor in resultado.items()
    }


@app.get("/")
def inicio() -> dict:
    return {
        "mensagem": "API da Calculadora Financeira",
        "documentacao": "/docs",
        "rotas": ["POST /desconto", "POST /economia"],
    }


@app.post("/desconto")
def desconto(dados: DescontoRequest) -> dict:
    try:
        resultado = calcular_desconto(dados.valor_compra, dados.cupom)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro)) from erro
    return converter_decimais(resultado)


@app.post("/economia")
def economia(dados: EconomiaRequest) -> dict:
    try:
        resultado = calcular_economia_mensal(
            dados.renda_mensal,
            dados.gastos_fixos,
            dados.meta_financeira,
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro)) from erro
    return converter_decimais(resultado)


app.mount(
    "/frontend",
    StaticFiles(directory=Path(__file__).parent / "frontend", html=True),
    name="frontend",
)
