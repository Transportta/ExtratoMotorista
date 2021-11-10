from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
import time
import dataframe_image as dfi

# Enviar msg
def envio_extrato(message, image, contato):
    import requests
    
    url = "http://bot.transportta.online/send-media"
    payload = {'number': contato, 'caption': message}

    files = [('file', ('baixados.png', image, 'image/png'))]
    requests.request("POST", url, data=payload, files=files)
    print('Extrato de Rota enviado no Whatsapp')

# Ler as Bases -------
dir = (r'I:\OneDrive\Professional\09 - Transportta\Sistema\Relatorio\extratoMotorista\Escala de Rotas 20.10.2021--18-09 -AT.xlsx')
r2 = (r'I:\OneDrive\Professional\09 - Transportta\Sistema\Relatorio\extratoMotorista\motoristas.xlsx')

dados = pd.read_excel(dir, sheet_name='ESCALA')
rMotorista = pd.read_excel(r2, sheet_name='Relacao')
#-----  Fim da Leitura

motoristas = pd.DataFrame(dados['MOTORISTA'].unique(), columns=['MOTORISTA'])


for i, motorista in motoristas.iterrows():
    # contato = (rMotorista.loc[rMotorista['Motorista']=='motorista']['Contato']).values[0]
    contato = (rMotorista.loc[rMotorista['Apelido']=='WESLLEY']['Contato']).values[0]
    extrato = []
    extrato.clear()

    for index, row in dados.iterrows():
        if motorista['MOTORISTA'] == row['MOTORISTA']:
            extrato.append([row['MOTORISTA'], row['ROTA'], row['HORARIOS']])

    extrato = pd.DataFrame(extrato, columns=['Motorista', 'Rotas', 'Horarios'])
    extrato = (extrato.pivot_table(index=["Motorista", "Rotas", "Horarios"], aggfunc=np.mean)).sort_values(by=['Horarios'], ascending=True)

    time.sleep(2)
    dfi.export(extrato, 'extratoRota.png')
    envio_extrato('Extrato de Rotas do dia 20/10/21', open('extratoRota.png', 'rb').read(), f'55{contato}@c.us')
