valor = float(input('Valor da venda: R$ '))

# Estrutura Match Case
print('''
[1] - PIX (12% de desconto)
[2] - Débito (8% de desconto)
[3] - Crédito (5% de desconto) 
[4] - Dinheiro (15% de desconto)
''')

operacao = True
desconto = 0
opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        print('---- PIX ----')
        desconto = valor * 0.12
    case 2:
        print('---- Débito ----')
        desconto = valor * 0.08        
    case 3:
        print('---- Crédito ----')
        desconto = valor * 0.05
    case 4:
        print('---- Dinheiro ----')
        desconto = valor * 0.15
    case _:
        operacao = False
        print('Opção Inválida')

#!= : Sinal de diferente

if opcao in [1, 2, 3, 4]:
#if operacao == True:
#if desconto != 0:
    valor_final = valor - desconto
    print(f'Preço: R$ {valor}')
    print(f'Desconto: R$ {desconto}')
    print(f'Total a pagar: R$ {valor_final}')
else:
    print(f'Por favor escolha uma das opções acima.')