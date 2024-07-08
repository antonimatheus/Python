print('Adicione preço do produto e a % do desconto!')

preco = float(input('Digite o preço: '))
desconto = float(input('Digite o desconto: '))

precoDesconto = (desconto / 100) * preco
novoPreco = preco - desconto

print(f'Produto com o preço de R${preco:.2f} e {desconto:.0f}% de desconto, o preço atual será de R${novoPreco:.2f}')
