"""Testes automatizados do pipeline CheeseData."""
from cheesedate.analysis.indicadores import resumo_geral
from cheesedate.clean.limpar import pipeline_limpeza
from cheesedate.collect.gerar_dados import gerar_producao


def test_gerar_producao_tem_dados():
    """A geracao de dados deve produzir registros."""
    df = gerar_producao(dias=30)
    assert len(df) > 0
    assert "tipo_queijo" in df.columns


def test_limpeza_adiciona_colunas():
    """A limpeza deve adicionar as colunas calculadas."""
    df_bruto = gerar_producao(dias=30)
    df_limpo = pipeline_limpeza(df_bruto)
    assert "faturamento" in df_limpo.columns
    assert "rendimento" in df_limpo.columns


def test_limpeza_remove_valores_invalidos():
    """A limpeza deve remover registros com kg negativo."""
    df_bruto = gerar_producao(dias=30)
    # Estraga uma linha de proposito
    df_bruto.loc[0, "kg_produzido"] = -10
    df_limpo = pipeline_limpeza(df_bruto)
    assert (df_limpo["kg_produzido"] > 0).all()


def test_resumo_geral_tem_kpis():
    """O resumo geral deve retornar os KPIs esperados."""
    df = pipeline_limpeza(gerar_producao(dias=30))
    kpis = resumo_geral(df)
    assert kpis["total_registros"] > 0
    assert kpis["faturamento_total"] > 0
