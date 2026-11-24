
def ask_choice(question, options):
    print(f"\n{question}")

    for number, option in enumerate(options, start=1):
        print(f"{number} - {option}")

    while True:
        answer = input("Digite sua opção: ").strip()

        if answer.isdigit():
            choice = int(answer)

            if 1 <= choice <= len(options):
                return options[choice - 1]

        print("Opção inválida! Tente novamente.")


def collect_profile():
    print("\n=== PERFIL DO CLIENTE ===")

    goal = ask_choice(
        "Qual é seu principal objetivo?",
        ["Hipertrofia", "Condicionamento físico", "Emagrecimento", "Saúde e bem-estar"]
    )

    frequency = ask_choice(
        "Quantas vezes por semana pretende treinar?",
        ["2 vezes", "3 vezes", "4 vezes", "5 vezes ou mais"]
    )

    experience = ask_choice(
        "Qual é seu nível de experiência?",
        ["Iniciante", "Intermediário", "Avançado"]
    )

    personalized = ask_choice(
        "Deseja acompanhamento personalizado?",
        ["Sim", "Não"]
    )

    period = ask_choice(
        "Qual período prefere treinar?",
        ["Manhã", "Tarde", "Noite"]
    )

    profile = {
        "goal": goal,
        "frequency": frequency,
        "experience": experience,
        "personalized": personalized,
        "period": period
    }

    return profile
