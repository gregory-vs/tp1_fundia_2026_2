from estado import ESTADO_INICIAL, PESSOAS, pessoas_no_final, sucessores
from dfs import busca_profundidade, reconstruir_caminho


def formatar_pessoas(pessoas):
    """Formata um conjunto de pessoas para exibição."""
    if not pessoas:
        return "ninguém"
    return ", ".join(sorted(pessoas))


def exibir_estado(estado):
    """Exibe as pessoas e a tocha em cada lado da ponte."""
    pessoas_inicio, lado_tocha = estado
    pessoas_final = pessoas_no_final(estado)

    print(f"Lado inicial: {formatar_pessoas(pessoas_inicio)}")
    print(f"Lado final:   {formatar_pessoas(pessoas_final)}")
    print(f"Tocha:        lado {lado_tocha}")


def exibir_solucao(no_objetivo):
    """
    Exibe a sequência de ações encontrada pela busca.
    """

    caminho = reconstruir_caminho(no_objetivo)

    print("\nCaminho encontrado:")

    for numero, no in enumerate(
        caminho[1:],
        start=1
    ):
        viajantes, origem, destino = no.acao

        nomes = " e ".join(viajantes)

        print(
            f"{numero}. "
            f"{nomes}: "
            f"{origem} -> {destino} "
            f"| custo acumulado: "
            f"{no.custo_acumulado} min"
        )

    print(
        f"\nTempo total: "
        f"{no_objetivo.custo_acumulado} minutos"
    )

    print(
        f"Profundidade da solução: "
        f"{no_objetivo.profundidade}"
    )


def main():
    print("Problema da Ponte e da Tocha")
    print("=" * 29)
    print("Tempos: A=1, B=2, C=5, D=10 minutos\n")

    print("Estado inicial:")
    exibir_estado(ESTADO_INICIAL)

    movimentos = sucessores(ESTADO_INICIAL)
    print(f"\nTravessias iniciais possíveis ({len(movimentos)}):")

    for numero, (acao, novo_estado, custo) in enumerate(movimentos, start=1):
        viajantes, origem, destino = acao
        nomes = " e ".join(viajantes)
        restantes, _ = novo_estado
        chegaram = PESSOAS - restantes

        print(
            f"{numero:>2}. {nomes}: {origem} -> {destino} "
            f"| custo: {custo} min "
            f"| início: [{formatar_pessoas(restantes)}] "
            f"| final: [{formatar_pessoas(chegaram)}]"
        )

    print("\nOs algoritmos de busca ainda não foram implementados.")

    no_objetivo, nos_expandidos = (
        busca_profundidade()
    )

    if no_objetivo is None:
        print("\nNenhuma solução encontrada.")
        print(
            f"Nós expandidos: "
            f"{nos_expandidos}"
        )
        return

    exibir_solucao(no_objetivo)

    print(
        f"Nós expandidos: "
        f"{nos_expandidos}"
    )



if __name__ == "__main__":
    main()
