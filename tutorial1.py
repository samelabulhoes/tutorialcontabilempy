# tutorial1.py: Automatizando Relatórios

import pandas as pd

# Carregar dados de exemplo
data = pd.read_csv('../data/example_data.csv')

# Gerar relatório resumido
summary = data.groupby('categoria').agg({'valor': 'sum'}).reset_index()

# Salvar relatório em um arquivo Excel
summary.to_excel('../data/relatorio_resumido.xlsx', index=False)

print("Relatório gerado com sucesso!")

# tutorial2.py: Processamento de Dados Fiscais

import pandas as pd

# Carregar dados fiscais de exemplo
data = pd.read_csv('../data/example_data.csv')

# Filtrar dados por um critério específico (ex: ano fiscal)
filtered_data = data[data['ano'] == 2023]

# Calcular total de impostos
total_impostos = filtered_data['imposto'].sum()

print(f"Total de impostos para o ano fiscal de 2023: R${total_impostos:.2f}")

# tutorial3.py: Análise de Despesas

import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados de despesas de exemplo
data = pd.read_csv('../data/example_data.csv')

# Filtrar despesas por categoria
despesas_por_categoria = data.groupby('categoria')['valor'].sum()

# Plotar gráfico de despesas por categoria
despesas_por_categoria.plot(kind='bar')
plt.title('Despesas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor (R$)')
plt.show()
