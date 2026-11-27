
from questionario import collect_profile
from conhecimento import gerar_fatos_iniciais
from inferencia import inferir
from explicacao import explicar_resultado


def main():
    print("=" * 40)
    print("FITADVISOR")
    print("Sistema Especialista para Academias")
    print("=" * 40)

    perfil = collect_profile()

    fatos_iniciais = gerar_fatos_iniciais(perfil)

    resultado = inferir(fatos_iniciais)

    print("\n=== RESULTADO DO SISTEMA ===")
    print(explicar_resultado(resultado))


if __name__ == "__main__":
    main()
