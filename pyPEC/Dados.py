#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:41:57 2020

@author: natalia
"""

import math
import statistics


class Dados:
    
    discrepancias_pontos_check  = []
    residuos_pontos_controle = []

    
    EQM_planimetrico = 0
    
    def __init__(self, FILE_PATH, colunas, linhas_a_ignorar, check_id, controle_id):
        self.FILE_PATH = FILE_PATH #caminho para o arquivo contendo os dados de precisão e acurácia
        self.colunas = colunas
        self.linhas_a_ignorar = linhas_a_ignorar
        self.check_id = check_id
        self.controle_id = controle_id
        
    
    def ler_arquivo(self):
        arquivo = open(self.FILE_PATH, 'r')
        disc_e_residuos = []
        
        if arquivo:
            print("LEITURA REALIZADA COM SUCESSO!")
            
            linhas = arquivo.readlines()
            contador = 0
            
            for linha in linhas:
                if contador <= self.linhas_a_ignorar -1:
                    contador+= 1
                    continue
                else:
                    linha_separada = linha.split()
                    if self.check_id in linha_separada[self.colunas[0]-1]:
                        ponto = []
                        ponto.append(linha_separada[self.colunas[0]-1])
                        ponto.append(float(linha_separada[self.colunas[1]-1]))
                        ponto.append(float(linha_separada[self.colunas[2]-1]))
                        ponto.append(float(linha_separada[self.colunas[3]-1]))
                        self.discrepancias_pontos_check.append(ponto)
                    
                    elif self.controle_id in linha_separada[self.colunas[0]-1]:
                        ponto = []
                        ponto.append(linha_separada[self.colunas[0]-1])
                        ponto.append(float(linha_separada[self.colunas[1]-1]))
                        ponto.append(float(linha_separada[self.colunas[2]-1]))
                        ponto.append(float(linha_separada[self.colunas[3]-1]))
                        self.residuos_pontos_controle.append(ponto)
            
            self.converter_unidades()
        else:
            print("NÃO FOI POSSÍVEL LER O ARQUIVO, POR FAVOR, VERIFIQUE O CAMINHO INFORMADO!")
            
    def converter_unidades(self):
        
        for ponto in self.discrepancias_pontos_check:
            if int(ponto[1]) == 0:
                ponto[1] *= 100 #converte para centimetros
            if int(ponto[2]) == 0:
                ponto[2] *= 100 #converte para centimetros
            if int(ponto[3]) == 0:
                ponto[3] *= 100 #converte para centimetros
        
        
    def analise_de_tendencia_discrepancias(self):        
        media_X = (sum([linha[1] for linha in self.discrepancias_pontos_check]) /
                   len([linha[1] for linha in self.discrepancias_pontos_check]))
        
        media_Y = (sum([linha[2] for linha in self.discrepancias_pontos_check]) /
                   len([linha[2] for linha in self.discrepancias_pontos_check]))
        
        media_Z = (sum([linha[3] for linha in self.discrepancias_pontos_check]) /
                   len([linha[3] for linha in self.discrepancias_pontos_check]))
    
        t_calc_X = ((media_X / 
                    statistics.stdev([linha[1] for linha in self.discrepancias_pontos_check])) *
                    math.sqrt(len([linha[1] for linha in self.discrepancias_pontos_check])))
        
        t_calc_Y = ((media_Y / 
                    statistics.stdev([linha[2] for linha in self.discrepancias_pontos_check])) *
                    math.sqrt(len([linha[2] for linha in self.discrepancias_pontos_check])))
        
        t_calc_Z = ((media_Z / 
                    statistics.stdev([linha[3] for linha in self.discrepancias_pontos_check])) *
                    math.sqrt(len([linha[3] for linha in self.discrepancias_pontos_check])))
        
        return [t_calc_X, t_calc_Y, t_calc_Z]
        
    """    
    def calcular_desvio_padrao_amostral():
        pass
    
    def calcular_media_discrepancias():
        pass"""
    
    def calcular_erro_medio_quadratico_plan(self):
        
        EQM_x = math.sqrt((sum([linha[1]**2 for linha in self.discrepancias_pontos_check]) /
                 len([linha[1] for linha in self.discrepancias_pontos_check])))
        
        EQM_y = math.sqrt((sum([linha[2]**2 for linha in self.discrepancias_pontos_check]) /
                 len([linha[2] for linha in self.discrepancias_pontos_check])))
        
        self.EQM_planimetrico = math.sqrt(EQM_x**2 + EQM_y**2)
        
    
    def analise_de_precisao(self, EP):
        
        variancia_PEC = EP / (math.sqrt(2))
        n = len(self.discrepancias_pontos_check)
        variancia_amostral_X = statistics.variance([linha[1] for linha in self.discrepancias_pontos_check])
        variancia_amostral_Y = statistics.variance([linha[2] for linha in self.discrepancias_pontos_check])
        variancia_amostral_Z = statistics.variance([linha[3] for linha in self.discrepancias_pontos_check])
        
        print('Variancia X: ', variancia_amostral_X)
        print('Variancia Y: ', variancia_amostral_Y)
        print('Variancia Z: ', variancia_amostral_Z)
        
        qui_quadrado_X = ((n-1) * variancia_amostral_X) / variancia_PEC
        qui_quadrado_Y = ((n-1) * variancia_amostral_Y) / variancia_PEC
        qui_quadrado_Z = ((n-1) * variancia_amostral_Z) / variancia_PEC
        
        return [qui_quadrado_X, qui_quadrado_Y, qui_quadrado_Z]
        
    
    
    def calcular_acuracia_planimetrica(self, prob=90):        
        if self.EQM_planimetrico == 0:
            self.calcular_erro_medio_quadratico_plan()
            print('EQM plan.: ', self.EQM_planimetrico)
        
        if prob == 90:
            acuracia = 1.6449 * self.EQM_planimetrico
        elif prob == 95:
            acuracia = 1.96 * self.EQM_planimetrico
        
        return acuracia
        