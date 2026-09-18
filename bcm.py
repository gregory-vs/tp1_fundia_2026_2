from heapq import heappop, heappush
from itertools import count

from estado import ESTADO_INICIAL, eh_objetivo, sucessores
from busca import NoBusca


def busca_custo_minimo(
    estado_inicial=ESTADO_INICIAL,
    limite_nos=100000
):
    """
    Executa uma Busca de Custo Uniforme (UCS).

    A fronteira é ordenada pelo custo acumulado g(n).

    Retorna:
        (no_objetivo, nos_expandidos)

    Caso nenhuma solução seja encontrada dentro do limite:
        (None, nos_expandidos)
    """

    raiz = NoBusca(
        estado=estado_inicial,
        pai=None,
        acao=None,
        custo_acumulado=0,
        profundidade=0,
    )

    # Contador usado para desempatar nós com o mesmo custo.
    ordem = count()

    # Cada elemento possui:
    #
    # (custo_acumulado, ordem_de_insercao, no)
    #
    # heapq sempre remove o elemento de menor prioridade.
    fronteira = []

    heappush(
        fronteira,
        (
            raiz.custo_acumulado,
            next(ordem),
            raiz,
        )
    )

    # Guarda o menor custo conhecido para chegar
    # a cada estado.
    melhor_custo = {
        estado_inicial: 0
    }

    nos_expandidos = 0

    while fronteira:

        custo_atual, _, no_atual = heappop(fronteira)

        # Pode existir na fila uma entrada antiga para esse
        # estado, com custo maior que um caminho descoberto
        # posteriormente.
        if custo_atual != melhor_custo.get(no_atual.estado):
            continue

        # Na UCS o teste de objetivo é feito quando o nó
        # é removido da fila de prioridade.
        if eh_objetivo(no_atual.estado):
            return no_atual, nos_expandidos

        if nos_expandidos >= limite_nos:
            return None, nos_expandidos

        nos_expandidos += 1

        for acao, novo_estado, custo in sucessores(
            no_atual.estado
        ):

            novo_custo = (
                no_atual.custo_acumulado + custo
            )

            custo_conhecido = melhor_custo.get(
                novo_estado,
                float("inf")
            )

            # Só interessa esse caminho se ele for
            # mais barato que os já encontrados.
            if novo_custo >= custo_conhecido:
                continue

            melhor_custo[novo_estado] = novo_custo

            novo_no = NoBusca(
                estado=novo_estado,
                pai=no_atual,
                acao=acao,
                custo_acumulado=novo_custo,
                profundidade=no_atual.profundidade + 1,
            )

            heappush(
                fronteira,
                (
                    novo_custo,
                    next(ordem),
                    novo_no,
                )
            )

    return None, nos_expandidos