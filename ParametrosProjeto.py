import sys
import json
from CondicoesCamara import *

sys.path.append(".")

# PARAMETROS DE PROJETO #
nome_produto = 'Carne bov. magra fresca'
tipo_isolante = 'Poliuretano'

dim_camara = {
    "temp_int": -1, # ºC
    "temp_ext": 35, # ºC
    "temp_piso": 15, # ºC
    "umidade_relativa": 60, # %
    "largura": 3, # m
    "comprimento": 2, # m
    "altura": 2 # m
}
condicoes_projeto = {
    "temp_entrada": 3, # ºC
    "num_pessoas": 1, # numero de pessoas
    "tempo_pessoas": 3, # tempo de permanencia de pessoas na camara
    "alfa_ext": 30, # coeficiente de convecção externo
    "alfa_int": 10, # coeficiente de convecção interno
    "qtd_total": 3000, # quantidade total de produto diária
    "q_a": 9 # ganho de calor projetado
}
dim_chapa = {
    "name": 'Aço Inoxidavel', #material da chapa de cobertura
    "k": 12.8, #coeficiente de condução de calor
    "length": 0.005 # espessura em m
}
dim_emb = {
    "name": 'Plástico',
    "massa_diaria": 0,
    "cp": 0,
    "temp_entrada": 0
}

mov_prod = 0.2 # 20% de movimentação de produtos
DH = 31.4
q = 238
tempo_funcionamento = 18
fator_seg = 10  # %

#########################


# tabela de dados em json dos parametros

tabela_produto = json.load(open('produto_table.json'))
tabela_isolante = json.load(open('iso_table.json'))

# Condições de projeto

emb = Embalagem(**dim_emb)
iso = Isolante(**tabela_isolante[tipo_isolante])
chapa = Chapa(**dim_chapa)
camara = Camara(**dim_camara)
condicoes = Condicoes(**condicoes_projeto)


indice = 0
for i, produto in enumerate(tabela_produto):
    if nome_produto in tabela_produto[i]['name']:
        indice = i

produto = Produto(**tabela_produto[indice])
#22.4
# Calculo do FTA conforme a tabela
if camara.temp_int > produto.ponto_congel:
    FTA_interp = interp1d(tab_ftav,tab_ftar,axis=0, fill_value="extrapolate")
else:
    FTA_interp = interp1d(tab_ftav,tab_ftac,axis=0, fill_value="extrapolate")

FTA = FTA_interp(camara.volume_interno())

DH = 31.4

# Calculo do q

q_interp = interp1d(tab_qt, tab_qq)

q = q_interp(camara.temp_int)

# Calculo do FTA

