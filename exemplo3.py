import os
os.system('cls')
import pandas as pd
import polars as pl 
from datetime import datetime
import gc

ENDERECO_DADOS = r'./Dados/'

try:
    print('Obtendo Dados')
   
    incio = datetime.now()
    lista_arquivos = []    
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)

    for arquivo in lista_dir_arquivos:            
        
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    for arquivo in lista_arquivos:
        print(f'Processndo Arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding= 'iso-8859-1')

        if 'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df
    print(df.head())

    del df
    gc.collect()

except ImportError as e:
    print("Erro ao obter dados: ", e)



