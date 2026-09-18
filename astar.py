from heapq import heappop, heappush
from itertools import count

from estado import ESTADO_INICIAL, eh_objetivo, sucessores
from busca import NoBusca
from heuristica import heuristica


def busca_a_estrela(
    estado_inicial=ESTADO_INICIAL,
    limite_nos=100000
):
    """
    Executa a busca A*.

    A prioridade de cada nó é dada por:

        f(n) = g(n) + h(n)

    onde:
        g(n) = custo acumulado até o nó
        h(n) = estimativa do custo restante

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

    ordem = count()

    # Guarda elementos no formato:
    #
    # (
    #     f(n),
    #     ordem_de_insercao,
    #     g(n),
    #     no
    # )
    #
    # O heap sempre remove o menor f(n).
    fronteira = []

    custo_inicial = 0
    heuristica_inicial = heuristica(estado_inicial)

    heappush(
        fronteira,
        (
            custo_inicial + heuristica_inicial,
            next(ordem),
            custo_inicial,
            raiz,
        )
    )

    # Guarda o menor g(n) conhecido para cada estado.
    melhor_custo = {
        estado_inicial: 0
    }

    nos_expandidos = 0

    while fronteira:

        _, _, custo_atual, no_atual = heappop(
            fronteira
        )

        # Pode haver uma entrada antiga do mesmo estado
        # na fila, com custo maior.
        if custo_atual != melhor_custo.get(
            no_atual.estado
        ):
            continue

        # Como a heurística utilizada é admissível,
        # quando o objetivo é removido da fila,
        # temos uma solução ótima.
        if eh_objetivo(no_atual.estado):
            return no_atual, nos_expandidos

        if nos_expandidos >= limite_nos:
            return None, nos_expandidos

        nos_expandidos += 1

        for acao, novo_estado, custo in sucessores(
            no_atual.estado
        ):

            novo_custo = (
                no_atual.custo_acumulado
                + custo
            )

            custo_conhecido = melhor_custo.get(
                novo_estado,
                float("inf")
            )

            # Se já conhecemos uma forma mais barata
            # ou igual de chegar ao estado, ignoramos.
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

            valor_heuristica = heuristica(
                novo_estado
            )

            prioridade = (
                novo_custo
                + valor_heuristica
            )

            heappush(
                fronteira,
                (
                    prioridade,
                    next(ordem),
                    novo_custo,
                    novo_no,
                )
            )

    return None, nos_expandidos