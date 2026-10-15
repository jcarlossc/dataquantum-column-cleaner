# DataQuantum Column Cleaner

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0%2B-150458.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**DataQuantum Column Cleaner** é uma biblioteca Python para limpeza e padronização dos nomes de colunas de DataFrames do Pandas.

O objetivo é facilitar a preparação de dados para projetos de análise de dados, ciência de dados e engenharia de dados, tornando os nomes das colunas mais consistentes e fáceis de utilizar em pipelines ETL e análises exploratórias.

> Desenvolvido pela **DataQuantum**, marca dedicada a soluções de análise, ciência e engenharia de dados.

## Funcionalidades

- Padronização dos nomes de colunas de DataFrames.
- Conversão dos nomes para um formato consistente.
- Remoção opcional de acentos gráficos.
- Tratamento de nomes de colunas duplicados.
- Retorno de uma cópia do DataFrame, preservando o objeto original.
- Integração com Pandas.

## Requisitos

- Python 3.11 ou superior.
- Pandas 3.0 ou superior.

## Instalação

Com pip

Para instalar a biblioteca usando pip:

```bash
pip install dataquantum-column-cleaner
```
Com Poetry

Para adicionar a biblioteca como dependência de um projeto gerenciado pelo Poetry:

```bash
poetry add dataquantum-column-cleaner
```

## Exemplo de utilização

Considere um DataFrame com nomes de colunas inconsistentes:
```bash
import pandas as pd

df = pd.DataFrame(
    {
        "Nome do Cliente": ["Ana", "Carlos"],
        "nome do cliente": ["Soares", "jose"],
        "Valor Total": [150.50, 275.00],
        "Data Venda": ["2026-01-10", "2026-01-11"],
        "Valor unitário": [10.12, 30.60],
    }
)

print(df.columns.tolist())
```

Saída inicial:

```bash
[
    'Nome do Cliente',
    'nome do cliente',
    'Valor Total',
    'Data Venda',
    'Valor unitário'
]
```

## Aplicando a limpeza

A função clean_column_names() recebe um DataFrame e retorna uma cópia com os nomes das colunas padronizados. O DataFrame original não deve ser alterado.

1. Limpeza padrão

Por padrão, a função realiza a limpeza e remove os acentos gráficos.

```bash
from dataquantum_column_cleaner import clean_column_names

df_clean = clean_column_names(df)

print(df_clean.columns.tolist())
```

Saída esperada:
```bash
[
    'nome_do_cliente',
    'nome_do_cliente_1',
    'valor_total',
    'data_venda',
    'valor_unitario'
]
```

2. Removendo acentos explicitamente

O argumento True solicita explicitamente a remoção dos acentos gráficos.

```bash
df_clean = clean_column_names(df, True)

print(df_clean.columns.tolist())
```

Saída esperada:

```bash
[
    'nome_do_cliente',
    'nome_do_cliente_1',
    'valor_total',
    'data_venda',
    'valor_unitario'
]
```

3. Mantendo os acentos gráficos

O argumento False mantém os acentos, aplicando as demais regras de padronização.

```bash
df_clean = clean_column_names(df, False)

print(df_clean.columns.tolist())
```

Saída esperada:

```bash
[
    'nome_do_cliente',
    'nome_do_cliente_1',
    'valor_total',
    'data_venda',
    'valor_unitário'
]
```

Preservação do DataFrame original

Como a função retorna uma cópia, você pode manter os dados originais e trabalhar com o resultado separadamente:

```bash
df_clean = clean_column_names(df)

print(df.columns.tolist())        # Nomes originais
print(df_clean.columns.tolist())  # Nomes padronizados
```

Essa abordagem facilita a reutilização dos dados originais em diferentes etapas de um pipeline ETL

## Aplicações

A biblioteca pode ser utilizada em:

- **Análise de dados:** padronização de colunas antes da análise exploratória.
- **Ciência de dados:** preparação de variáveis para experimentos e modelos.
- **Engenharia de dados:** normalização de esquemas durante processos ETL.
- **Integração de dados:** organização de nomes de colunas recebidos de diferentes fontes.

## Desenvolvimento

Este projeto utiliza Poetry para gerenciamento de dependências e do ambiente de desenvolvimento.

Clone o repositório:

```bash
git clone https://github.com/jcarlossc/dataquantum-column-cleaner.git
cd dataquantum-column-cleaner
```

Instale as dependências:

```bash
poetry install
```

Execute os testes:

```bash
poetry run task test
```

Execute os testes com cobertura:

```bash
poetry run task cov
```

Execute as verificações de qualidade:

```bash
poetry run task check
```

## Testes e qualidade

O projeto utiliza ferramentas de qualidade e testes automatizados:

- **pytest:** execução dos testes.
- **pytest-cov:** medição da cobertura de testes.
- **Ruff:** análise estática e formatação.
- **mypy:** verificação de tipos.
- **pre-commit:** verificações automatizadas antes dos commits.

## Versionamento

O projeto segue o [Semantic Versioning](https://semver.org/lang/pt-BR/).

As versões seguem o formato:

`MAJOR.MINOR.PATCH`

- **MAJOR:** mudanças incompatíveis.
- **MINOR:** novas funcionalidades compatíveis.
- **PATCH:** correções compatíveis.

Consulte o arquivo [CHANGELOG.md](CHANGELOG.md) para acompanhar as alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

## Autor e contato

**DataQuantum**

GitHub: [jcarlossc](https://github.com/jcarlossc)

Repositório: [dataquantum-column-cleaner](https://github.com/jcarlossc/dataquantum-column-cleaner)
