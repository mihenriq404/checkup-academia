from conhecimento import REGRAS


def inferir(fatos_iniciais):
    if not isinstance(fatos_iniciais, (set, list, tuple)):
        raise TypeError(
            "Os fatos iniciais devem ser um conjunto ou uma lista."
        )

    fatos = set(fatos_iniciais)
    fatos_originais = set(fatos_iniciais)
    regras_ativadas = []
    ids_ativados = set()

    regras_ordenadas = sorted(
        REGRAS,
        key=lambda regra: regra.get("prioridade", 0),
        reverse=True
    )

    houve_mudanca = True

    while houve_mudanca:
        houve_mudanca = False

        for indice, regra in enumerate(regras_ordenadas, start=1):
            identificador = regra.get("id", f"R{indice}")
            condicoes = set(regra.get("condicoes", set()))
            conclusao = regra.get("conclusao")

            if not condicoes:
                continue

            if (
                condicoes.issubset(fatos)
                and identificador not in ids_ativados
            ):
                regras_ativadas.append(regra)
                ids_ativados.add(identificador)

                if conclusao and conclusao not in fatos:
                    fatos.add(conclusao)
                    houve_mudanca = True

    regras_de_recomendacao = [
        regra
        for regra in regrasativadas
        if str(regra.get("conclusao", "")).startswith("plano")
    ]

    regra_recomendacao = None
    plano_recomendado = None

    if regras_de_recomendacao:
        regra_recomendacao = max(
            regras_de_recomendacao,
            key=lambda regra: regra.get("prioridade", 0)
        )
        plano_recomendado = regra_recomendacao["conclusao"]

    return {
        "plano": plano_recomendado,
        "fatos_iniciais": fatos_originais,
        "fatos": fatos,
        "regras_ativadas": regras_ativadas,
        "regra_recomendacao": regra_recomendacao
    }