from estado import TEMPOS, pessoas_no_final


def heuristica(estado):
    """
    Estima o custo mínimo restante para alcançar o objetivo.

    A heurística considera:

    1. Se todas as pessoas já atravessaram:
       h(n) = 0

    2. Se a tocha está no lado inicial:
       a pessoa mais lenta que ainda está no início
       obrigatoriamente terá que atravessar.

       h(n) = maior tempo entre as pessoas no início

    3. Se a tocha está no lado final:
       alguém precisa obrigatoriamente trazer a tocha de volta
       antes que as pessoas restantes possam atravessar.

       Consideramos, de forma otimista, que a pessoa mais rápida
       do lado final fará esse retorno.

       h(n) =
           menor tempo no lado final
           +
           maior tempo no lado inicial
    """

    pessoas_no_inicio, lado_tocha = estado

    # Estado objetivo.
    if not pessoas_no_inicio:
        return 0

    maior_tempo_inicio = max(
        TEMPOS[pessoa]
        for pessoa in pessoas_no_inicio
    )

    if lado_tocha == "inicio":
        return maior_tempo_inicio

    if lado_tocha == "final":

        pessoas_final = pessoas_no_final(estado)

        # Este caso representa uma configuração inválida:
        # a tocha não poderia estar no lado final sem que
        # nenhuma pessoa estivesse lá.
        if not pessoas_final:
            raise ValueError(
                "Estado inválido: a tocha está no lado final "
                "sem nenhuma pessoa no lado final."
            )

        menor_tempo_final = min(
            TEMPOS[pessoa]
            for pessoa in pessoas_final
        )

        return (
            menor_tempo_final
            + maior_tempo_inicio
        )

    raise ValueError(
        "O lado da tocha deve ser 'inicio' ou 'final'."
    )