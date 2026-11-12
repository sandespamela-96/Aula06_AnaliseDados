ingresso = float(input('Valor do ingresso: R$ '))

print('''
[1] - Inteira (Sem desconto)
[2] - Meia entrada (50% de desconto)
[3] - Promoção (30% de desconto)
      ''')

opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        desconto = 0
        valor_final = ingresso - desconto
        print('\nInteira (Sem desconto)')
        print(f'Total a pagar: R$ {valor_final}')
    
    case 2:
        desconto = ingresso * 0.50
        valor_final = ingresso - desconto
        print('\nMeia entrada (50% de desconto)')
        print(f'Valor do ingresso: R$ {ingresso}')
        print(f'Desconto: R$ {desconto}')
        print(f'Total a pagar: R$ {valor_final}')    
    
    case 3:
        desconto = ingresso * 0.30
        valor_final = ingresso - desconto
        print('\nPromoção (30% de desconto)')
        print(f'Valor do ingresso: R$ {ingresso}')
        print(f'Desconto: R$ {desconto}')
        print(f'Total a pagar: R$ {valor_final}')

    case _:
        print('Opção Inválida.')