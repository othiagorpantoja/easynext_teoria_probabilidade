"""
Exemplo básico: Sorteio de Cartas de Baralho
Demonstra espaço amostral complexo e eventos
"""

import random
import matplotlib.pyplot as plt
from collections import Counter

class Baralho:
    """
    Classe que representa um baralho de 52 cartas
    """
    
    def __init__(self):
        self.naipes = ['copas', 'ouros', 'espadas', 'paus']
        self.valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cartas = []
        self.cartas_restantes = []
        self.cartas_sacadas = []
        
        # Cria o baralho
        for naipe in self.naipes:
            for valor in self.valores:
                self.cartas.append((valor, naipe))
        
        self.cartas_restantes = self.cartas.copy()
    
    def embaralhar(self):
        """
        Embaralha o baralho
        """
        random.shuffle(self.cartas_restantes)
    
    def sacar_carta(self):
        """
        Saca uma carta do baralho
        """
        if not self.cartas_restantes:
            raise ValueError("Baralho vazio!")
        
        carta = self.cartas_restantes.pop()
        self.cartas_sacadas.append(carta)
        return carta
    
    def sacar_multiplas_cartas(self, n):
        """
        Saca n cartas do baralho
        """
        cartas = []
        for _ in range(n):
            cartas.append(self.sacar_carta())
        return cartas
    
    def resetar_baralho(self):
        """
        Reseta o baralho para o estado inicial
        """
        self.cartas_restantes = self.cartas.copy()
        self.cartas_sacadas = []
        self.embaralhar()
    
    def probabilidade_evento(self, evento):
        """
        Calcula a probabilidade de um evento específico
        evento: função que retorna True se a carta satisfaz o evento
        """
        cartas_favoraveis = [carta for carta in self.cartas if evento(carta)]
        return len(cartas_favoraveis) / len(self.cartas)
    
    def probabilidade_empirica(self, evento, n_sorteios=None):
        """
        Calcula a probabilidade empírica de um evento
        """
        if n_sorteios is None:
            n_sorteios = len(self.cartas_sacadas)
        
        if n_sorteios == 0:
            return 0
        
        # Usa apenas os últimos n_sorteios
        cartas_recentes = self.cartas_sacadas[-n_sorteios:]
        
        # Conta quantas vezes o evento ocorreu
        ocorrencias = sum(1 for carta in cartas_recentes if evento(carta))
        
        return ocorrencias / n_sorteios

def demonstrar_eventos_baralho():
    """
    Demonstra diferentes eventos com um baralho
    """
    print("=== DEMONSTRAÇÃO: BARALHO DE CARTAS ===\n")
    
    # Cria um baralho
    baralho = Baralho()
    
    print("1. ESPAÇO AMOSTRAL:")
    print(f"   Número total de cartas: {len(baralho.cartas)}")
    print(f"   Naipes: {baralho.naipes}")
    print(f"   Valores: {baralho.valores}")
    print(f"   Primeiras 10 cartas: {baralho.cartas[:10]}")
    
    print("\n2. EVENTOS E SUAS PROBABILIDADES:")
    
    # Evento: sair um Ás
    def evento_as(carta):
        return carta[0] == 'A'
    
    prob_as = baralho.probabilidade_evento(evento_as)
    print(f"   A = 'Sair um Ás'")
    print(f"   P(A) = {prob_as:.3f}")
    
    # Evento: sair uma carta de copas
    def evento_copas(carta):
        return carta[1] == 'copas'
    
    prob_copas = baralho.probabilidade_evento(evento_copas)
    print(f"   B = 'Sair carta de copas'")
    print(f"   P(B) = {prob_copas:.3f}")
    
    # Evento: sair uma figura (J, Q, K)
    def evento_figura(carta):
        return carta[0] in ['J', 'Q', 'K']
    
    prob_figura = baralho.probabilidade_evento(evento_figura)
    print(f"   C = 'Sair uma figura (J, Q, K)'")
    print(f"   P(C) = {prob_figura:.3f}")
    
    # Evento: sair uma carta vermelha
    def evento_vermelha(carta):
        return carta[1] in ['copas', 'ouros']
    
    prob_vermelha = baralho.probabilidade_evento(evento_vermelha)
    print(f"   D = 'Sair carta vermelha'")
    print(f"   P(D) = {prob_vermelha:.3f}")
    
    # Evento: sair um Ás de copas
    def evento_as_copas(carta):
        return carta == ('A', 'copas')
    
    prob_as_copas = baralho.probabilidade_evento(evento_as_copas)
    print(f"   E = 'Sair Ás de copas'")
    print(f"   P(E) = {prob_as_copas:.3f}")
    
    print("\n3. SIMULAÇÃO DE SORTEIOS:")
    baralho.resetar_baralho()
    n_sorteios = 20  # Sorteia 20 cartas
    cartas_sacadas = baralho.sacar_multiplas_cartas(n_sorteios)
    
    print(f"   Primeiras 10 cartas sacadas: {cartas_sacadas[:10]}")
    
    print("\n4. PROBABILIDADES EMPÍRICAS:")
    print(f"   P(Ás) = {baralho.probabilidade_empirica(evento_as):.3f}")
    print(f"   P(copas) = {baralho.probabilidade_empirica(evento_copas):.3f}")
    print(f"   P(figura) = {baralho.probabilidade_empirica(evento_figura):.3f}")
    print(f"   P(vermelha) = {baralho.probabilidade_empirica(evento_vermelha):.3f}")
    print(f"   P(Ás de copas) = {baralho.probabilidade_empirica(evento_as_copas):.3f}")
    
    return baralho

