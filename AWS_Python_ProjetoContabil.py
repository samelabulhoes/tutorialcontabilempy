
### tutorials/tutorial_aws_s3.py

```python
# tutorial_aws_s3.py: Integração com AWS S3

import boto3
import pandas as pd

# Configurar o cliente S3
s3 = boto3.client('s3')

# Nome do bucket S3 e arquivo a ser carregado
bucket_name = 'meu-bucket'
file_name = 'data/example_data.csv'

# Carregar dados de exemplo localmente
data = pd.read_csv(f'../{file_name}')

# Gerar relatório resumido
summary = data.groupby('categoria').agg({'valor': 'sum'}).reset_index()

# Salvar relatório em um arquivo CSV
summary_file_name = 'data/relatorio_resumido.csv'
summary.to_csv(summary_file_name, index=False)

# Fazer upload do arquivo CSV para o S3
s3.upload_file(summary_file_name, bucket_name, summary_file_name)

print(f"Relatório carregado com sucesso para o bucket {bucket_name}!")

# Introdução ao Python na Contabilidade

Este tutorial introdutório explica os benefícios de usar Python na contabilidade e oferece uma visão geral dos tópicos que serão cobertos nos tutoriais subsequentes.

## Benefícios do Python

# - Automação de tarefas repetitivas
# - Processamento de grandes volumes de dados
# - Análise avançada de dados
# - Criação de relatórios personalizados
# - Integração com serviços na nuvem como AWS

## Tópicos Cobertos

- Automatizando Relatórios
- Processamento de Dados Fiscais
- Análise de Despesas
- Integração com AWS S3

boto3
pandas
matplotlib

