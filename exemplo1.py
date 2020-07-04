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

Check e C são os identificadores dos pontos de verificação e apoio, respectivamente
"""
dados_metashape = Dados('/home/natalia/Documentos/Mestrado/pyPEC-PCD/exemplo/2Faixas_5Bases_Erros.txt', 
                        [1,7,8,9], 2, 'Check', 'C')
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

