# Estrutura de repetição
#laço for
for i in range(5):
    print(f'\nRODADA {i + 1}')
    valor = float(input('Valor da venda: R$ '))
    
    if valor >= 200:
        desconto = valor * 0.10
        valor_final = valor - desconto
        print(f'Valor do desconto: R$ {desconto}')
        print(f'Valor final da compra: R$ {valor_final}')

    else: 
        print(f'Não elegível para receber o desconto. Valor final da compra: R$ {valor}')

