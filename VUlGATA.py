import time
import random
import sys

# MENU
def limpar_tela():
    print("\n" * 50)

def print_delay(texto, velocidade=0.03):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(velocidade)
    print()

def pausar():
    input("\nPressione ENTER para continuar...")

jogador = {
    "nome": "",
    "vida_atual": 1,
    "fé": 5,
    "sabedoria": 0,
    "coragem": 0,
    "carisma": 0,
    "historico": [],
    "memorias": []
}

def salvar_jogo():
    try: 
        with open ("salvamento.txt", "w") as arquivo:
            for chave, valor in jogador.items():
                arquivo.write(f"{chave}={valor}\n")
        print_delay("Jogo salvo com sucesso")
    except:
        print_delay("Erro ao salvar")

def carregar_jogo():
    global jogador
    try:
        with open("salvamento.txt", "r") as arquivo:
            for linha in arquivo:
                if "=" in linha:
                    chave, valor = linha.strip().split("=", 1)
                    if chave in ["fé", "sabedoria", "coragem", "carisma", "vida_atual"]:
                        jogador[chave] = int(valor)
                    else:
                        jogador[chave] = valor
        print_delay("Jogo carregando")
        return True 
    except FileNotFoundError:
        return False
    except:
        print_delay("Erro ao carregar salvamento")
        return False 

def tela_boas_vindas():
    limpar_tela()
    print("=" * 50)
    print("""
    ██╗   ██╗██╗   ██╗██╗      ██████╗  █████╗ ████████╗ █████╗ 
    ██║   ██║██║   ██║██║     ██╔════╝ ██╔══██╗╚══██╔══╝██╔══██╗
    ██║   ██║██║   ██║██║     ██║  ███╗███████║   ██║   ███████║
    ╚██╗ ██╔╝██║   ██║██║     ██║   ██║██╔══██║   ██║   ██╔══██║
     ╚████╔╝ ╚██████╔╝███████╗╚██████╔╝██║  ██║   ██║   ██║  ██║
      ╚═══╝   ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
    """)
    print("=" * 50)
    print("                    VULGATA")
    print("    Uma jornada pela mitologia cristã")
    print("=" * 50)
    print()

def menu_principal():
    while True:
        print("\n===MENU PRINCIPAL===")
        print("1. Novo jogo")
        print("2. Carregar jogo")
        print("3. Sobre")
        print("4. Sair")

        opcao_menu = input("\nEscolha uma opção (1-4)")

        if opcao_menu == "1":
            novo_jogo()
            break
        elif opcao_menu == "2":
            if carregar_jogo():
                continuar_jogo()
                break
            else:
                print_delay("Nenhum salvamento encontrado")
                pausar()
        elif opcao_menu == "3":
            tela_sobre()
        elif opcao_menu == "4":
            print_delay("Até logo...")
            sys.exit()
        else:
            print_delay("Opção inválida")
            pausar()

def novo_jogo():
    limpar_tela()
    print_delay("Boas-vindas")
    time.sleep(1)

    nome = input("\nComo deseja ser chamado? ")
    jogador["nome"] = nome
    jogador["vida_atual"] = 1
    jogador["fé"] = 5
    jogador["sabedoria"] = 0
    jogador["carisma"] = 0
    jogador["historico"] = []
    jogador["memorias"] = []

    print_delay(f"Que a jornada comece, {nome}")
    pausar()
    vida_1_adao()

def continuar_jogo():
    print_delay(f"Bem-vindo de volta, {jogador['nome']}")
    print_delay(f"Você está na vida {jogador['vida_atual']}")
    pausar()
    vida_1_adao()

def tela_sobre():
    limpar_tela()
    print("Manutenção")
    pausar()

def mostrar_status():
    print("\n" + "-" * 30)
    print(f"Jogador: {jogador['nome']}")
    print(f"Vida: {jogador['vida_atual']}")
    print(f"Fé: {jogador['fé']} | Sabedoria: {jogador['sabedoria']}")
    print(f"Coragem: {jogador['coragem']} | Carisma: {jogador['carisma']}")
    print("-" * 30)

