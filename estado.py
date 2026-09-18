from itertools import combinations


PESSOAS = frozenset({"A", "B", "C", "D"})

TEMPOS = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 10,
}

ESTADO_INICIAL = (PESSOAS, "inicio")
ESTADO_OBJETIVO = (frozenset(), "final")


def eh_objetivo(estado):
    """Retorna True quando todas as pessoas chegaram ao lado final."""
    return estado == ESTADO_OBJETIVO


def pessoas_no_final(estado):
    """Retorna as pessoas que já atravessaram para o lado final."""
    pessoas_no_inicio, _ = estado
    return PESSOAS - pessoas_no_inicio


def custo_travessia(pessoas):
    """Calcula o custo de uma travessia de uma ou duas pessoas."""
    if not 1 <= len(pessoas) <= 2:
        raise ValueError("Uma travessia deve conter uma ou duas pessoas.")

    if not set(pessoas) <= PESSOAS:
        raise ValueError("A travessia contém uma pessoa desconhecida.")

    if len(set(pessoas)) != len(pessoas):
        raise ValueError("Uma pessoa não pode aparecer duas vezes na travessia.")

    return max(TEMPOS[pessoa] for pessoa in pessoas)

def pessoas_disponiveis(estado):
    """
    Retorna as pessoas que estão no mesmo lado da tocha
    e, portanto, podem participar da próxima travessia.
    """
    pessoas_no_inicio, lado_tocha = estado

    if lado_tocha == "inicio":
        return pessoas_no_inicio

    if lado_tocha == "final":
        return pessoas_no_final(estado)

    raise ValueError("O lado da tocha deve ser 'inicio' ou 'final'.")


def acoes_validas(estado):
    """
    Gera todas as ações que podem ser executadas a partir
    do estado informado.

    Uma ação possui o formato:

        (viajantes, origem, destino)

    onde viajantes contém uma ou duas pessoas.
    """
    _, lado_tocha = estado

    disponiveis = sorted(pessoas_disponiveis(estado))

    if lado_tocha == "inicio":
        origem = "inicio"
        destino = "final"
    else:
        origem = "final"
        destino = "inicio"

    acoes = []

    for quantidade in (1, 2):
        for viajantes in combinations(disponiveis, quantidade):
            acao = (viajantes, origem, destino)
            acoes.append(acao)

    return acoes


def aplicar_acao(estado, acao):
    """
    Aplica uma ação válida a um estado e retorna
    o estado resultante.

    Esta função representa a função de transição.
    """
    pessoas_no_inicio, lado_tocha = estado
    viajantes, origem, destino = acao

    # A tocha precisa estar na origem da ação.
    if lado_tocha != origem:
        raise ValueError(
            "A ação deve partir do lado em que está a tocha."
        )

    # Precisamos de uma ou duas pessoas.
    if not 1 <= len(viajantes) <= 2:
        raise ValueError(
            "Uma travessia deve conter uma ou duas pessoas."
        )

    grupo = frozenset(viajantes)

    if len(grupo) != len(viajantes):
        raise ValueError(
            "Uma mesma pessoa não pode aparecer duas vezes."
        )

    # Verifica se os viajantes estão realmente disponíveis.
    disponiveis = pessoas_disponiveis(estado)

    if not grupo <= disponiveis:
        raise ValueError(
            "Todos os viajantes devem estar no mesmo lado da tocha."
        )

    if origem == "inicio":
        novo_inicio = pessoas_no_inicio - grupo
    else:
        novo_inicio = pessoas_no_inicio | grupo

    return (novo_inicio, destino)



def sucessores(estado):
    """
    Gera todos os sucessores de um estado.

    Cada sucessor possui o formato:

        (acao, novo_estado, custo)
    """
    resultados = []

    for acao in acoes_validas(estado):
        novo_estado = aplicar_acao(estado, acao)

        viajantes, _, _ = acao
        custo = custo_travessia(viajantes)

        resultados.append(
            (acao, novo_estado, custo)
        )

    return resultados