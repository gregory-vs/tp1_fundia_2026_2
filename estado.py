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


def sucessores(estado):
    """Gera as ações válidas, os estados resultantes e seus custos.

    Cada item retornado possui o formato::

        (acao, novo_estado, custo)

    A ação é uma tupla ``(viajantes, origem, destino)``. ``viajantes`` também
    é uma tupla, contendo uma ou duas pessoas.
    """
    pessoas_no_inicio, lado_tocha = estado

    if not isinstance(pessoas_no_inicio, frozenset):
        raise ValueError("As pessoas no lado inicial devem formar um frozenset.")

    if not pessoas_no_inicio <= PESSOAS:
        raise ValueError("O estado contém uma pessoa desconhecida.")

    if lado_tocha == "inicio":
        pessoas_disponiveis = pessoas_no_inicio
        origem, destino = "inicio", "final"
    elif lado_tocha == "final":
        pessoas_disponiveis = pessoas_no_final(estado)
        origem, destino = "final", "inicio"
    else:
        raise ValueError("O lado da tocha deve ser 'inicio' ou 'final'.")

    resultados = []
    pessoas_ordenadas = sorted(pessoas_disponiveis)

    for quantidade in (1, 2):
        for viajantes in combinations(pessoas_ordenadas, quantidade):
            grupo = frozenset(viajantes)

            if lado_tocha == "inicio":
                novo_inicio = pessoas_no_inicio - grupo
            else:
                novo_inicio = pessoas_no_inicio | grupo

            acao = (viajantes, origem, destino)
            novo_estado = (novo_inicio, destino)
            resultados.append((acao, novo_estado, custo_travessia(viajantes)))

    return resultados
