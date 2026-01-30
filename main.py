import os

gastos = []

# TITULO DO PROJETO
def titulo_projeto():
    print("𝑮𝒆𝒓𝒆𝒏𝒄𝒊𝒂𝒅𝒐 𝑭𝒊𝒏𝒂𝒏𝒄𝒆𝒊𝒓𝒐")
  
# TITULOS
def titulos(texto):
    os.system("cls")
    print(texto)
        
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
                adicionar_gasto()
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
    titulo_projeto()
    menu()

# SCRIPT VOLTAR
def voltar_ao_menu():
    print("\n⌨️  Pressione [Enter] para voltar ao menu... 🔙")
    input()
    voltar()

# ADICIONAR GASTO
def adicionar_gasto():
    titulos("𝑨𝒅𝒊𝒄𝒊𝒐𝒏𝒂𝒓 𝑮𝒂𝒔𝒕𝒐𝒔\n")
    
    try:
        valor = float(input("Digite o valor do gasto (R$): "))
        
        if valor <= 0.0:
            print("\n⚠️ Erro: O valor deve ser maior que zero!")
        else: 
            
            descricao = input("Descrição da despesa: ")
            categoria = input("Categoria (ex: Alimentação, Lazer): ")
            
            gasto = {}
            gasto["valor"] = valor
            gasto["descricao"] = descricao
            gasto["categoria"] = categoria
            
            gastos.append(gasto)
            
            print(gastos)
            print(f"\n✅ Gasto de R$ {valor:.2f} registrado com sucesso!")    
    except ValueError:
        print("🧐 Não entendi... Certifique-se de digitar um valor válido!")

    voltar_ao_menu()
    
# VISUALIZAR PROJETO
def visualizar_projeto():
    titulo_projeto()
    escolha_opcao()

visualizar_projeto()