#ADAO - 1
def vida_1_adao():
    limpar_tela()
    print_delay("== VIDA 1 - ADÃO, O PRIMEIRO JARDINEIRO ==")
    time.sleep(1)
    print_delay("\nVocê acorda no Jardim do Éden. A luz é suave e aquece sua pele, que reluz nos sol. O ar é profundo e puro. Você escuta muitos sons, vê muitas cores e sente muuitas texturas.")
    print_delay("Uma voz ecoa do além: Plante, regue, colha e alimente plantas e criaturas do jardim")

    plantas = []
    animais = {
        "ovelha": {"alimentado": False},
        "galinha": {"alimentado": False}
    }
    
    colheitas = 0
    produtos_animais = 0

    while colheitas < 6 or produtos_animais < 6:

        
        mostrar_status()

        print("\n=== JARDIM DO ÉDEN ===")
        print("1. Plantar")
        print("2. Regar plantas")
        print("3. Colher plantas")
        print("4. Alimentar animais")
        print("5. Coletar produtos dos animais")
        print("6. Ver fazenda")
        print("7. Salvar jogo")

        escolha = input("\nEscolha: ")
    
        if escolha == "1":
            planta=random.choice(["trigo", "morango", "feijão", "maracujá", "batata", "cenoura"])
            plantas.append({"tipo": planta, "regado": False})

            print(f"Você plantou {planta}")
            jogador["sabedoria"]+=1
            print("+ 1 Sabedoria")
            pausar()

        elif escolha == "2":
            if not plantas:
                print("\nNão há plantas para regar")
            else:
                for p in plantas:
                    p["regado"] = True
                print("\nVocê regou todas as plantas")
            pausar()

        elif escolha == "3":
            prontas = [p for p in plantas if p["regado"]]

            if prontas:
                planta = prontas.pop()
                plantas.remove(planta)

                print(f"\nVocê colheu {planta['tipo']}")
                colheitas +=1
                jogador["fé"] +=1
                print("+1 Fé")
            else:
                print("\nNenhuma planta está pronta para colher")
            pausar()

        elif escolha == "4":
            animal=random.choice(["ovelha", "galinha", "vaca", "porco"])
            for animal in animais:
                animais[animal]["alimentado"] = True

            print("\nVocê alimentou os animais.")
            jogador["carisma"] += 1
            print("+1 Carisma")
            pausar()

        elif escolha == "5":
            coletado = False

            for animal in animais:
                if animais[animal]["alimentado"]:
                    print(f"\nVocê coletou um produto de {animal}")
                    produtos_animais += 1
                    animais[animal]["alimentado"] = False
                    coletado = True

            if not coletado:
                print("\nOs animais precisam ser alimentados primeiro")
            else:
                jogador["coragem"] += 1
                print("+ 1 Coragem")

            pausar()

        elif escolha == "6":
            print("\n=== SUA FAZENDA ===")

            print("\nPlantas plantadas:", len(plantas))

            print("\nAnimais:")
            for animal in animais:
                estado = "alimentado" if animais[animal]["alimentado"] else "com fome"
                print(f"- {animal}: {estado}")

            print("\nColheitas feitas:", colheitas)
            print("Produtos coletados:", produtos_animais)

            pausar()

        elif escolha == "7":
            salvar_jogo()
            pausar()

    limpar_tela()
    print_delay("\nEnquanto você trabalha no jardim, algo se move entre as árvores...")
    print_delay("Uma serpente aparece com um fruto brilhante.")
    time.sleep(1)
    print_delay("'Coma', ela diz. 'E terá conhecimento.'")

    print("\nO que você faz?")
    print("1. Recusar")
    print("2. Comer o fruto")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        print_delay("\nVocê tenta resistir...")
        print_delay("Se passam algumas semanas e você percebe que a serpente havia pego toda a comida.")
        print_delay("Então, a serpente aparece novamente, e como quem sabe o que irá acontecer, lhe oferece o fruto novamente. Desta vez, você aceita.")
    else:
        print_delay("\nVocê prova o fruto proibido. Ele é doce e suculento, algo que você jamais esquecerá.")

    print_delay("\nO conhecimento invade sua mente.")
    jogador["sabedoria"] += 3
    print("+3 Sabedoria")

    jogador["vida_atual"] = 2
    jogador["historico"].append("Adão")

    salvar_jogo()
    pausar()

    limpar_tela()
    print_delay("Fim da Vida 1: Adão")
    print_delay("Novas vidas virão em breve...")
    pausar()

    pausar()
    menu_principal()







if __name__ == "__main__":
    tela_boas_vindas()
    time.sleep(2)
    menu_principal()
