#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:15:18 2020

@author: Natalia C. de Amorim
"""

from .Dados import Dados

class Plot:
    
    @staticmethod
    def gerar_graficos_tendencia_planimetrica(CAMINHO_ARQUIVO_GRAFICO, points):
        
        import matplotlib.pyplot as plt
        import numpy as np
        import statistics
        #rom matplotlib.pyplot import figure
        
        plt.figure(figsize=(4,4))
        plt.title("Discrepâncias nos Pontos de Verificação", y=1.02)
        for i in range(len(points)):
            plt.scatter(points[i][1], points[i][2], color="blue")
            plt.text(points[i][1] * (1 + 0.01), points[i][2] * (1 + 0.01) , points[i][0], fontsize=8)
        #plt.scatter(x_residual, y_residual, color="blue")
        plt.scatter(statistics.mean([l[1] for l in points]), 
                     statistics.mean([l[2] for l in points]), 
                      color="red")
        plt.xlabel("Discrepância em X (cm)", labelpad=2)
        plt.ylabel("Discrepância em Y (cm)", labelpad=2)
        plt.grid()
        plt.tick_params(pad=3)
        plt.savefig(CAMINHO_ARQUIVO_GRAFICO, dpi=300, bbox_inches = "tight")
        plt.show()
    
    
    @staticmethod
    def gerar_grafico_tendencia_altimetrica(CAMINHO_ARQUIVO_GRAFICO, points):
        
        import matplotlib.pyplot as plt
        import numpy as np
        
        objects = tuple([l[0] for l in points])
        y_pos = np.arange(len(objects))
        
        plt.figure(figsize=(4, 4)) 
        plt.bar(y_pos, [l[3] for l in points], align='center', alpha=1.0, width=0.8)
        plt.xticks(y_pos, objects, fontsize=9, rotation=90)
        plt.grid(axis='y')
        plt.ylabel('Discrepância (cm)', labelpad=2)
        plt.title('Discrepâncias Altimétricas')
        plt.savefig(CAMINHO_ARQUIVO_GRAFICO, dpi=300, bbox_inches = "tight")
        plt.show()