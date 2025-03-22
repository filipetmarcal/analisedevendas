# Analisador de Vendas com Pandas e SQL

Este é um programa simples em Python que utiliza a biblioteca **Pandas** e um banco de dados **SQL** para armazenar, processar e analisar dados de vendas inseridos pelo usuário. Ele calcula o faturamento total e exibe estatísticas detalhadas por produto.

## 📌 Funcionalidades
- Permite a entrada manual de produtos, quantidades e preços.
- Armazena os dados em um banco de dados SQL (compatível com MySQL, PostgreSQL, etc.).
- Calcula o faturamento total e por produto.
- Exibe estatísticas sobre as vendas.

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as bibliotecas necessárias caso ainda não tenha:
   ```sh
   pip install pandas sqlalchemy pymysql psycopg2
   ```
3. Configure a conexão com o banco de dados SQL no arquivo `config.py`.
4. Execute o script Python:
   ```sh
   python analise_vendas.py
   ```
5. Insira os produtos vendidos e finalize digitando **'sair'**.

## 📊 Exemplo de Uso
```
Digite o nome do produto (ou 'sair' para finalizar): A
Digite a quantidade vendida: 10
Digite o preço unitário: 20
Digite o nome do produto (ou 'sair' para finalizar): B
Digite a quantidade vendida: 5
Digite o preço unitário: 30
Digite o nome do produto (ou 'sair' para finalizar): sair

Faturamento Total: 350

Faturamento por Produto:
Produto
A    200
B    150
Name: Faturamento, dtype: int64

Quantidade Vendida por Produto:
Produto
A    10
B     5
Name: Quantidade, dtype: int64
```

## 🛠 Tecnologias Utilizadas
- **Python**
- **Pandas**
- **SQLAlchemy** (para conexão com bancos SQL como MySQL, PostgreSQL, etc.)

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para modificá-lo e usá-lo como quiser.

---

✨ Desenvolvido por Filipe Marçal 🚀

