class EscolaNatacaoException(Exception):
    """Exceção base para erros de negócio do sistema da escola de natação."""
    pass


class LimiteToalhasExcedidoException(EscolaNatacaoException):
    """Lançada quando um utilizador tenta retirar mais toalhas do que o permitido."""
    pass


class ToalhaIndisponivelException(EscolaNatacaoException):
    """Lançada quando a toalha solicitada não está disponível para empréstimo."""
    pass


class RecursoNaoEncontradoException(EscolaNatacaoException):
    """Lançada quando um utilizador ou toalha não é encontrado no sistema."""
    pass