from collections import deque

from estado import ESTADO_INICIAL, eh_objetivo, sucessores
from busca import NoBusca


def busca_largura(
    estado_inicial=ESTADO_INICIAL,
    limite_nos=100000
):
    """
    Executa uma Busca em Largura (BFS).

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

    # BFS utiliza uma fila (FIFO).
    fronteira = deque([raiz])

    # Estados que já foram descobertos.
    # Evita ciclos e inserções repetidas na fronteira.
    visitados = {estado_inicial}

    nos_expandidos = 0

    while fronteira:

        # Remove o primeiro elemento inserido na fila.
        no_atual = fronteira.popleft()

        # Verifica se o estado atual é o objetivo.
        if eh_objetivo(no_atual.estado):
            return no_atual, nos_expandidos

        # Limite de segurança.
        if nos_expandidos >= limite_nos:
            return None, nos_expandidos

        nos_expandidos += 1

        # Na BFS não usamos reversed().
        # Os sucessores entram na fila na mesma ordem
        # em que são produzidos.
        for acao, novo_estado, custo in sucessores(
            no_atual.estado
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

    # A fronteira ficou vazia sem encontrar uma solução.
    return None, nos_expandidos