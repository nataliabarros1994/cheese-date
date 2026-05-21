"""Geracao de graficos dos indicadores de producao."""
import matplotlib

matplotlib.use("Agg")  # backend sem janela (so salva arquivos)
import matplotlib.pyplot as plt
import pandas as pd

from cheesedate.logger import get_logger
from cheesedate.paths import REPORTS

log = get_logger(__name__)

# Paleta de cores do projeto
COR_PRINCIPAL = "#E8A33D"   # amarelo-queijo
COR_SECUNDARIA = "#6B8E4E"  # verde


def grafico_producao_mensal(df_mensal: pd.DataFrame) -> str:
    """Grafico de barras da producao mensal (kg)."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(df_mensal["ano_mes"], df_mensal["kg_total"], color=COR_PRINCIPAL)
    ax.set_title("Producao mensal de queijos (kg)")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Kg produzidos")
    plt.xticks(rotation=45)
    fig.tight_layout()

    caminho = REPORTS / "01_producao_mensal.png"
    fig.savefig(caminho, dpi=120)
    plt.close(fig)
    log.info("Grafico salvo: %s", caminho)
    return str(caminho)


def grafico_ranking_queijos(df_ranking: pd.DataFrame) -> str:
    """Grafico de barras horizontais do faturamento por tipo de queijo."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(df_ranking["tipo_queijo"], df_ranking["faturamento"], color=COR_SECUNDARIA)
    ax.set_title("Faturamento por tipo de queijo (R$)")
    ax.set_xlabel("Faturamento (R$)")
    ax.invert_yaxis()  # maior em cima
    fig.tight_layout()

    caminho = REPORTS / "02_ranking_queijos.png"
    fig.savefig(caminho, dpi=120)
    plt.close(fig)
    log.info("Grafico salvo: %s", caminho)
    return str(caminho)


def grafico_consumo_leite(df_consumo: pd.DataFrame) -> str:
    """Grafico de barras da eficiencia (litros de leite por kg)."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(df_consumo["tipo_queijo"], df_consumo["litros_por_kg"], color=COR_PRINCIPAL)
    ax.set_title("Eficiencia: litros de leite por kg de queijo")
    ax.set_xlabel("Tipo de queijo")
    ax.set_ylabel("Litros de leite / kg")
    plt.xticks(rotation=45)
    fig.tight_layout()

    caminho = REPORTS / "03_consumo_leite.png"
    fig.savefig(caminho, dpi=120)
    plt.close(fig)
    log.info("Grafico salvo: %s", caminho)
    return str(caminho)


def gerar_todos_graficos(df_mensal, df_ranking, df_consumo) -> list[str]:
    """Gera todos os graficos e retorna a lista de caminhos."""
    log.info("Gerando todos os graficos")
    caminhos = [
        grafico_producao_mensal(df_mensal),
        grafico_ranking_queijos(df_ranking),
        grafico_consumo_leite(df_consumo),
    ]
    log.info("%d graficos gerados", len(caminhos))
    return caminhos
