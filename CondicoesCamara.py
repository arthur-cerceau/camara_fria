# Dados [TODAS AS UNIDADES ESTÃO NO S.I.]

class Isolante:
    """Nome do Isolante, Coeficiente de condução de calor, largura da parede
    """

    def __init__(self, name, k, length):
        self.name = name
        self.k = k
        self.length = length


class Chapa:
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

    def __init__(self, temp_entrada, num_pessoas, tempo_pessoas, alfa_ext, alfa_int, qtd_total):
        self.temp_entrada = temp_entrada
        self.num_pessoas = num_pessoas
        self.tempo_pessoas = tempo_pessoas
        self.alfa_ext = alfa_ext
        self.alfa_int = alfa_int
        self.qtd_total = qtd_total


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


class Embalagem:
    """Massa diária embalagem, Calor específico da embalagem, Temperatura
    inicial da embalagem
    """

    def __init__(self, name, massa_diaria, Cp, Ti):
        self.name = name
        self.massa_diaria = massa_diaria
        self.Temp_inicial = Ti
        self.Cp = Cp
