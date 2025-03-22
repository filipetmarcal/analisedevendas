import pandas as pd

# Lista para armazenar os dados
produtos = []
quantidades = []
precos = []

# Entrada de dados
enquanto = True
while enquanto:
    produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
    if produto.lower() == 'sair':
        break
    quantidade = int(input("Digite a quantidade vendida: "))
    preco = float(input("Digite o preço unitário: "))
    
    produtos.append(produto)
    quantidades.append(quantidade)
    precos.append(preco)

# Criar DataFrame
data = {'Produto': produtos, 'Quantidade': quantidades, 'Preço_Unitario': precos}
df = pd.DataFrame(data)

# Calcular o faturamento total por produto
df['Faturamento'] = df['Quantidade'] * df['Preço_Unitario']

# Estatísticas básicas
faturamento_total = df['Faturamento'].sum()
faturamento_por_produto = df.groupby('Produto')['Faturamento'].sum()
quantidade_por_produto = df.groupby('Produto')['Quantidade'].sum()

# Exibir resultados
print("Faturamento Total:", faturamento_total)
print("\nFaturamento por Produto:")
print(faturamento_por_produto)
print("\nQuantidade Vendida por Produto:")
print(quantidade_por_produto)
