import os

gastos = []

# TITULO DO PROJETO
def titulo_projeto():
    print("𝑮𝒆𝒓𝒆𝒏𝒄𝒊𝒂𝒅𝒐 𝑭𝒊𝒏𝒂𝒏𝒄𝒆𝒊𝒓𝒐")
  
# TITULOS
def titulos(texto):
    os.system("cls")
    print(texto)
    input()
    
# MENU DO PROJETO
def menu():
    print("\n1- Adicionar gasto")
    print("2- Listar gastos")
    print("3- Mostrar total")
    print("4- Filtrar por categoria")
    print("5- Exportar dados")
    print("6- Sair")

# ESCOLHA DE OPÇÕES
def escolha_opcao():
    menu()
    
    while True:
        try:
            escolha = int(input("\nEscolha uma opção: "))
            
            if escolha == 1:
                print("Adicionar gasto")
            elif escolha == 2:
                print("Listar gastos")
            elif escolha == 3:
                print("Mostrar total")
            elif escolha == 4:
                print("Filtrar por categoria")
            elif escolha == 5:
                print("Exportar dados")
            elif escolha == 6:
                sair()
            else:
                print("\n⚠️ Opção inválida! Escolha um número entre 1 e 6. 🚫")
        except ValueError:
            print("❌ ERRO: Por favor, digite apenas NÚMEROS! ❌")
                
# SAIR DO SISTEMA
def sair():
    print("Obrigado por cuidar das suas finanças! Até logo! 👋✨")
    exit()

# VOLTAR AO MENU
def voltar():
    os.system("cls")
    menu()

# VISUALIZAR PROJETO
def visualizar_projeto():
    titulo_projeto()
    escolha_opcao()

visualizar_projeto()