"""
Redes Bayesianas
Demonstra como usar probabilidade em redes Bayesianas para inferência
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import random

class RedeBayesiana:
    """
    Classe para representar e trabalhar com redes Bayesianas
    """
    
    def __init__(self):
        self.nos = {}
        self.arestas = defaultdict(list)
        self.tabelas_probabilidade = {}
    
    def adicionar_no(self, nome, valores_possiveis, pais=None):
        """
        Adiciona um nó à rede
        """
        self.nos[nome] = {
            'valores': valores_possiveis,
            'pais': pais or []
        }
        
        # Adiciona arestas dos pais para este nó
        for pai in (pais or []):
            self.arestas[pai].append(nome)
    
    def definir_tabela_probabilidade(self, no, tabela):
        """
        Define a tabela de probabilidade condicional para um nó
        """
        self.tabelas_probabilidade[no] = tabela
    
    def calcular_probabilidade_conjunta(self, evidencia):
        """
        Calcula a probabilidade conjunta P(X1, X2, ..., Xn)
        """
        probabilidade = 1.0
        
        for no in self.nos:
            if no in evidencia:
                valor = evidencia[no]
                pais = self.nos[no]['pais']
                
                # Pega a probabilidade condicional
                if pais:
                    # P(no | pais)
                    chave_pais = tuple(evidencia[pai] for pai in pais)
                    prob_condicional = self.tabelas_probabilidade[no][chave_pais][valor]
                else:
                    # P(no) - probabilidade marginal
                    prob_condicional = self.tabelas_probabilidade[no][valor]
                
                probabilidade *= prob_condicional
        
        return probabilidade
    
    def inferencia_por_enumeration(self, variavel, evidencia):
        """
        Realiza inferência usando o algoritmo de enumeração
        """
        # Encontra todas as variáveis não observadas
        variaveis_nao_observadas = [v for v in self.nos if v not in evidencia and v != variavel]
        
        # Calcula P(variavel | evidencia)
        probabilidades = {}
        
        for valor in self.nos[variavel]['valores']:
            evidencia_completa = evidencia.copy()
            evidencia_completa[variavel] = valor
            
            # Soma sobre todas as combinações de variáveis não observadas
            prob = 0.0
            for combinacao in self._gerar_combinacoes(variaveis_nao_observadas):
                evidencia_final = evidencia_completa.copy()
                evidencia_final.update(combinacao)
                prob += self.calcular_probabilidade_conjunta(evidencia_final)
            
            probabilidades[valor] = prob
        
        # Normaliza as probabilidades
        total = sum(probabilidades.values())
        if total > 0:
            for valor in probabilidades:
                probabilidades[valor] /= total
        
        return probabilidades
    
    def _gerar_combinacoes(self, variaveis):
        """
        Gera todas as combinações possíveis de valores para as variáveis
        """
        if not variaveis:
            return [{}]
        
        primeira_variavel = variaveis[0]
        resto_variaveis = variaveis[1:]
        
        combinacoes_resto = self._gerar_combinacoes(resto_variaveis)
        combinacoes = []
        
        for valor in self.nos[primeira_variavel]['valores']:
            for combinacao_resto in combinacoes_resto:
                nova_combinacao = {primeira_variavel: valor}
                nova_combinacao.update(combinacao_resto)
                combinacoes.append(nova_combinacao)
        
        return combinacoes

def exemplo_rede_simples():
    """
    Exemplo de uma rede Bayesiana simples: Chuva -> Grama Molhada
    """
    print("=== EXEMPLO: REDE BAYESIANA SIMPLES ===\n")
    
    # Cria a rede
    rede = RedeBayesiana()
    
    # Adiciona nós
    rede.adicionar_no('Chuva', ['sim', 'não'])
    rede.adicionar_no('GramaMolhada', ['sim', 'não'], ['Chuva'])
    
    # Define tabelas de probabilidade
    # P(Chuva)
    rede.definir_tabela_probabilidade('Chuva', {
        'sim': 0.2,
        'não': 0.8
    })
    
    # P(GramaMolhada | Chuva)
    rede.definir_tabela_probabilidade('GramaMolhada', {
        ('sim',): {'sim': 0.9, 'não': 0.1},  # Se chove, grama molhada com 90%
        ('não',): {'sim': 0.1, 'não': 0.9}   # Se não chove, grama molhada com 10%
    })
    
    print("1. ESTRUTURA DA REDE:")
    print("   Chuva -> GramaMolhada")
    print("   P(Chuva = sim) = 0.2")
    print("   P(GramaMolhada = sim | Chuva = sim) = 0.9")
    print("   P(GramaMolhada = sim | Chuva = não) = 0.1")
    
    print("\n2. INFERÊNCIA:")
    
    # P(Chuva | GramaMolhada = sim)
    evidencia = {'GramaMolhada': 'sim'}
    probabilidades = rede.inferencia_por_enumeration('Chuva', evidencia)
    
    print(f"   P(Chuva = sim | GramaMolhada = sim) = {probabilidades['sim']:.3f}")
    print(f"   P(Chuva = não | GramaMolhada = sim) = {probabilidades['não']:.3f}")
    
    # P(GramaMolhada | Chuva = sim)
    evidencia = {'Chuva': 'sim'}
    probabilidades = rede.inferencia_por_enumeration('GramaMolhada', evidencia)
    
    print(f"   P(GramaMolhada = sim | Chuva = sim) = {probabilidades['sim']:.3f}")
    print(f"   P(GramaMolhada = não | Chuva = sim) = {probabilidades['não']:.3f}")
    
    return rede

def exemplo_rede_medica():
    """
    Exemplo de rede Bayesiana para diagnóstico médico
    """
    print("\n=== EXEMPLO: REDE BAYESIANA MÉDICA ===\n")
    
    # Cria a rede
    rede = RedeBayesiana()
    
    # Adiciona nós
    rede.adicionar_no('Doenca', ['sim', 'não'])
    rede.adicionar_no('Sintoma1', ['sim', 'não'], ['Doenca'])
    rede.adicionar_no('Sintoma2', ['sim', 'não'], ['Doenca'])
    rede.adicionar_no('Teste', ['positivo', 'negativo'], ['Doenca'])
    
    # Define tabelas de probabilidade
    # P(Doenca)
    rede.definir_tabela_probabilidade('Doenca', {
        'sim': 0.01,  # 1% da população tem a doença
        'não': 0.99
    })
    
    # P(Sintoma1 | Doenca)
    rede.definir_tabela_probabilidade('Sintoma1', {
        ('sim',): {'sim': 0.8, 'não': 0.2},   # 80% dos doentes têm sintoma1
        ('não',): {'sim': 0.1, 'não': 0.9}    # 10% dos não-doentes têm sintoma1
    })
    
    # P(Sintoma2 | Doenca)
    rede.definir_tabela_probabilidade('Sintoma2', {
        ('sim',): {'sim': 0.6, 'não': 0.4},   # 60% dos doentes têm sintoma2
        ('não',): {'sim': 0.05, 'não': 0.95}  # 5% dos não-doentes têm sintoma2
    })
    
    # P(Teste | Doenca)
    rede.definir_tabela_probabilidade('Teste', {
        ('sim',): {'positivo': 0.95, 'negativo': 0.05},   # 95% dos doentes testam positivo
        ('não',): {'positivo': 0.02, 'negativo': 0.98}    # 2% dos não-doentes testam positivo
    })
    
    print("1. ESTRUTURA DA REDE:")
    print("   Doenca -> Sintoma1")
    print("   Doenca -> Sintoma2")
    print("   Doenca -> Teste")
    
    print("\n2. INFERÊNCIA COM EVIDÊNCIA PARCIAL:")
    
    # P(Doenca | Sintoma1 = sim)
    evidencia = {'Sintoma1': 'sim'}
    probabilidades = rede.inferencia_por_enumeration('Doenca', evidencia)
    
    print(f"   P(Doenca = sim | Sintoma1 = sim) = {probabilidades['sim']:.3f}")
    print(f"   P(Doenca = não | Sintoma1 = sim) = {probabilidades['não']:.3f}")
    
    # P(Doenca | Sintoma1 = sim, Sintoma2 = sim)
    evidencia = {'Sintoma1': 'sim', 'Sintoma2': 'sim'}
    probabilidades = rede.inferencia_por_enumeration('Doenca', evidencia)
    
    print(f"   P(Doenca = sim | Sintoma1 = sim, Sintoma2 = sim) = {probabilidades['sim']:.3f}")
    print(f"   P(Doenca = não | Sintoma1 = sim, Sintoma2 = sim) = {probabilidades['não']:.3f}")
    
    # P(Doenca | Teste = positivo)
    evidencia = {'Teste': 'positivo'}
    probabilidades = rede.inferencia_por_enumeration('Doenca', evidencia)
    
    print(f"   P(Doenca = sim | Teste = positivo) = {probabilidades['sim']:.3f}")
    print(f"   P(Doenca = não | Teste = positivo) = {probabilidades['não']:.3f}")
    
    return rede

def exemplo_rede_weather():
    """
    Exemplo de rede Bayesiana para previsão do tempo
    """
    print("\n=== EXEMPLO: REDE BAYESIANA DO TEMPO ===\n")
    
    # Cria a rede
    rede = RedeBayesiana()
    
    # Adiciona nós
    rede.adicionar_no('Tempo', ['ensolarado', 'nublado', 'chuvoso'])
    rede.adicionar_no('Umidade', ['alta', 'normal'], ['Tempo'])
    rede.adicionar_no('Vento', ['forte', 'fraco'], ['Tempo'])
    rede.adicionar_no('JogarTenis', ['sim', 'não'], ['Tempo', 'Umidade', 'Vento'])
    
    # Define tabelas de probabilidade
    # P(Tempo)
    rede.definir_tabela_probabilidade('Tempo', {
        'ensolarado': 0.5,
        'nublado': 0.3,
        'chuvoso': 0.2
    })
    
    # P(Umidade | Tempo)
    rede.definir_tabela_probabilidade('Umidade', {
        ('ensolarado',): {'alta': 0.3, 'normal': 0.7},
        ('nublado',): {'alta': 0.4, 'normal': 0.6},
        ('chuvoso',): {'alta': 0.8, 'normal': 0.2}
    })
    
    # P(Vento | Tempo)
    rede.definir_tabela_probabilidade('Vento', {
        ('ensolarado',): {'forte': 0.2, 'fraco': 0.8},
        ('nublado',): {'forte': 0.3, 'fraco': 0.7},
        ('chuvoso',): {'forte': 0.6, 'fraco': 0.4}
    })
    
    # P(JogarTenis | Tempo, Umidade, Vento)
    rede.definir_tabela_probabilidade('JogarTenis', {
        ('ensolarado', 'alta', 'forte'): {'sim': 0.3, 'não': 0.7},
        ('ensolarado', 'alta', 'fraco'): {'sim': 0.5, 'não': 0.5},
        ('ensolarado', 'normal', 'forte'): {'sim': 0.7, 'não': 0.3},
        ('ensolarado', 'normal', 'fraco'): {'sim': 0.9, 'não': 0.1},
        ('nublado', 'alta', 'forte'): {'sim': 0.2, 'não': 0.8},
        ('nublado', 'alta', 'fraco'): {'sim': 0.4, 'não': 0.6},
        ('nublado', 'normal', 'forte'): {'sim': 0.6, 'não': 0.4},
        ('nublado', 'normal', 'fraco'): {'sim': 0.8, 'não': 0.2},
        ('chuvoso', 'alta', 'forte'): {'sim': 0.1, 'não': 0.9},
        ('chuvoso', 'alta', 'fraco'): {'sim': 0.2, 'não': 0.8},
        ('chuvoso', 'normal', 'forte'): {'sim': 0.3, 'não': 0.7},
        ('chuvoso', 'normal', 'fraco'): {'sim': 0.4, 'não': 0.6}
    })
    
    print("1. ESTRUTURA DA REDE:")
    print("   Tempo -> Umidade")
    print("   Tempo -> Vento")
    print("   Tempo -> JogarTenis")
    print("   Umidade -> JogarTenis")
    print("   Vento -> JogarTenis")
    
    print("\n2. INFERÊNCIA:")
    
    # P(JogarTenis | Tempo = ensolarado)
    evidencia = {'Tempo': 'ensolarado'}
    probabilidades = rede.inferencia_por_enumeration('JogarTenis', evidencia)
    
    print(f"   P(JogarTenis = sim | Tempo = ensolarado) = {probabilidades['sim']:.3f}")
    print(f"   P(JogarTenis = não | Tempo = ensolarado) = {probabilidades['não']:.3f}")
    
    # P(JogarTenis | Tempo = ensolarado, Umidade = alta)
    evidencia = {'Tempo': 'ensolarado', 'Umidade': 'alta'}
    probabilidades = rede.inferencia_por_enumeration('JogarTenis', evidencia)
    
    print(f"   P(JogarTenis = sim | Tempo = ensolarado, Umidade = alta) = {probabilidades['sim']:.3f}")
    print(f"   P(JogarTenis = não | Tempo = ensolarado, Umidade = alta) = {probabilidades['não']:.3f}")
    
    return rede

def plotar_rede_bayesiana():
    """
    Plota a estrutura de uma rede Bayesiana
    """
    print("\n=== VISUALIZAÇÃO: ESTRUTURA DA REDE ===\n")
    
    # Cria uma rede simples para visualização
    rede = RedeBayesiana()
    rede.adicionar_no('A', ['sim', 'não'])
    rede.adicionar_no('B', ['sim', 'não'], ['A'])
    rede.adicionar_no('C', ['sim', 'não'], ['A'])
    rede.adicionar_no('D', ['sim', 'não'], ['B', 'C'])
    
    # Plota a estrutura
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Posições dos nós
    posicoes = {
        'A': (0.5, 0.8),
        'B': (0.2, 0.4),
        'C': (0.8, 0.4),
        'D': (0.5, 0.1)
    }
    
    # Desenha os nós
    for no, pos in posicoes.items():
        circle = plt.Circle(pos, 0.1, color='lightblue', ec='black')
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], no, ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Desenha as arestas
    arestas = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D')
    ]
    
    for pai, filho in arestas:
        pos_pai = posicoes[pai]
        pos_filho = posicoes[filho]
        ax.arrow(pos_pai[0], pos_pai[1]-0.1, 
                pos_filho[0]-pos_pai[0], pos_filho[1]-pos_pai[1]+0.1,
                head_width=0.03, head_length=0.03, fc='black', ec='black')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Estrutura de uma Rede Bayesiana', fontsize=16, fontweight='bold')
    
    plt.show()
    
    print("A rede mostra as dependências entre as variáveis:")
    print("- A influencia B e C")
    print("- B e C influenciam D")
    print("- Cada nó tem uma tabela de probabilidade condicional")

def demonstrar_ventilacao():
    """
    Demonstra o algoritmo de ventilação para inferência em redes Bayesianas
    """
    print("\n=== ALGORITMO DE VENTILAÇÃO ===\n")
    
    print("1. CONCEITO:")
    print("   O algoritmo de ventilação é uma técnica eficiente para")
    print("   inferência em redes Bayesianas, evitando a enumeração")
    print("   de todas as possibilidades.")
    
    print("\n2. VANTAGENS:")
    print("   - Mais eficiente que enumeração")
    print("   - Funciona bem com redes grandes")
    print("   - Pode ser implementado de forma distribuída")
    
    print("\n3. LIMITAÇÕES:")
    print("   - Complexidade de implementação")
    print("   - Pode não convergir em alguns casos")
    print("   - Requer estrutura de árvore ou grafo cordal")

if __name__ == "__main__":
    # Executa todos os exemplos
    rede_simples = exemplo_rede_simples()
    rede_medica = exemplo_rede_medica()
    rede_weather = exemplo_rede_weather()
    
    # Visualizações
    plotar_rede_bayesiana()
    demonstrar_ventilacao()
