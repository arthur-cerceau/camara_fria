# Dados [TODAS AS UNIDADES ESTÃO NO S.I.]
import bisect
from scipy.interpolate import interp1d

class Isolante:
    """Coeficiente de condução de calor, largura da parede
    """

    def __init__(self, k, length):
        self.k = k
        self.length = length


class Chapa(object):
    """Material da chapa, coeficiente de condução de calor, largura da chapa
    """

    def __init__(self, name, k, length):
        self.name = name
        self.k = k
        self.length = length


class Camara(object):
    """Temperatura Interna, Temperatura Externa,Temperatura do piso,
    Umidade Relativa, Largura, Comprimento e Altura da Câmara
    """

    def __init__(self, temp_int, temp_ext, temp_piso, umidade_relativa, largura, comprimento, altura):
        self.temp_int = temp_int
        self.temp_ext = temp_ext
        self.temp_piso = temp_piso
        self.umidade_relativa = umidade_relativa
        # Dimensões internas da câmara
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura

    # Calculo das áreas
    def area_piso_teto(self):
        return self.largura * self.comprimento

    def area_paredes(self):
        return 2 * (self.largura * self.altura) + 2 * (self.comprimento * self.altura)

    def volume_interno(self):
        return self.largura * self.comprimento * self.altura


class Condicoes(object):
    """Temperatura de Entrada do produto na câmara, Numero de pessoas,
    Tempo de permanencia das pessoas, Coeficientes de convecçao externo
    e interno
    """

    def __init__(self, temp_entrada, num_pessoas, tempo_pessoas, alfa_ext, alfa_int, qtd_total, q_a):
        self.temp_entrada = temp_entrada
        self.num_pessoas = num_pessoas
        self.tempo_pessoas = tempo_pessoas
        self.alfa_ext = alfa_ext
        self.alfa_int = alfa_int
        self.qtd_total = qtd_total
        self.q_a = q_a

class Produto(object):
    """Nome do produto, Temperatura de conservação, Umidade relativa, Cp antes,
    Cp pós, calor latente, Temperatura de congelamento, calor respiração
    [DADOS DA TABELA]
    """

    def __init__(self, name, temp_conservacao, umidade_relativa, calor_especif_antes_congel, calor_especif_pos_congel,
                 calor_latente, ponto_congel, calor_resp):
        self.name = name
        self.temp_conservacao = temp_conservacao
        self.umidade_relativa = umidade_relativa
        self.calor_especif_antes_congel = calor_especif_antes_congel
        self.calor_especif_pos_congel = calor_especif_pos_congel
        self.calor_latente = calor_latente
        self.ponto_congel = ponto_congel
        self.calor_resp = calor_resp


class Embalagem(object):
    """Massa diária embalagem, Calor específico da embalagem, Temperatura
    inicial da embalagem
    """

    def __init__(self, name, massa_diaria, cp, temp_entrada):
        self.name = name
        self.massa_diaria = massa_diaria
        self.temp_entrada = temp_entrada
        self.cp = cp
        
# Calculo da resistencia termica

def R_conv_ext(alfa_ext):
    return 1 / alfa_ext

def R_conv_int(alfa_int):
    return 1 / alfa_int

def R_chapa(L_ch, k_ch):
    return L_ch / k_ch

def R_iso(L_iso, k_iso):
    return L_iso / k_iso

# Seleção da espessura do isolante térmico

def escolher_espessura(length, x):
    i = bisect.bisect_right(length, x)
    return length[i]

# Tabela dados q (calor por pessoas)
tab_qt = [10,5,0,-5,-10,-15,-20,25]
tab_qq = [181,208,233,258,279,312,337,360]

# Tabela FTA

tab_ftav = [40,50,60,80,100,125,150,200,300,
            400,500,700,1000,1200,1500,2000,3000,5000,10000,15000]
tab_ftar = [15,13,12,10,9,8,7,6,5,4.10,3.60,3,2.5,2.2,2,1.7,1.4,1.1,0.95,0.9]
tab_ftac = [11,10,9,8,7,6,5.5,4.5,3.7,3.2,2.8,2.3,1.9,1.7,1.5,1.3,1.1,1,0.8,0.8]