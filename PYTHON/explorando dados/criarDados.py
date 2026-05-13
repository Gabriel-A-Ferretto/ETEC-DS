import pandas as pd
import sqlite3 
import numpy as np

df_vendas = pd.DataFrame({
    'ID_Vendas': [101, 102, 103, 104, 105, 106],
    'Produto': ['Teclado', 'Monitor', 'Mause', 'Notebook', 'Cadeira', 'Mesa'],
    'Vendas': [150.0, 1200.0, 80.0, 4500.0, 900.0, 1200.0],
    'Custo': [60.0, 800.0, 30.0, 3200.0, 500.0, 800.0]
})

df_vendas.to_excel('Vendas_Anual.xlsx', index=False)

df_dev = pd.DataFrame({
    'ID_Vendas': [102, 105],
    'Motivo':['Defeito', 'Arrependimento']
})
df_dev.to_csv('Devolucoes.csv', index=False)

conn = sqlite3.connect('sistema.db')
df_acessos = pd.DataFrame({
    'usuario': ['admin', 'aluno1', 'prof_jose', 'aluno2', 
                'suporte'],
    'Data_Acesso': ['2026-04-10 09:00', '2026-05-01 22:30',
                    '2026-05-05 10:15',
                    '2026-05-06 02:00', '2026-05-06 14:00']

})
df_acessos.to_sql('tb_acesso', conn, index=False, if_exists='replace')
conn.close()

df_notas = pd.DataFrame({
    'Cursso': ['Sistemas', 'Informatica', 'Sistemas', 'Informatica', 'Sistemas'],
    'Cidade': ['São Paulo', 'Santos', 'São Paulo', 'Campinas', 'Santos'],
    'Nota': [85, 70, 92, 65, 88]
})
df_notas.to_csv('Notas_Alunos.csv', index=False)

df_inv = pd.DataFrame({
    'Item': ['Servidor', 'Switch', 'Roteador', 'Nobreak'],
    'Data_Aquisicao' : ['2018-05-20', '2002-01-19', '2015-11-30', np.nan],
    'Cursto_Manutencao' : [1500, 200, 800, 400],
    'Marca' : ['Dell', np.nan, 'Cisco', 'APC']
})
df_inv.to_excel('Inventario.xlsx', index=False)

print("ARQUIVOS CRIADOS COM SUCESSO!")

