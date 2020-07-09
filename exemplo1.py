#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:04:13 2020

@author: natalia
"""

from pyPEC import Dados

"""Lendo um arquivo gerado pelo Metashape, no qual estão as discrepâncias dos
pontos de verificação e os resíduos dos pontos de apoio

Na coluna 1 estão os nomes dos pontos.

As discrepâncias e residuos estão nas colunas 7, 8 e 9 e o arquivo tem duas linhas
com informações de cabeçalho que devem ser ignoradas

V e C são os identificadores dos pontos de verificação e apoio, respectivamente
"""
caminho_para_relatorio = '/home/natalia/Documentos/Mestrado/pyPEC-PCD/exemplo/2Faixas_5Bases_Erros.txt'

dados_metashape = Dados(caminho_para_relatorio, [1,7,8,9], 2, 'V', 'C')
dados_metashape.ler_arquivo()

t_X, t_Y, t_Z = dados_metashape.analise_de_tendencia_discrepancias()

print('============== Estatistica t ===================')
print('======= para análise de tendência ==============')
print('t_X: ', t_X)
print('t_Y: ', t_Y)
print('t_Z: ', t_Z)

print('\n============== Grau de Lib. ===================')
print(len(dados_metashape.discrepancias_pontos_check)-1)

print('\n============== Acuracia ===================')
print(dados_metashape.calcular_acuracia_planimetrica())

valores_qui_quadrado = dados_metashape.analise_de_precisao(100.0)

print('Qui_X: ', valores_qui_quadrado[0])
print('Qui_Y: ', valores_qui_quadrado[1])
print('Qui_Z: ', valores_qui_quadrado[2])

#============== Gerando os graficos de dispersão das disc. planimétricas

caminho_salvar_grafico = '/home/natalia/Documentos/Mestrado/pyPEC-PCD/exemplo/graficos/Grafico_plan.png'
dados_metashape.gerar_graficos_tendencia_planimetrica(caminho_salvar_grafico)

#============== Gerando os graficos de dispersão das disc. altimétricas

caminho_salvar_grafico_alt = '/home/natalia/Documentos/Mestrado/pyPEC-PCD/exemplo/graficos/Grafico_alt.png'

dados_metashape.gerar_grafico_tendencia_altimetrica(caminho_salvar_grafico_alt)

# Desvio padrão amostral

dados_metashape.calcular_desvio_padrao_amostral()

print('=========== Desvio Padrão ============')

print(dados_metashape.desvio_amostral[0])
print(dados_metashape.desvio_amostral[1])
print(dados_metashape.desvio_amostral[2])

print('=========== Media ============')

dados_metashape.calcular_media_discrepancias()
print(dados_metashape.media_aritmetica[0])
print(dados_metashape.media_aritmetica[1])
print(dados_metashape.media_aritmetica[2])