def demonstrar_sorteio_sem_reposicao():
    """
    Demonstra como a probabilidade muda quando não há reposição
    """
    print("\n=== DEMONSTRAÇÃO: SORTEIO SEM REPOSIÇÃO ===\n")
    
    baralho = Baralho()
    
    print("1. PROBABILIDADE DE SORTEAR ÁS:")
    print("   Primeira carta:")
    
    # Primeira carta
    baralho.resetar_baralho()
    primeira_carta = baralho.sacar_carta()
    print(f"   Carta sacada: {primeira_carta}")
    
    # Probabilidade de Ás na segunda carta
    def evento_as(carta):
        return carta[0] == 'A'
    
    # Conta quantos Áses restam
    ases_restantes = sum(1 for carta in baralho.cartas_restantes if evento_as(carta))
    prob_segunda_carta_as = ases_restantes / len(baralho.cartas_restantes)
    
    print(f"   Áses restantes: {ases_restantes}")
    print(f"   Cartas restantes: {len(baralho.cartas_restantes)}")
    print(f"   P(segunda carta ser Ás) = {prob_segunda_carta_as:.3f}")
    
    if primeira_carta[0] == 'A':
        print("   A primeira carta foi um Ás, então a probabilidade diminuiu!")
    else:
        print("   A primeira carta não foi um Ás, então a probabilidade aumentou!")
    
    print("\n2. SIMULAÇÃO DE MÚLTIPLOS SORTEIOS:")
    baralho.resetar_baralho()
    
    probabilidades_as = []
    cartas_sacadas = []
    
    for i in range(10):
        carta = baralho.sacar_carta()
        cartas_sacadas.append(carta)
        
        # Calcula probabilidade de Ás nas cartas restantes
        ases_restantes = sum(1 for carta in baralho.cartas_restantes if evento_as(carta))
        prob_as_restante = ases_restantes / len(baralho.cartas_restantes) if baralho.cartas_restantes else 0
        probabilidades_as.append(prob_as_restante)
        
        print(f"   Carta {i+1}: {carta} | P(próximo Ás) = {prob_as_restante:.3f}")
    
    return cartas_sacadas, probabilidades_as

def plotar_distribuicao_naipes():
    """
    Plota a distribuição dos naipes em múltiplos sorteios
    """
    print("\n=== VISUALIZAÇÃO: DISTRIBUIÇÃO DE NAIPES ===\n")
    
    baralho = Baralho()
    n_simulacoes = 1000
    resultados_naipes = []
    
    for _ in range(n_simulacoes):
        baralho.resetar_baralho()
        carta = baralho.sacar_carta()
        resultados_naipes.append(carta[1])
    
    # Conta os resultados
    contagem_naipes = Counter(resultados_naipes)
    
    # Cria o gráfico
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de barras
    naipes = list(contagem_naipes.keys())
    valores = list(contagem_naipes.values())
    cores = ['red', 'gold', 'black', 'green']
    
    barras = ax1.bar(naipes, valores, color=cores, alpha=0.7)
    ax1.set_title(f'Distribuição de Naipes em {n_simulacoes} sorteios')
    ax1.set_ylabel('Frequência')
    ax1.set_xlabel('Naipe')
    
    # Adiciona valores nas barras
    for barra, valor in zip(barras, valores):
        ax1.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                str(valor), ha='center', va='bottom')
    
    # Gráfico de pizza
    ax2.pie(valores, labels=naipes, colors=cores, autopct='%1.1f%%', startangle=90)
    ax2.set_title('Proporção de Naipes')
    
    plt.tight_layout()
    plt.show()
    
    print(f"Distribuição observada: {dict(contagem_naipes)}")
    print("Teoricamente, cada naipe deveria aparecer 25% das vezes")

if __name__ == "__main__":
    # Executa as demonstrações
    baralho = demonstrar_eventos_baralho()
    
    # Demonstra sorteio sem reposição
    cartas, probs = demonstrar_sorteio_sem_reposicao()
    
    # Plota distribuição de naipes
    plotar_distribuicao_naipes()
