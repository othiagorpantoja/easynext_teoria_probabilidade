"""
Caminhada Aleatória
Demonstra processos estocásticos e suas aplicações
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

class CaminhadaAleatoria:
    """
    Classe para simular caminhadas aleatórias
    """
    
    def __init__(self, posicao_inicial=0):
        self.posicao_inicial = posicao_inicial
        self.posicoes = [posicao_inicial]
        self.passos = []
    
    def passo_simples(self, tamanho=1):
        """
        Dá um passo simples (esquerda ou direita)
        """
        direcao = random.choice([-1, 1])
        passo = direcao * tamanho
        self.passos.append(passo)
        nova_posicao = self.posicoes[-1] + passo
        self.posicoes.append(nova_posicao)
        return passo
    
    def passo_gaussiano(self, media=0, desvio=1):
        """
        Dá um passo com distribuição gaussiana
        """
        passo = np.random.normal(media, desvio)
        self.passos.append(passo)
        nova_posicao = self.posicoes[-1] + passo
        self.posicoes.append(nova_posicao)
        return passo
    
    def caminhar(self, n_passos, tipo='simples', **kwargs):
        """
        Realiza uma caminhada de n passos
        """
        self.posicoes = [self.posicao_inicial]
        self.passos = []
        
        for _ in range(n_passos):
            if tipo == 'simples':
                self.passo_simples(kwargs.get('tamanho', 1))
            elif tipo == 'gaussiano':
                self.passo_gaussiano(kwargs.get('media', 0), kwargs.get('desvio', 1))
        
        return self.posicoes, self.passos
    
    def reset(self):
        """
        Reseta a caminhada para a posição inicial
        """
        self.posicoes = [self.posicao_inicial]
        self.passos = []

def exemplo_caminhada_simples():
    """
    Exemplo: Caminhada aleatória simples
    """
    print("=== EXEMPLO: CAMINHADA ALEATÓRIA SIMPLES ===\n")
    
    # Parâmetros
    n_passos = 1000
    n_simulacoes = 100
    
    print("1. PARÂMETROS:")
    print(f"   Número de passos: {n_passos}")
    print(f"   Número de simulações: {n_simulacoes}")
    print("   Tipo: Passos de tamanho 1 para esquerda ou direita")
    
    # Simula múltiplas caminhadas
    caminhadas = []
    posicoes_finais = []
    
    for i in range(n_simulacoes):
        caminhada = CaminhadaAleatoria()
        posicoes, passos = caminhada.caminhar(n_passos, tipo='simples')
        caminhadas.append(posicoes)
        posicoes_finais.append(posicoes[-1])
    
    # Estatísticas
    posicoes_finais = np.array(posicoes_finais)
    media_posicao_final = np.mean(posicoes_finais)
    variancia_posicao_final = np.var(posicoes_finais)
    
    print(f"\n2. ESTATÍSTICAS DAS POSIÇÕES FINAIS:")
    print(f"   Média: {media_posicao_final:.3f}")
    print(f"   Variância: {variancia_posicao_final:.3f}")
    print(f"   Desvio padrão: {np.sqrt(variancia_posicao_final):.3f}")
    
    # Teoria: para caminhada simples, variância = n_passos
    print(f"\n3. COMPARAÇÃO COM TEORIA:")
    print(f"   Variância teórica: {n_passos}")
    print(f"   Variância observada: {variancia_posicao_final:.3f}")
    print(f"   Diferença: {abs(variancia_posicao_final - n_passos):.3f}")
    
    # Plota algumas caminhadas
    plt.figure(figsize=(15, 10))
    
    # Subplot 1: Algumas caminhadas individuais
    plt.subplot(2, 2, 1)
    for i in range(min(10, n_simulacoes)):
        plt.plot(caminhadas[i], alpha=0.7, linewidth=1)
    plt.xlabel('Passo')
    plt.ylabel('Posição')
    plt.title('Caminhadas Aleatórias Individuais')
    plt.grid(True, alpha=0.3)
    
    # Subplot 2: Distribuição das posições finais
    plt.subplot(2, 2, 2)
    plt.hist(posicoes_finais, bins=20, density=True, alpha=0.7, color='skyblue')
    
    # Sobrepoe distribuição normal teórica
    x_teorico = np.linspace(posicoes_finais.min(), posicoes_finais.max(), 100)
    y_teorico = stats.norm.pdf(x_teorico, 0, np.sqrt(n_passos))
    plt.plot(x_teorico, y_teorico, 'r-', linewidth=2, label='Distribuição Teórica')
    
    plt.xlabel('Posição Final')
    plt.ylabel('Densidade')
    plt.title('Distribuição das Posições Finais')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 3: Evolução da variância
    plt.subplot(2, 2, 3)
    variancias = []
    passos_analise = range(10, n_passos + 1, 10)
    
    for passo in passos_analise:
        posicoes_no_passo = [caminhada[passo] for caminhada in caminhadas]
        variancia = np.var(posicoes_no_passo)
        variancias.append(variancia)
    
    plt.plot(passos_analise, variancias, 'b-', linewidth=2, label='Variância Observada')
    plt.plot(passos_analise, passos_analise, 'r--', linewidth=2, label='Variância Teórica')
    plt.xlabel('Passo')
    plt.ylabel('Variância')
    plt.title('Evolução da Variância')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 4: Caminhada média
    plt.subplot(2, 2, 4)
    posicoes_medias = np.mean(caminhadas, axis=0)
    posicoes_std = np.std(caminhadas, axis=0)
    
    plt.plot(posicoes_medias, 'b-', linewidth=2, label='Posição Média')
    plt.fill_between(range(len(posicoes_medias)), 
                    posicoes_medias - posicoes_std, 
                    posicoes_medias + posicoes_std, 
                    alpha=0.3, color='blue', label='±1 Desvio Padrão')
    plt.xlabel('Passo')
    plt.ylabel('Posição')
    plt.title('Caminhada Média')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return caminhadas, posicoes_finais

def exemplo_caminhada_gaussiana():
    """
    Exemplo: Caminhada aleatória com passos gaussianos
    """
    print("\n=== EXEMPLO: CAMINHADA ALEATÓRIA GAUSSIANA ===\n")
    
    # Parâmetros
    n_passos = 1000
    n_simulacoes = 100
    media_passo = 0
    desvio_passo = 1
    
    print("1. PARÂMETROS:")
    print(f"   Número de passos: {n_passos}")
    print(f"   Número de simulações: {n_simulacoes}")
    print(f"   Média do passo: {media_passo}")
    print(f"   Desvio padrão do passo: {desvio_passo}")
    
    # Simula múltiplas caminhadas
    caminhadas = []
    posicoes_finais = []
    
    for i in range(n_simulacoes):
        caminhada = CaminhadaAleatoria()
        posicoes, passos = caminhada.caminhar(n_passos, tipo='gaussiano', 
                                            media=media_passo, desvio=desvio_passo)
        caminhadas.append(posicoes)
        posicoes_finais.append(posicoes[-1])
    
    # Estatísticas
    posicoes_finais = np.array(posicoes_finais)
    media_posicao_final = np.mean(posicoes_finais)
    variancia_posicao_final = np.var(posicoes_finais)
    
    print(f"\n2. ESTATÍSTICAS DAS POSIÇÕES FINAIS:")
    print(f"   Média: {media_posicao_final:.3f}")
    print(f"   Variância: {variancia_posicao_final:.3f}")
    print(f"   Desvio padrão: {np.sqrt(variancia_posicao_final):.3f}")
    
    # Teoria: para caminhada gaussiana, variância = n_passos * desvio_passo²
    variancia_teorica = n_passos * desvio_passo**2
    print(f"\n3. COMPARAÇÃO COM TEORIA:")
    print(f"   Variância teórica: {variancia_teorica}")
    print(f"   Variância observada: {variancia_posicao_final:.3f}")
    print(f"   Diferença: {abs(variancia_posicao_final - variancia_teorica):.3f}")
    
    # Plota os resultados
    plt.figure(figsize=(15, 10))
    
    # Subplot 1: Algumas caminhadas individuais
    plt.subplot(2, 2, 1)
    for i in range(min(10, n_simulacoes)):
        plt.plot(caminhadas[i], alpha=0.7, linewidth=1)
    plt.xlabel('Passo')
    plt.ylabel('Posição')
    plt.title('Caminhadas Aleatórias Gaussianas')
    plt.grid(True, alpha=0.3)
    
    # Subplot 2: Distribuição das posições finais
    plt.subplot(2, 2, 2)
    plt.hist(posicoes_finais, bins=20, density=True, alpha=0.7, color='lightgreen')
    
    # Sobrepoe distribuição normal teórica
    x_teorico = np.linspace(posicoes_finais.min(), posicoes_finais.max(), 100)
    y_teorico = stats.norm.pdf(x_teorico, 0, np.sqrt(variancia_teorica))
    plt.plot(x_teorico, y_teorico, 'r-', linewidth=2, label='Distribuição Teórica')
    
    plt.xlabel('Posição Final')
    plt.ylabel('Densidade')
    plt.title('Distribuição das Posições Finais')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 3: Evolução da variância
    plt.subplot(2, 2, 3)
    variancias = []
    passos_analise = range(10, n_passos + 1, 10)
    
    for passo in passos_analise:
        posicoes_no_passo = [caminhada[passo] for caminhada in caminhadas]
        variancia = np.var(posicoes_no_passo)
        variancias.append(variancia)
    
    plt.plot(passos_analise, variancias, 'b-', linewidth=2, label='Variância Observada')
    plt.plot(passos_analise, [p * desvio_passo**2 for p in passos_analise], 
            'r--', linewidth=2, label='Variância Teórica')
    plt.xlabel('Passo')
    plt.ylabel('Variância')
    plt.title('Evolução da Variância')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 4: Caminhada média
    plt.subplot(2, 2, 4)
    posicoes_medias = np.mean(caminhadas, axis=0)
    posicoes_std = np.std(caminhadas, axis=0)
    
    plt.plot(posicoes_medias, 'b-', linewidth=2, label='Posição Média')
    plt.fill_between(range(len(posicoes_medias)), 
                    posicoes_medias - posicoes_std, 
                    posicoes_medias + posicoes_std, 
                    alpha=0.3, color='blue', label='±1 Desvio Padrão')
    plt.xlabel('Passo')
    plt.ylabel('Posição')
    plt.title('Caminhada Média')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return caminhadas, posicoes_finais

def exemplo_caminhada_bidimensional():
    """
    Exemplo: Caminhada aleatória bidimensional
    """
    print("\n=== EXEMPLO: CAMINHADA ALEATÓRIA BIDIMENSIONAL ===\n")
    
    # Parâmetros
    n_passos = 1000
    n_simulacoes = 5
    
    print("1. PARÂMETROS:")
    print(f"   Número de passos: {n_passos}")
    print(f"   Número de simulações: {n_simulacoes}")
    print("   Dimensão: 2D")
    
    # Simula caminhadas bidimensionais
    caminhadas_x = []
    caminhadas_y = []
    
    for i in range(n_simulacoes):
        # Caminhada em X
        caminhada_x = CaminhadaAleatoria()
        posicoes_x, _ = caminhada_x.caminhar(n_passos, tipo='gaussiano')
        
        # Caminhada em Y
        caminhada_y = CaminhadaAleatoria()
        posicoes_y, _ = caminhada_y.caminhar(n_passos, tipo='gaussiano')
        
        caminhadas_x.append(posicoes_x)
        caminhadas_y.append(posicoes_y)
    
    # Plota as caminhadas
    plt.figure(figsize=(15, 10))
    
    # Subplot 1: Caminhadas no plano
    plt.subplot(2, 2, 1)
    for i in range(n_simulacoes):
        plt.plot(caminhadas_x[i], caminhadas_y[i], alpha=0.7, linewidth=1)
        plt.scatter(caminhadas_x[i][0], caminhadas_y[i][0], color='green', s=50, marker='o')
        plt.scatter(caminhadas_x[i][-1], caminhadas_y[i][-1], color='red', s=50, marker='s')
    
    plt.xlabel('Posição X')
    plt.ylabel('Posição Y')
    plt.title('Caminhadas Aleatórias Bidimensionais')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # Subplot 2: Distância da origem
    plt.subplot(2, 2, 2)
    for i in range(n_simulacoes):
        distancias = np.sqrt(np.array(caminhadas_x[i])**2 + np.array(caminhadas_y[i])**2)
        plt.plot(distancias, alpha=0.7, linewidth=1)
    
    plt.xlabel('Passo')
    plt.ylabel('Distância da Origem')
    plt.title('Distância da Origem vs Passo')
    plt.grid(True, alpha=0.3)
    
    # Subplot 3: Distribuição das distâncias finais
    plt.subplot(2, 2, 3)
    distancias_finais = []
    for i in range(n_simulacoes):
        dist_final = np.sqrt(caminhadas_x[i][-1]**2 + caminhadas_y[i][-1]**2)
        distancias_finais.append(dist_final)
    
    plt.hist(distancias_finais, bins=10, density=True, alpha=0.7, color='orange')
    plt.xlabel('Distância Final')
    plt.ylabel('Densidade')
    plt.title('Distribuição das Distâncias Finais')
    plt.grid(True, alpha=0.3)
    
    # Subplot 4: Evolução da distância média
    plt.subplot(2, 2, 4)
    distancias_medias = []
    for passo in range(n_passos + 1):
        dist_passo = []
        for i in range(n_simulacoes):
            dist = np.sqrt(caminhadas_x[i][passo]**2 + caminhadas_y[i][passo]**2)
            dist_passo.append(dist)
        distancias_medias.append(np.mean(dist_passo))
    
    plt.plot(distancias_medias, 'b-', linewidth=2)
    plt.xlabel('Passo')
    plt.ylabel('Distância Média')
    plt.title('Evolução da Distância Média')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return caminhadas_x, caminhadas_y

def exemplo_aplicacoes_caminhada_aleatoria():
    """
    Demonstra aplicações da caminhada aleatória
    """
    print("\n=== APLICAÇÕES DA CAMINHADA ALEATÓRIA ===\n")
    
    print("1. APLICAÇÕES EM FÍSICA:")
    print("   - Movimento browniano de partículas")
    print("   - Difusão de moléculas")
    print("   - Propagação de ondas")
    
    print("\n2. APLICAÇÕES EM FINANÇAS:")
    print("   - Modelagem de preços de ações")
    print("   - Teoria do passeio aleatório")
    print("   - Opções e derivativos")
    
    print("\n3. APLICAÇÕES EM BIOLOGIA:")
    print("   - Migração de animais")
    print("   - Evolução de populações")
    print("   - Propagação de doenças")
    
    print("\n4. APLICAÇÕES EM COMPUTAÇÃO:")
    print("   - Algoritmos de otimização")
    print("   - Simulação de redes")
    print("   - Algoritmos genéticos")
    
    print("\n5. PROPRIEDADES MATEMÁTICAS:")
    print("   - Martingales")
    print("   - Processos de Markov")
    print("   - Teorema central do limite")

if __name__ == "__main__":
    # Executa todos os exemplos
    caminhadas_simples, posicoes_finais_simples = exemplo_caminhada_simples()
    caminhadas_gaussianas, posicoes_finais_gaussianas = exemplo_caminhada_gaussiana()
    caminhadas_x, caminhadas_y = exemplo_caminhada_bidimensional()
    exemplo_aplicacoes_caminhada_aleatoria()
