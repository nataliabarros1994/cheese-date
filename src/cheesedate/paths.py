"""Caminhos do projeto. Centralizar aqui evita strings de caminho espalhadas."""
from pathlib import Path

# ROOT = a pasta raiz do projeto (sobe 3 niveis a partir deste arquivo)
ROOT = Path(__file__).resolve().parents[2]

DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_OUTPUT = ROOT / "data" / "output"
REPORTS = ROOT / "reports"

# Cria as pastas se nao existirem
for _pasta in (DATA_RAW, DATA_PROCESSED, DATA_OUTPUT, REPORTS):
    _pasta.mkdir(parents=True, exist_ok=True)
