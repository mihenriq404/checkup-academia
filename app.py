
from questionario import collect_profile


def main():
    print("=" * 40)
    print("          FITADVISOR")
    print(" Sistema Especialista para Academias")
    print("=" * 40)

    profile = collect_profile()

    print("\n=== PERFIL REGISTRADO ===")

    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\nInformações coletadas com sucesso!")


if __name__ == "__main__":
    main()
