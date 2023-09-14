import os
import shutil
from datetime import datetime, timedelta

#Determine a data do dia anterior
data_hoje = datetime.now()
data_ontem = data_hoje - timedelta(days=1)
pasta_ontem = data_ontem.strftime("%Y%m%d")

#Caminho da pasta de origem e destino
pasta_files = 'S:/Files'
pasta_origem = os.path.join(pasta_files, pasta_ontem, 'Curves')
pasta_destino = 'O:/_Hedge Accounting/RM/Source_BMF/TaxaSwap'

#Nome do arquivo a ser copiado
nome_arquivo = f'Curves_CurveFile_{pasta_ontem}_1.txt'

#verifique se a pasta de origem e o arquivo existem
if os.path.exists(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
    if os.path.exists(caminho_arquivo):
        #Copie o arquivo da pasta de origem para a pasta de destino
        shutil.copy2(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
        print(f'Arquivo {nome_arquivo} copiado com sucesso para {pasta_destino}')
    else:
        print(f'O arquivo {nome_arquivo} não existe na pasta de origem {pasta_origem}')
else:
    print(f'A pasta de origem {pasta_ontem} não existe')