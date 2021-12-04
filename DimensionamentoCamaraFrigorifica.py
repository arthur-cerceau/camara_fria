from ParametrosProjeto import *

print(f'''Calculo da carga térmica para uma câmara fria para armazenamento de
{condicoes.qtd_total} kg de {produto.name} com movimentação diária de {0.2 * condicoes.qtd_total} kg ''')

# Calculo da Resistencia Térmica Total

R_total = R_conv_ext(condicoes.alfa_ext) + R_conv_int(condicoes.alfa_int) + \
          2 * R_chapa(chapa.length, chapa.k) + R_iso(iso.length, iso.k)

# Calculo ganho de calor por unidade de área
# Q paredes e teto

Q_paredes_teto = (camara.temp_ext - camara.temp_int) / R_total

# Q piso

Q_piso = (camara.temp_piso - camara.temp_int) / R_total

# Calculo da carga térmica devido a transmissão de calor:
# Qtm = (Q/A)*A*24 [kcal/dia]

Q_tm = Q_paredes_teto * (camara.area_piso_teto() + camara.area_paredes()) * 24 + \
       Q_piso * (camara.area_piso_teto()) * 24

print(f'\nCarga térmica devido a transmissão de calor: Qtm = {Q_tm:.2f} [kcal/dia]')

# Calculo da carga térmica devido ao produto

Q_prod = condicoes.qtd_total * 0.2 * (produto.calor_especif_antes_congel *
                                      (condicoes.temp_entrada - produto.temp_conservacao) +
                                      produto.calor_latente + produto.calor_especif_pos_congel * (
                                              produto.temp_conservacao - produto.ponto_congel)) + \
         condicoes.qtd_total * produto.calor_resp

print(f'\nCarga térmica devido aos produtos: Qprod = {Q_prod:.2f} [kcal/dia]')

# Calculo da carga térmica devido a infiltração de ar externo

Q_inf = camara.volume_interno() * FTA * DH
print(f'\nCarga térmica devido a infiltração de ar externo: Qinf = {Q_inf:.2f} [kcal/dia]')

# Calculo de carga térmica devido a pessoas

Q_pes = condicoes.num_pessoas * condicoes.tempo_pessoas * q
print(f'\nCarga térmica devido a pessoas: Qpes = {Q_pes:.2f} [kcal/dia]')

# Calculo de carga térmica devido a embalagem

Q_emb = emb.massa_diaria * emb.Cp * (emb.Temp_inicial - produto.temp_conservacao)
print(f'\nCarga térmica devido a embalagem: Qemb = {Q_emb:.2f} [kcal/dia]')

# Calculo da carga térmica devido a iluminação

Q_ilum = 10 * camara.area_piso_teto() * condicoes.tempo_pessoas * 0.86
print(f'\nCarga térmica devido a iluminação: Qilum = {Q_ilum:.2f} [kcal/dia]')

# Ganho de calor total

Q_total = Q_tm + Q_prod + Q_inf + Q_pes + Q_ilum + Q_emb

print(f'''\nO ganho de calor total é: Qtotal = {Q_total:.2f} [kcal/dia]...
Adotando um tempo de funcionamento de {tempo_funcionamento} horas tem-se que:
Carga térmica total: Q = {(Q_total / tempo_funcionamento) * (1 + fator_seg / 100):.2f} [kcal/hora]
para um fator de segurança de {fator_seg}%''')
