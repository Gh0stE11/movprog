import shutil
import os   
from datetime import datetime, timedelta

# Diretório de origem
diretorio_origem = 'S:\\Files\\20230910\\Curves'

# Diretório de destino
diretorio_destino = 'C:\\Users\\caio.ishizu\\OneDrive - Capitania S.A\\Área de Trabalho\\teste'

# Obter a data atual
data_atual = datetime.now()

#Calcular a data do dia anterior
data_anterior = data_atual - timedelta(days=1)

#Formatar a data no formato desejado (por exemplo, "YYYY-MM-DD")
data_formatada = data_anterior.strftime('%Y%m%d')

# Nome do arquivo com base na data do dia anterior
nome_arquivo = f'Curves_CurveFileV2_{data_formatada}_1.txt'

# Caminhos completos do arquivo de origem e destino
caminho_origem = os.path.join(diretorio_origem, nome_arquivo)
caminho_destino = os.path.join(diretorio_destino, nome_arquivo)

# Verificar se o arquivo de origem existe antes de mover
if os.path.exists(caminho_origem):
    shutil.move(caminho_origem, caminho_destino)
    print(f'Arquivo txt movido com sucesso para pasta taxa swap!')
else:
    print(f'O arquivo txt não existe no diretório de origem.')