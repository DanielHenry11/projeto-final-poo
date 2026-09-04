class NadoLivreError(Exception):
    """Exceção base do sistema Nado Livre."""
    pass

class ItemNaoEncontradoError(NadoLivreError):
    """Lançada quando Nadador, Toalha ou Atendente não existem."""
    pass

class ToalhaIndisponivelError(NadoLivreError):
    """Lançada quando tenta-se retirar uma toalha que já está em uso."""
    pass