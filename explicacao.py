from conhecimento import MAPEAMENTO_FATOS, PLANOS


def explicar_resultado(resultado):
    plano = resultado.get("plano")

    if not plano or plano not in PLANOS:
        return (
            "Não foi possível recomendar um plano com as informações "
            "fornecidas. Tente revisar suas respostas."
        )

    dados_plano = PLANOS[plano]
    regra_recomendacao = resultado.get("regra_recomendacao")
    fatos_iniciais = resultado.get("fatos_iniciais", set())
    regras_ativadas = resultado.get("regras_ativadas", [])

    nomes_fatos = {}

    for campo, opcoes in MAPEAMENTO_FATOS.items():
        for resposta, fato in opcoes.items():
            nomes_fatos[fato] = f"{campo}: {resposta}"

    fatos_explicados = sorted(
        nomes_fatos.get(fato, fato)
        for fato in fatos_iniciais
        if fato != "perfil_completo"
    )

    linhas = [
        f"Recomendação: {dados_plano['nome']}",
        "",
        dados_plano["descricao"],
        "",
        "Fatos considerados:"
    ]

    if fatos_explicados:
        for fato in fatos_explicados:
            linhas.append(f"- {fato}")
    else:
        linhas.append("- Nenhum fato disponível.")

    linhas.extend([
        "",
        "Regras ativadas:"
    ])

    if regras_ativadas:
        for regra in regras_ativadas:
            linhas.append(
                f"- {regra.get('id', 'Regra')}: "
                f"{regra.get('descricao', 'Regra aplicada.')}"
            )
    else:
        linhas.append("- Nenhuma regra foi ativada.")

    if regra_recomendacao:
        linhas.extend([
            "",
            "Regra responsável pela recomendação:",
            f"{regra_recomendacao.get('id', 'Regra')}: "
            f"{regra_recomendacao.get('descricao', '')}"
        ])

    return "\n".join(linhas)