
MAPEAMENTO_FATOS = {
    "goal": {
        "Hipertrofia": "objetivo_hipertrofia",
        "Condicionamento físico": "objetivo_condicionamento",
        "Emagrecimento": "objetivo_emagrecimento",
        "Saúde e bem-estar": "objetivo_saude"
    },
    "frequency": {
        "2 vezes": "frequencia_2",
        "3 vezes": "frequencia_3",
        "4 vezes": "frequencia_4",
        "5 vezes ou mais": "frequencia_5_mais"
    },
    "experience": {
        "Iniciante": "experiencia_iniciante",
        "Intermediário": "experiencia_intermediaria",
        "Avançado": "experiencia_avancada"
    },
    "personalized": {
        "Sim": "deseja_acompanhamento",
        "Não": "nao_deseja_acompanhamento"
    },
    "period": {
        "Manhã": "periodo_manha",
        "Tarde": "periodo_tarde",
        "Noite": "periodo_noite"
    }
}


PLANOS = {
    "plano_basico": {
        "nome": "Plano Básico",
        "descricao": "Acesso à academia e estrutura convencional de treinamento."
    },
    "plano_intermediario": {
        "nome": "Plano Intermediário",
        "descricao": "Acesso à academia com benefícios adicionais para apoiar a organização da rotina de treinos."
    },
    "plano_premium": {
        "nome": "Plano Premium",
        "descricao": "Acesso à academia com acompanhamento personalizado."
    }
}


REGRAS = [
    {
        "id": "R01",
        "descricao": "Cliente que deseja acompanhamento personalizado e busca hipertrofia.",
        "condicoes": {"perfil_completo", "objetivo_hipertrofia", "deseja_acompanhamento"},
        "conclusao": "plano_premium",
        "prioridade": 100
    },
    {
        "id": "R02",
        "descricao": "Cliente que deseja acompanhamento personalizado e busca condicionamento físico.",
        "condicoes": {"perfil_completo", "objetivo_condicionamento", "deseja_acompanhamento"},
        "conclusao": "plano_premium",
        "prioridade": 100
    },
    {
        "id": "R03",
        "descricao": "Cliente que deseja acompanhamento personalizado e busca emagrecimento.",
        "condicoes": {"perfil_completo", "objetivo_emagrecimento", "deseja_acompanhamento"},
        "conclusao": "plano_premium",
        "prioridade": 100
    },
    {
        "id": "R04",
        "descricao": "Cliente que deseja acompanhamento personalizado e busca saúde e bem-estar.",
        "condicoes": {"perfil_completo", "objetivo_saude", "deseja_acompanhamento"},
        "conclusao": "plano_premium",
        "prioridade": 100
    },
    {
        "id": "R05",
        "descricao": "Cliente com foco em hipertrofia que pretende treinar quatro vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_hipertrofia", "frequencia_4", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R06",
        "descricao": "Cliente com foco em hipertrofia que pretende treinar cinco vezes ou mais por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_hipertrofia", "frequencia_5_mais", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R07",
        "descricao": "Cliente com foco em condicionamento físico que pretende treinar quatro vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_condicionamento", "frequencia_4", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R08",
        "descricao": "Cliente com foco em condicionamento físico que pretende treinar cinco vezes ou mais por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_condicionamento", "frequencia_5_mais", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R09",
        "descricao": "Cliente com foco em emagrecimento que pretende treinar quatro vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_emagrecimento", "frequencia_4", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R10",
        "descricao": "Cliente com foco em emagrecimento que pretende treinar cinco vezes ou mais por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_emagrecimento", "frequencia_5_mais", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R11",
        "descricao": "Cliente com foco em saúde e bem-estar que pretende treinar quatro vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_saude", "frequencia_4", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R12",
        "descricao": "Cliente com foco em saúde e bem-estar que pretende treinar cinco vezes ou mais por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_saude", "frequencia_5_mais", "nao_deseja_acompanhamento"},
        "conclusao": "plano_intermediario",
        "prioridade": 70
    },
    {
        "id": "R13",
        "descricao": "Cliente com foco em hipertrofia que pretende treinar duas vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_hipertrofia", "frequencia_2", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R14",
        "descricao": "Cliente com foco em hipertrofia que pretende treinar três vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_hipertrofia", "frequencia_3", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R15",
        "descricao": "Cliente com foco em condicionamento físico que pretende treinar duas vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_condicionamento", "frequencia_2", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R16",
        "descricao": "Cliente com foco em condicionamento físico que pretende treinar três vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_condicionamento", "frequencia_3", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R17",
        "descricao": "Cliente com foco em emagrecimento que pretende treinar duas vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_emagrecimento", "frequencia_2", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R18",
        "descricao": "Cliente com foco em emagrecimento que pretende treinar três vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_emagrecimento", "frequencia_3", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R19",
        "descricao": "Cliente com foco em saúde e bem-estar que pretende treinar duas vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_saude", "frequencia_2", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    },
    {
        "id": "R20",
        "descricao": "Cliente com foco em saúde e bem-estar que pretende treinar três vezes por semana e não deseja acompanhamento personalizado.",
        "condicoes": {"perfil_completo", "objetivo_saude", "frequencia_3", "nao_deseja_acompanhamento"},
        "conclusao": "plano_basico",
        "prioridade": 50
    }
]


def gerar_fatos_iniciais(perfil):
    fatos = {"perfil_completo"}

    for campo, mapeamento in MAPEAMENTO_FATOS.items():
        resposta = perfil.get(campo)

        if resposta not in mapeamento:
            raise ValueError(
                f"Resposta inválida ou ausente para o campo: {campo}"
            )

        fatos.add(mapeamento[resposta])

    return fatos