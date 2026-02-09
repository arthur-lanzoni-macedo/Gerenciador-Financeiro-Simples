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
                listar_gasto()
            elif escolha == 3:
                mostrar_total()
            elif escolha == 4:
                filtrar_por_categoria()
            elif escolha == 5:
                print("Exportar dados")
            elif escolha == 6:
                sair()
            else:
                print("\n⚠️ Opção inválida! Escolha um número entre 1 e 6. 🚫")
        except ValueError:
            print("❌ ERRO: Por favor, digite apenas NÚMEROS! ❌")

# CASO NÃO TENHA ITEM ADICIONADO
def sem_item_encontrado():
    print("🧐 Valor não identificado. Clique em 'Voltar ao Menu' e tente realizar a operação novamente.")
             
# SAIR DO SISTEMA
def sair():
    os.system("cls")
    print("Sua gestão financeira está em dia. Parabéns pelo compromisso e organização! Até breve. 📈✅")
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
            
            print(f"\n✅ Gasto de R$ {valor:.2f} registrado com sucesso!")    
    except ValueError:
        print("🧐 Não entendi... Certifique-se de digitar um valor válido!")

    voltar_ao_menu()

# LISTAR GASTOS
def listar_gasto():
    titulos("𝑳𝒊𝒔𝒕𝒂𝒓 𝑮𝒂𝒔𝒕𝒐𝒔\n")
    
    if not gastos:
        sem_item_encontrado()
    else:
        for numero, listando in enumerate(gastos, start=1):                
            print(f"{numero:02d} →"
                f"\n💰 Valor: {listando['valor']}"
                f"\n📝 Descrição: {listando['descricao']}"
                f"\n🏷️ Categoria: {listando['categoria']}"
                f"\n{'-'*30}")           
    
    voltar_ao_menu()

# MOSTRAR TOTAL
def mostrar_total():
    titulos("𝑴𝒐𝒔𝒕𝒓𝒂𝒓 𝑻𝒐𝒕𝒂𝒍")
    
    if not gastos:
        sem_item_encontrado()
    else:
        valor_total = 0
        
        for valor in gastos: 
            valor_total += valor['valor']
            
    print(f"Resumo de gastos finalizado! O valor total foi de R$ {valor_total:.2f}. 📝")
    
    voltar_ao_menu()

# FILTRAR POR CATEGORIA
def filtrar_por_categoria():
    titulos("𝑭𝒊𝒍𝒕𝒓𝒂𝒓 𝒑𝒐𝒓 𝑪𝒂𝒕𝒆𝒈𝒐𝒓𝒊𝒂")
    
    if not gastos:
        sem_item_encontrado()
    else:
        categoria = input("Qual categoria você está procurando? ").strip().lower()
        encontrado = False
        
        for gasto in gastos:
            if gasto.get('categoria', '').strip().lower() == categoria:
                encontrado = True
                print(
                    f"\n💰 Valor: {gasto['valor']}"
                    f"\n📝 Descrição: {gasto['descricao']}"
                    f"\n🏷️ Categoria: {gasto['categoria']}"
                    f"\n{'-'*30}"
                )
        if not encontrado:
            sem_item_encontrado()
                
    voltar_ao_menu()

# VISUALIZAR PROJETO
def visualizar_projeto():
    titulo_projeto()
    escolha_opcao()

visualizar_projeto()