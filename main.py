import pandas as pd
from sqlalchemy import create_engine

# Configuração do banco de dados SQL (altere conforme necessário)
DATABASE_URL = "mysql+pymysql://usuario:senha@localhost/banco"
engine = create_engine(DATABASE_URL)

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

# Enviar dados para o banco de dados
df.to_sql('vendas', con=engine, if_exists='replace', index=False)

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
