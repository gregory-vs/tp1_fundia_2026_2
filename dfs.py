from estado import ESTADO_INICIAL, eh_objetivo, sucessores
from busca import NoBusca


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


def busca_profundidade(
    estado_inicial=ESTADO_INICIAL,
    limite_nos=100000
):
    """
    Executa uma Busca em Profundidade (DFS).

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

    # DFS utiliza uma pilha (LIFO).
    fronteira = [raiz]

    # Impede que um mesmo estado seja inserido repetidamente
    # na busca, evitando ciclos no grafo.
    visitados = {estado_inicial}

    nos_expandidos = 0

    while fronteira:

        # Retira o último elemento inserido.
        no_atual = fronteira.pop()

        # Verifica se encontramos o objetivo.
        if eh_objetivo(no_atual.estado):
            return no_atual, nos_expandidos

        # Limite de segurança solicitado pelo trabalho.
        if nos_expandidos >= limite_nos:
            return None, nos_expandidos

        nos_expandidos += 1

        # A função sucessores pertence à modelagem do problema.
        #
        # Usamos reversed porque a fronteira é uma pilha.
        # Assim, o primeiro sucessor produzido por sucessores()
        # será também o primeiro explorado pela DFS.
        for acao, novo_estado, custo in reversed(
            sucessores(no_atual.estado)
        ):

            if novo_estado in visitados:
                continue

            visitados.add(novo_estado)

            novo_no = NoBusca(
                estado=novo_estado,
                pai=no_atual,
                acao=acao,
                custo_acumulado=(
                    no_atual.custo_acumulado + custo
                ),
                profundidade=no_atual.profundidade + 1,
            )

            fronteira.append(novo_no)

    # A fronteira acabou sem encontrar solução.
    return None, nos_expandidos