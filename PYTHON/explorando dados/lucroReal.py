import pandas as pd 
import matplotlib.pyplot as plt

def calcular_lucro(linha):
    if pd.isna(linha['Motivo']):
        return linha['Venda'] - linha['Custo']
    else:
        return 0
    
vendas = pd.read_excel('Vendas_Anual.xlsx')
devolucoes = pd.read_csv('Devolucoes.csv')

df_final = pd.merge(vendas, devolucoes, on='ID_Vendas', how='left')

print("DADOS COMBINADADOS:")
print(df_final)

df_final['Lucro_Real'] = df_final.apply(calcular_lucro, axis=1)

# Axis para aplicar a função linha por linha
# Axis=1 seria coluna por coluna

faturamento_bruto = df_final['Venda'].sum()

venda_confirmadas = df_final[df_final['Motivo'].isna()]
faturamento_liquido  = venda_confirmadas['Venda'].sum()

