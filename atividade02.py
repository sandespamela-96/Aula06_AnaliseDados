# numero = float(input('Insira um número: '))

# dobro = numero * 2
# triplo = numero * 3
# quadrado = numero * numero
# ##quadruplo = numero * numero ou numero ** 2 (** significa potencia)

# print(f'\nO dobro de {numero} é {dobro}')
# print(f'O triplo de {numero} é {triplo}')
# print(f'O quadruplo de {numero} é {quadrado}')

# Estrutura de repetição
#laço for
for i in range(3):
    print(f'\nRODADA {i + 1}')
    num = float(input('Número: '))
    
    dobro = num * 2
    triplo = num * 3
    quadrado = num ** 2

    print(f'\nO dobro de {num} é {dobro}')
    print(f'O triplo de {num} é {triplo}')
    print(f'O quadrado de {num} é {quadrado}')