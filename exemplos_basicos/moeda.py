"""
Exemplo básico: Lançamento de Moeda
Demonstra os conceitos fundamentais de espaço amostral e probabilidade
"""

import random
import matplotlib.pyplot as plt
from collections import Counter

class Moeda:
    """
    Classe que representa uma moeda e suas operações probabilísticas
    """
    
    def __init__(self):
        self.espaco_amostral = ['cara', 'coroa']
        self.historico = []
    
    def lancar(self):
        """
        Lança a moeda e retorna o resultado
        """
        resultado = random.choice(self.espaco_amostral)
        self.historico.append(resultado)
        return resultado
    
    def lancar_multiplas_vezes(self, n):
        """
        Lança a moeda n vezes e retorna os resultados
        """
        resultados = []
        for _ in range(n):
            resultados.append(self.lancar())
        return resultados
    
    def probabilidade_cara(self):
        """
        Calcula a probabilidade teórica de sair cara
        """
        return 1 / len(self.espaco_amostral)
    
    def probabilidade_coroa(self):
        """
        Calcula a probabilidade teórica de sair coroa
        """
        return 1 / len(self.espaco_amostral)
    
    def probabilidade_empirica(self, evento='cara', n_lancamentos=None):
        """
        Calcula a probabilidade empírica baseada no histórico
        """
        if n_lancamentos is None:
            n_lancamentos = len(self.historico)
        
        if n_lancamentos == 0:
            return 0
        
        # Usa apenas os últimos n_lancamentos
        historico_recente = self.historico[-n_lancamentos:]
        contagem = Counter(historico_recente)
        
        return contagem[evento] / n_lancamentos
    
    def plotar_resultados(self, n_lancamentos=1000):
        """
        Plota os resultados de múltiplos lançamentos
        """
        # Limpa o histórico e faz novos lançamentos
        self.historico = []
        resultados = self.lancar_multiplas_vezes(n_lancamentos)
        
        # Conta os resultados
        contagem = Counter(resultados)
        
        # Cria o gráfico
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Gráfico de barras
        eventos = list(contagem.keys())
        valores = list(contagem.values())
        cores = ['gold' if evento == 'cara' else 'silver' for evento in eventos]
        
        ax1.bar(eventos, valores, color=cores, alpha=0.7)
        ax1.set_title(f'Resultados de {n_lancamentos} lançamentos')
        ax1.set_ylabel('Frequência')
        ax1.set_xlabel('Resultado')
        
        # Adiciona valores nas barras
        for i, v in enumerate(valores):
            ax1.text(i, v + 0.01, str(v), ha='center', va='bottom')
        
        # Gráfico de probabilidade empírica ao longo do tempo
        probabilidades_cara = []
        for i in range(1, n_lancamentos + 1):
            prob = self.probabilidade_empirica('cara', i)
            probabilidades_cara.append(prob)
        
        ax2.plot(range(1, n_lancamentos + 1), probabilidades_cara, 'b-', alpha=0.7)
        ax2.axhline(y=0.5, color='r', linestyle='--', label='Probabilidade Teórica (0.5)')
        ax2.set_title('Convergência da Probabilidade Empírica')
        ax2.set_xlabel('Número de lançamentos')
        ax2.set_ylabel('Probabilidade de Cara')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        return contagem

def demonstrar_conceitos():
    """
    Demonstra os conceitos fundamentais da probabilidade com uma moeda
    """
    print("=== DEMONSTRAÇÃO: LANÇAMENTO DE MOEDA ===\n")
    
    # Cria uma moeda
    moeda = Moeda()
    
    print("1. ESPAÇO AMOSTRAL:")
    print(f"   Ω = {moeda.espaco_amostral}")
    print(f"   Número de resultados possíveis: {len(moeda.espaco_amostral)}\n")
    
    print("2. PROBABILIDADES TEÓRICAS:")
    print(f"   P(cara) = {moeda.probabilidade_cara()}")
    print(f"   P(coroa) = {moeda.probabilidade_coroa()}\n")
    
    print("3. SIMULAÇÃO DE LANÇAMENTOS:")
    n_lancamentos = 10
    resultados = moeda.lancar_multiplas_vezes(n_lancamentos)
    print(f"   Resultados de {n_lancamentos} lançamentos: {resultados}")
    
    contagem = Counter(resultados)
    print(f"   Contagem: {dict(contagem)}")
    
    print("\n4. PROBABILIDADES EMPÍRICAS:")
    for evento in moeda.espaco_amostral:
        prob_empirica = moeda.probabilidade_empirica(evento)
        print(f"   P({evento}) = {prob_empirica:.3f}")
    
    print("\n5. SIMULAÇÃO COM MAIS LANÇAMENTOS:")
    n_grande = 1000
    moeda.historico = []  # Limpa o histórico
    resultados_grandes = moeda.lancar_multiplas_vezes(n_grande)
    contagem_grande = Counter(resultados_grandes)
    
    print(f"   Resultados de {n_grande} lançamentos:")
    for evento in moeda.espaco_amostral:
        prob_empirica = moeda.probabilidade_empirica(evento)
        print(f"   P({evento}) = {prob_empirica:.3f}")
    
    print(f"\n   Observação: Com mais lançamentos, a probabilidade empírica")
    print(f"   se aproxima da probabilidade teórica (Lei dos Grandes Números)")
    
    return moeda

if __name__ == "__main__":
    # Executa a demonstração
    moeda = demonstrar_conceitos()
    
    # Plota os resultados
    print("\n6. VISUALIZAÇÃO DOS RESULTADOS:")
    print("   Gerando gráficos...")
    moeda.plotar_resultados(1000)
