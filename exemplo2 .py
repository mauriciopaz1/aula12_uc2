import os
os.system('cls')
import pandas as pd
import polars as pl 
from datetime import datetime
import gc


try:
    ENDERECO_DADOS = r'./Dados/'

    incio = datetime.now()
    lista_arquivos = ['202401_NovoBolsaFamilia.csv', '202402_NovoBolsaFamilia.csv']
    # print(lista_arquivos)
    
    # hora_impressao = datetime.now()
    # print(f'Tempo de Execução: {hora_impressao - incio}')

    for arquivo in lista_arquivos:
        print(f'Processando Arquivo {arquivo}')
        
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding= 'iso-8859-1')

        if 'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        else:
            df_bolsa_familia = df
    print(df.head())
   
    # del df
    # gc.collect()


except ImportError as e:
    print("Erro ao obter dados: ", e)



