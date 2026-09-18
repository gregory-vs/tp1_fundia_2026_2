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

def reconstruir_caminho(no_objetivo):
    """
    Reconstrói o caminho entre o estado inicial e o estado objetivo.

    Retorna uma lista de nós, começando pela raiz e terminando
    no nó objetivo.
    """
    caminho = []
    no_atual = no_objetivo

    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = no_atual.pai

    caminho.reverse()

    return caminho
