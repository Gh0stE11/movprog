import shutil
import os
from datetime import datetime, timedelta

# Diretório de destino
diretorio_destino = 'C:/Users/caio.ishizu/OneDrive - Capitania S.A/Área de Trabalho/teste'

# Calcular a data de 3 dias atrás
data_tres_dias_atras = datetime.now() - timedelta(days=3)

# Formatar a data no formato desejado (por exemplo, "YYYYMMDD")
data_formatada = data_tres_dias_atras.strftime('%Y%m%d')

# Construir o caminho de origem com base na data de 3 dias atrás
caminho_origem = os.path.join(f'S:/Files/{data_formatada}/Curves', 'Curves_CurveFileV2_{data_formatada}_1.txt')

# Verificar se o arquivo de origem existe antes de mover
if os.path.exists(caminho_origem):
    shutil.move(caminho_origem, diretorio_destino)
    print(f'Arquivo movido com sucesso para {diretorio_destino}')
else:
    print(f'O arquivo não existe no diretório de origem.')

