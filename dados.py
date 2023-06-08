import os  
import pandas as pd

lista_arquivo = os.listdir("C:\Users\Jean Lucas\Downloads\Vendas")  #importa os arquivos
tabela_total = pd.DataFrame()  #cria tabela vazia 

for arquivo in lista_arquivo:
    if 'vendas' in arquivo.lower():
        tabela = pd.read_csv(f'C:\Users\Jean Lucas\Downloads\Vendas/{arquivo}')
        tabela_total = tabela_total.append(tabela)

print(tabela_total)
