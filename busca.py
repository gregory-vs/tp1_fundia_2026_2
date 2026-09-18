from dataclasses import dataclass

@dataclass
class NoBusca:
    """
    Representa um nó da árvore de busca.

    estado:
        Estado do problema associado ao nó.

    pai:
        Nó que gerou este nó.

    acao:
        Ação executada a partir do pai para chegar neste nó.

    custo_acumulado:
        Soma dos custos das travessias desde o estado inicial.

    profundidade:
        Número de ações realizadas desde o estado inicial.
    """
    estado: tuple
    pai: "NoBusca | None" = None
    acao: tuple | None = None
    custo_acumulado: int = 0
    profundidade: int = 0
