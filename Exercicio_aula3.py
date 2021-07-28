print ('Ficha do exército\n')
print ('AVISO, para numeros quebrados deve-se inserir ponto no lugar da virgula\n')

idade = int(input ('Escreva sua idade: '))
peso = float(input ('Escreva seu Peso: '))
altura = float(input ('Escreva sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print ('Você está apto a entrar no Exército')
else:
    print ('Você não está apto a entrar no exército')