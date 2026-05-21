"""Pipeline completo do CheeseData: dos dados brutos ao relatorio Excel."""
from cheesedate.analysis.indicadores import (
    consumo_materia_prima,
    producao_mensal,
    ranking_queijos,
    resumo_geral,
)
from cheesedate.clean.limpar import pipeline_limpeza
from cheesedate.collect.gerar_dados import gerar_producao, salvar_dados
from cheesedate.excel.gerar_planilha import gerar_planilha_excel
from cheesedate.logger import get_logger
from cheesedate.viz.graficos import gerar_todos_graficos

log = get_logger(__name__)


def executar_pipeline() -> str:
    """Executa todas as etapas do projeto em sequencia.

    Returns:
        Caminho da planilha Excel gerada.
    """
    log.info("=== INICIANDO PIPELINE CHEESEDATA ===")

    # 1. Gera e salva os dados brutos
    df_bruto = gerar_producao()
    salvar_dados(df_bruto)

    # 2. Limpa e valida
    df = pipeline_limpeza(df_bruto)

    # 3. Calcula indicadores
    kpis = resumo_geral(df)
    df_mensal = producao_mensal(df)
    df_ranking = ranking_queijos(df)
    df_consumo = consumo_materia_prima(df)

    # 4. Gera graficos
    gerar_todos_graficos(df_mensal, df_ranking, df_consumo)

    # 5. Gera a planilha Excel final
    caminho = gerar_planilha_excel(kpis, df_mensal, df_ranking, df_consumo, df)

    log.info("=== PIPELINE CONCLUIDO ===")
    log.info("Relatorio final: %s", caminho)
    return caminho


if __name__ == "__main__":
    executar_pipeline()
