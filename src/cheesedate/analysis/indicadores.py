"""Calculo dos indicadores de producao de queijos."""
import pandas as pd

from cheesedate.logger import get_logger

log = get_logger(__name__)


def producao_mensal(df: pd.DataFrame) -> pd.DataFrame:
    """Resumo de producao agrupado por mes."""
    resumo = df.groupby("ano_mes").agg(
        kg_total=("kg_produzido", "sum"),
        litros_leite=("litros_leite", "sum"),
        faturamento=("faturamento", "sum"),
        registros=("kg_produzido", "count"),
    ).round(2).reset_index()
    log.info("Producao mensal calculada (%d meses)", len(resumo))
    return resumo


def ranking_queijos(df: pd.DataFrame) -> pd.DataFrame:
    """Ranking dos tipos de queijo por producao e faturamento."""
    resumo = df.groupby("tipo_queijo").agg(
        kg_total=("kg_produzido", "sum"),
        faturamento=("faturamento", "sum"),
        rendimento_medio=("rendimento", "mean"),
    ).round(2)
    resumo = resumo.sort_values("faturamento", ascending=False).reset_index()
    log.info("Ranking de %d tipos de queijo calculado", len(resumo))
    return resumo


def producao_por_dia_semana(df: pd.DataFrame) -> pd.DataFrame:
    """Producao media por dia da semana."""
    ordem = ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]
    resumo = df.groupby("dia_semana").agg(
        kg_total=("kg_produzido", "sum"),
        kg_medio=("kg_produzido", "mean"),
    ).round(2)
    # Reordena para a ordem natural da semana
    resumo = resumo.reindex(ordem).dropna().reset_index()
    log.info("Producao por dia da semana calculada")
    return resumo


def consumo_materia_prima(df: pd.DataFrame) -> pd.DataFrame:
    """Consumo de leite por tipo de queijo."""
    resumo = df.groupby("tipo_queijo").agg(
        litros_total=("litros_leite", "sum"),
        kg_produzido=("kg_produzido", "sum"),
    ).round(2)
    # Litros de leite necessarios para 1 kg de queijo
    resumo["litros_por_kg"] = (resumo["litros_total"] / resumo["kg_produzido"]).round(2)
    resumo = resumo.sort_values("litros_total", ascending=False).reset_index()
    log.info("Consumo de materia-prima calculado")
    return resumo


def resumo_geral(df: pd.DataFrame) -> dict:
    """Indicadores gerais (KPIs) do periodo todo."""
    kpis = {
        "total_registros": len(df),
        "kg_total": round(df["kg_produzido"].sum(), 2),
        "litros_total": round(df["litros_leite"].sum(), 2),
        "faturamento_total": round(df["faturamento"].sum(), 2),
        "tipos_diferentes": df["tipo_queijo"].nunique(),
        "rendimento_medio": round(df["rendimento"].mean(), 3),
    }
    log.info("Resumo geral calculado: %d KPIs", len(kpis))
    return kpis
