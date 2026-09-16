"""Executa as duas situacoes pelo terminal.

A camada de calculo esta no pacote `financas`, pronta para ser chamada por um HTML.
"""

from financas import calcular_desconto, calcular_economia_mensal


def moeda(valor) -> str:
    return f"R$ {valor:.2f}".replace(".", ",")


def executar_situacao_a() -> None:
    print("\nSITUACAO A - DESCONTO COM CUPOM")
    valor = float(input("Valor da compra: R$ ").replace(",", "."))
    cupom = input("Cupom (use PROMO15): ")
    resultado = calcular_desconto(valor, cupom)
    print(f"Valor original: {moeda(resultado['valor_original'])}")
    print(f"Desconto: {moeda(resultado['valor_desconto'])}")
    print(f"Valor final: {moeda(resultado['valor_final'])}")


def executar_situacao_b() -> None:
    print("\nSITUACAO B - ECONOMIA MENSAL")
    renda = float(input("Renda mensal: R$ ").replace(",", "."))
    gastos = float(input("Gastos fixos: R$ ").replace(",", "."))
    meta = float(input("Meta financeira: R$ ").replace(",", "."))
    resultado = calcular_economia_mensal(renda, gastos, meta)
    print(f"Economia mensal: {moeda(resultado['economia_mensal'])}")
    if resultado["possivel_atingir_meta"]:
        print(f"Meses necessarios: {resultado['meses_necessarios']}")
    else:
        print("Nao e possivel atingir a meta com essa economia mensal.")


def main() -> None:
    print("CALCULADORA FINANCEIRA")
    print("1 - Desconto com cupom")
    print("2 - Economia mensal")
    opcao = input("Escolha uma situacao: ").strip()
    if opcao == "1":
        executar_situacao_a()
    elif opcao == "2":
        executar_situacao_b()
    else:
        print("Opcao invalida.")


if __name__ == "__main__":
    main()
