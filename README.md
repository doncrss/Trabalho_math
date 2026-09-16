# Trabalho de Matematica Financeira

Projeto em Python dividido em duas situacoes.

## Estrutura

- `financas/descontos.py`: Situacao A, desconto de 15% para compras acima de R$ 100,00 com o cupom `PROMO15`.
- `financas/economia.py`: Situacao B, economia mensal e quantidade de meses para atingir uma meta.
- `app.py`: exemplo de uso pelo terminal.
- `api.py`: API FastAPI para conectar futuramente a um HTML.
- `frontend/`: interface web responsiva para usar as duas situações.
- `tests/`: testes das regras principais.

As funcoes de calculo continuam separadas da API e retornam dicionarios prontos para uso.

## Como executar

Na pasta do projeto:

```bash
python app.py
```

## Como executar a API FastAPI

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
uvicorn api:app --reload
```

Depois, acesse `http://127.0.0.1:8000/docs` para testar os endpoints pela documentacao interativa.

Para usar a interface visual, acesse `http://127.0.0.1:8000/frontend/`.

### Exemplos de requisicao

`POST /desconto`:

```json
{
	"valor_compra": 200,
	"cupom": "PROMO15"
}
```

`POST /economia`:

```json
{
	"renda_mensal": 3000,
	"gastos_fixos": 2000,
	"meta_financeira": 2500
}
```

## Como testar

```bash
python -m unittest discover -s tests -v
```

O projeto usa apenas a biblioteca padrao do Python.
