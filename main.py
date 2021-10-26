import pandas as pd
import numpy as np
import time 

# Enviar msg no Boot
def envio_relatorio(mensagem):
    import requests

    message = mensagem
    url_send_message = 'http://151.106.108.32:5500/send-group-message'
    data = {
        'id':'558681889492-1629742189@g.us',
        'message': message
    }
    requests.post(url_send_message, data=data)


def exportarImagem(detalhamento):
    import dataframe_image as dfi

    dfi.export(detalhamento, 'extratoRota.png')
    print('Imagem Exportada!')



dir = (r'I:\OneDrive\Professional\09 - Transportta\Sistema\Relatorio\extratoMotorista\HistoricoRotas-2021-10-19_2021-10-19.xlsx')
dados = pd.read_excel(dir, sheet_name='Planilha')

motoristas = pd.DataFrame(dados['Motorista'].unique(),columns=['Motorista'])

# print (dados['Motorista'].value_counts())

for i, motorista in motoristas.iterrows():
    relatorio=[]
    relatorio.clear()
    
    for index, row in dados.iterrows():
        if motorista['Motorista'] == row['Motorista']:
            relatorio.append(row['Rota'])
    envio_relatorio(row['Rota'])
    time.sleep(1)

    relatorio = pd.DataFrame(relatorio,columns=[motorista])





