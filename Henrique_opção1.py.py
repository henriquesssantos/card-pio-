cardapio = ['Água', 5, 'Refrigerante', 10, 'Feijoada', 30, 'Parmegiana', 35, 'Stroganoff', 25]
# Lista vazia para armazenar os itens do pedido
pedido = []
sequencia = 1


# ===== MENU PRINCIPAL =====
# Laço while para manter o menu aberto
while True:
    print("\n" + "="*40)
    print("         MENU PRINCIPAL  ")
    print("="*40)
    print("1 - Exibir Cardápio")
    print("2 - Adicionar Item ao Pedido")
    print("3 - Remover Item do Pedido")
    print("4 - Listar Meu Pedido")
    print("5 - Finalizar Compra (Calcular Total)")
    print("6 - Sair")
    print("="*40)
        
    opcao = input("Escolha uma opção (1-6): ")

# ===== BLOCO PARA EXIBIR O CARDÁPIO =====
        
    if opcao == "1":
        print("="*40)
        print(" "*16 + "CARDÁPIO" + " "*16)
        print("="*40)


        # Laço for para passar de 2 em 2 (nome e preço)
        for i in range(0, len(cardapio), 2):
            nome = cardapio[i]
            preco = cardapio[i + 1]
            print(f"{sequencia} - {nome:.<20} R${preco}")
            
            ''' .<20 é para fazer um "preenchimento, significa que a variavel inserida precisa ter 20 caracteres, 
            no total, descontando o numero de caracteres já presente na variavel, a seta "<" indica o sentido do preenchimento'''
            sequencia += 1
            
        print("="*40 + "\n")

 # ===== BLOCO PARA ADICIONAR ITEM AO PEDIDO =====
 
    elif opcao == "2":
        escolha = int(input("Digite o número do item desejado: "))

        # Pega o nome e preço do item escolhido
        indice_real = (escolha - 1) * 2

        nome = cardapio[indice_real]
        preco = cardapio[indice_real + 1]

        '''cada item completo (nome + preço) tem dois espaços na lista, por eu ter escolhido uma lista plana,
        precisa multiplicar por 2 para pular os itens de dois em dois e cair sempre no índice 
        onde o nome daquele prato começa.'''

        # Adiciona à lista de pedido
        pedido.append([nome, preco])
        print("="*40 + "\n")

# ===== BLOCO PARA REMOVER ITEM DO PEDIDO =====

    elif opcao == "3":
        print("\n--- ITENS NO PEDIDO ---")
            
        # Exibe os itens numerados
        for i in range(len(pedido)):
            print(f"{i+1} - {pedido[i][0]} (R${pedido[i][1]})")

        '''
        O pedido[i] vai lá na linha exata (ex: pega a mini-lista (matriz criada por causa do pedido) ['Feijoada', 30]).
        Depois, o [0] pega o primeiro item dessa mini-lista, que é o nome (Feijoada).

        {pedido[i][1]}: Faz a mesma coisa, mas o [1] pega o segundo item da mini-lista, que é o preço (30).
        '''
        escolha = int(input("\nDigite o número do item a remover: "))
        item_removido = pedido.pop(escolha - 1)  # Remove e guarda o item
        print(f"✅ {item_removido[0]} removido do pedido!")

# ==== BLOCO PARA EXIBIR LISTA DE PEDIDOS ==== 

    elif opcao == "4":
        print("\n" + "="*40)
        print("         ITENS DO PEDIDO  ")
        print("="*40)
        
        # Laço para exibir cada item
        for i in range(len(pedido)):
            nome = pedido[i][0]
            preco = pedido[i][1]
            print(f"{i + 1}. {nome:.<25} R${preco}")
            
        print("="*40 + "\n")

# ===== BLOCO PARA CALCULAR E EXIBIR O TOTAL =====

    elif opcao == "5":
        # Laço para somar todos os preços
        total = 0
        for item in pedido:
                total += item[1]
            
        print(f"💰 TOTAL A PAGAR: R${total}")
        print("="*40 + "\n")
        
    elif opcao == "6":
            print("\n👋 Obrigado por usar nosso sistema! Até logo!\n")
            break  # Sai do laço while
        
    else:
        print("❌ Opção inválida! Digite de 1 a 6.")
