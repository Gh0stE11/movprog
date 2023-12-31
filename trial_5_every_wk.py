import os
import shutil
from datetime import datetime, timedelta

# Função para verificar a existência do arquivo TXT e obter a confirmação do usuário
def verificar_e_obter_confirmacao(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        return False
    resposta = input(f'O arquivo {caminho_arquivo} não existe em formato TXT. Deseja renomear o arquivo CSV para TXT? (S/N): ')
    return resposta.strip().upper() == 'S'

# Determine a data do dia anterior
data_hoje = datetime.now()

# Subtrai um dia da data atual
data_ontem = data_hoje - timedelta(days=1)

# Verifique se a data do dia anterior é um dia útil (segunda a sexta-feira)
while data_ontem.weekday() >= 5:  # 5 representa sábado e 6 representa domingo
    data_ontem -= timedelta(days=1)

pasta_ontem = data_ontem.strftime("%Y%m%d")

# Caminho da pasta de origem e destino
pasta_files = 'S:/Files'
pasta_origem = os.path.join(pasta_files, pasta_ontem, 'Curves')
pasta_destino = 'O:/_Hedge Accounting/RM/Source_BMF/TaxaSwap'  # Substitua pelo caminho desejado

# Nome do arquivo a ser copiado
nome_arquivo = f'Curves_CurveFile_{pasta_ontem}_1.txt'
caminho_arquivo_txt = os.path.join(pasta_origem, nome_arquivo)

# Verifique se a pasta de origem e o arquivo existem
if os.path.exists(pasta_origem):
    if os.path.exists(caminho_arquivo_txt):
        # O arquivo TXT já existe
        print(f'O arquivo {nome_arquivo} já existe em formato TXT.')
    else:
        # Verifique se há um arquivo CSV com o mesmo nome
        caminho_arquivo_csv = caminho_arquivo_txt.replace('.txt', '.csv')
        if os.path.exists(caminho_arquivo_csv):
            # Verifique se o usuário deseja renomear o arquivo CSV para TXT
            confirmacao = verificar_e_obter_confirmacao(caminho_arquivo_txt)
            if confirmacao:
                # Copie o arquivo CSV e renomeie-o para TXT
                shutil.copy2(caminho_arquivo_csv, os.path.join(pasta_destino, nome_arquivo))
                print(f'Arquivo {caminho_arquivo_csv} copiado e renomeado para {nome_arquivo} em {pasta_destino}')
        else:
            print(f'O arquivo {nome_arquivo} em formato TXT não foi encontrado e não há um arquivo CSV correspondente.')
else:
    print(f'A pasta de origem {pasta_ontem} não existe.')
