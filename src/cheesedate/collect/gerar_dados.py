"""Geracao de dados sinteticos de producao de queijos."""
import numpy as np
import pandas as pd

from cheesedate.logger import get_logger
from cheesedate.paths import DATA_RAW

log = get_logger(__name__)

# Tipos de queijo e suas caracteristicas (rendimento = kg queijo por litro de leite)
TIPOS_QUEIJO = {
    "Minas Frescal": {"rendimento": 0.18, "preco_kg": 32.0},
    "Mussarela": {"rendimento": 0.10, "preco_kg": 45.0},
    "Prato": {"rendimento": 0.10, "preco_kg": 48.0},
    "Parmesao": {"rendimento": 0.08, "preco_kg": 89.0},
    "Coalho": {"rendimento": 0.15, "preco_kg": 38.0},
    "Ricota": {"rendimento": 0.06, "preco_kg": 28.0},
}


def gerar_producao(dias: int = 180, seed: int = 42) -> pd.DataFrame:
    """Gera registros sinteticos de producao diaria de queijos.

    Args:
        dias: numero de dias de producao a simular.
        seed: semente aleatoria para reprodutibilidade.

    Returns:
        DataFrame com os registros de producao.
    """
    rng = np.random.default_rng(seed)
    log.info("Gerando %d dias de producao de queijos", dias)

    datas = pd.date_range(end=pd.Timestamp.today().normalize(), periods=dias, freq="D")
    tipos = list(TIPOS_QUEIJO.keys())

    registros = []
    for data in datas:
        # Cada dia produz de 2 a 4 tipos diferentes de queijo
        n_tipos = rng.integers(2, 5)
        tipos_do_dia = rng.choice(tipos, size=n_tipos, replace=False)

        for tipo in tipos_do_dia:
            info = TIPOS_QUEIJO[tipo]
            litros_leite = float(rng.integers(200, 1500))
            # Producao = leite * rendimento, com pequena variacao
            variacao = rng.normal(1.0, 0.05)
            kg_produzido = round(litros_leite * info["rendimento"] * variacao, 1)

            registros.append({
                "data": data,
                "tipo_queijo": tipo,
                "litros_leite": litros_leite,
                "kg_produzido": kg_produzido,
                "preco_kg": info["preco_kg"],
                "turno": rng.choice(["Manha", "Tarde"]),
            })

    df = pd.DataFrame(registros)
    log.info("Gerados %d registros de producao", len(df))
    return df


def salvar_dados(df: pd.DataFrame) -> None:
    """Salva os dados de producao em CSV na pasta data/raw."""
    caminho = DATA_RAW / "producao_queijos.csv"
    df.to_csv(caminho, index=False)
    log.info("Dados salvos em %s", caminho)


if __name__ == "__main__":
    dados = gerar_producao()
    salvar_dados(dados)
