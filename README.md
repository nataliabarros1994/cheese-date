# 🧀 CheeseDate — Automação de Relatórios de Produção de Laticínios

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![openpyxl](https://img.shields.io/badge/openpyxl-3.1-orange.svg)](https://openpyxl.readthedocs.io/)

Ferramenta de **automação de planilhas Excel** que transforma dados brutos de produção de queijos em um **relatório profissional** — com múltiplas abas, formatação, indicadores e gráficos editáveis — gerado 100% por código Python.

---

## 🎯 O problema

Fábricas de laticínios costumam controlar a produção em planilhas manuais: trabalhoso, propenso a erro e sem visão analítica. O CheeseData automatiza esse processo de ponta a ponta.

## ✨ O que o projeto faz

- **Gera** uma base de dados de produção (volume, tipos de queijo, consumo de leite)
- **Limpa e valida** os dados (remove duplicatas, valores inválidos, padroniza tipos)
- **Calcula indicadores**: produção mensal, ranking de queijos, consumo de matéria-prima, produção por dia da semana
- **Cria gráficos** dos principais indicadores
- **Gera automaticamente** uma planilha Excel `.xlsx` com 5 abas formatadas e gráficos nativos editáveis

## 📊 Indicadores analisados

| Indicador | Insight gerado |
|-----------|----------------|
| Produção mensal | Evolução do volume ao longo do tempo |
| Ranking de queijos | Quais tipos mais faturam |
| Consumo de matéria-prima | Litros de leite por kg — eficiência por tipo |
| Produção por dia da semana | Padrões de produção semanal |

## 🛠️ Stack Técnica

- **Python 3.13**
- **pandas** — manipulação e análise de dados
- **openpyxl** — automação e formatação de Excel
- **matplotlib** — geração de gráficos
- **pytest** — testes automatizados
- **ruff** — qualidade de código

## 🏗️ Estrutura do projeto

```
cheesedate/
├── src/cheesedate/      ← código-fonte do projeto
│   ├── collect/         ← geração/coleta de dados
│   ├── clean/           ← limpeza e validação
│   ├── analysis/        ← análise (EDA, indicadores)
│   ├── excel/           ← automação de Excel (o coração!)
│   └── viz/             ← gráficos
├── data/
│   ├── raw/             ← dados brutos
│   ├── processed/       ← dados limpos
│   └── output/          ← planilhas Excel geradas
├── tests/               ← testes automatizados
├── reports/             ← relatórios e figuras
└── notebooks/           ← exploração
```

## 🚀 Como usar

```bash
# Clone o repositório
git clone https://github.com/nataliabarros1994/cheesedate.git
cd cheesedate

# Crie o ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -e ".[dev]"

# Rode o pipeline completo
python -m cheesedate.run
```

A planilha final é gerada em `data/output/relatorio_producao_queijos.xlsx`.

## 🧪 Testes

```bash
pytest -v
```

## 📈 Resultado

O projeto gera uma planilha Excel profissional com 5 abas:
**Resumo** (KPIs), **Produção Mensal**, **Ranking de Queijos**, **Consumo de Leite** e **Dados Completos** — todas formatadas e com gráficos editáveis.

---

## 👩‍💻 Autora

**Natalia Barros** — Cientista de Dados

- 💼 [LinkedIn](https://www.linkedin.com/in/seu-perfil)

## 📄 Licença

MIT

