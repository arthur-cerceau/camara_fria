import sys
import json
from CondicoesCamara import *

sys.path.append(".")

#
nome_produto = 'Carne bov. magra fresca'
dim_camara = {
    "temp_int": -1,
    "temp_ext": 35,
    "temp_piso": 15,
    "umidade_relativa": 60,
    "largura": 3,
    "comprimento": 2,
    "altura": 2
}
condicoes_projeto = {
    "temp_entrada": 3,
    "num_pessoas": 1,
    "tempo_pessoas": 3,
    "alfa_ext": 30,
    "alfa_int": 10,
    "qtd_total": 3000
}
#


# tabela de dados em json dos parametros

tabela_produto = json.load(open('produto_table.json'))

# Condições de projeto

iso = Isolante('Poliuretano', 0.023, 0.1)

chapa = Chapa('Aço Inoxidavel', 12.8, 0.005)

camara = Camara(**dim_camara)
condicoes = Condicoes(**condicoes_projeto)
# condicoes = Condicoes(3,1,3,30,10,2000)

indice = 0
for i, produto in enumerate(tabela_produto):
    if nome_produto in tabela_produto[i]['name']:
        indice = i

produto = Produto(**tabela_produto[indice])

emb = Embalagem('Plástico', 0, 0, 0)

FTA = 22.4

DH = 31.4

q = 238

tempo_funcionamento = 18

fator_seg = 10  # %


# Calculo da resistencia termica

def R_conv_ext(alfa_ext):
    return 1 / alfa_ext


def R_conv_int(alfa_int):
    return 1 / alfa_int


def R_chapa(L_ch, k_ch):
    return L_ch / k_ch


def R_iso(L_iso, k_iso):
    return L_iso / k_iso
