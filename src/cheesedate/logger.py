"""Logger configurado para o projeto."""
import logging


def get_logger(nome: str) -> logging.Logger:
    """Retorna um logger formatado e pronto para uso."""
    logger = logging.getLogger(nome)

    # Evita adicionar handlers duplicados se chamado varias vezes
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
