"""Limpeza e validacao dos dados de producao."""
import pandas as pd

from cheesedate.logger import get_logger

log = get_logger(__name__)


def remover_duplicatas(df: pd.DataFrame) -> pd.DataFrame:
    """Remove linhas completamente duplicadas."""
    antes = len(df)
    df = df.drop_duplicates()
    removidas = antes - len(df)
    log.info("Removidas %d duplicatas", removidas)
    return df


def validar_valores(df: pd.DataFrame) -> pd.DataFrame:
    """Remove registros com valores impossiveis ou invalidos."""
    antes = len(df)

    # Producao e leite tem que ser positivos
    df = df[df["kg_produzido"] > 0]
    df = df[df["litros_leite"] > 0]

    # Preco tem que ser positivo
    df = df[df["preco_kg"] > 0]

    removidas = antes - len(df)
    log.info("Removidos %d registros com valores invalidos", removidas)
    return df


def converter_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """Garante que cada coluna tem o tipo de dado correto."""
    df = df.copy()
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    # Remove linhas onde a data nao pode ser convertida
    antes = len(df)
    df = df.dropna(subset=["data"])
    if antes - len(df) > 0:
        log.info("Removidas %d linhas com data invalida", antes - len(df))

    return df


def adicionar_colunas_calculadas(df: pd.DataFrame) -> pd.DataFrame:
    """Adiciona colunas uteis derivadas dos dados."""
    df = df.copy()

    # Faturamento = kg produzido * preco por kg
    df["faturamento"] = (df["kg_produzido"] * df["preco_kg"]).round(2)

    # Rendimento real = kg de queijo por litro de leite
    df["rendimento"] = (df["kg_produzido"] / df["litros_leite"]).round(3)

    # Componentes da data, uteis para agrupar depois
    df["ano_mes"] = df["data"].dt.to_period("M").astype(str)
    df["dia_semana"] = df["data"].dt.day_name()

    log.info("Adicionadas colunas: faturamento, rendimento, ano_mes, dia_semana")
    return df


def pipeline_limpeza(df: pd.DataFrame) -> pd.DataFrame:
    """Executa todas as etapas de limpeza em sequencia."""
    log.info("Iniciando pipeline de limpeza (%d linhas)", len(df))
    df = remover_duplicatas(df)
    df = converter_tipos(df)
    df = validar_valores(df)
    df = adicionar_colunas_calculadas(df)
    log.info("Pipeline finalizado (%d linhas)", len(df))
    return df
