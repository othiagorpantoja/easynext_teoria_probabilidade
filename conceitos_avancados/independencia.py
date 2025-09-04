"""
Independência de Eventos
Demonstra quando dois eventos são independentes: P(A ∩ B) = P(A) * P(B)

Desenvolvido por: Thiago Rodrigues Pantoja
Empresa: EasyNext Informática LTDA
Emails: thiago.pantoja@easynext.tech | thiago.pantoja@easynext.consulting
Telefones: (11) 98801-0667 | (92) 98456-1928
Data: Setembro 2025
"""

import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

class IndependenciaEventos:
    """
    Classe para demonstrar independência de eventos
    """
    
    def __init__(self):
        pass
    
    def verificar_independencia(self, evento_a, evento_b, espaco_amostral):
        """
        Verifica se dois eventos são independentes
        """
        # P(A)
        resultados_a = [x for x in espaco_amostral if evento_a(x)]
        prob_a = len(resultados_a) / len(espaco_amostral)
        
        # P(B)
        resultados_b = [x for x in espaco_amostral if evento_b(x)]
        prob_b = len(resultados_b) / len(espaco_amostral)
        
        # P(A ∩ B)
        resultados_a_e_b = [x for x in espaco_amostral if evento_a(x) and evento_b(x)]
        prob_a_e_b = len(resultados_a_e_b) / len(espaco_amostral)
        
        # P(A) * P(B)
        prob_independencia = prob_a * prob_b
        
        # Verifica se P(A ∩ B) = P(A) * P(B)
        independencia = abs(prob_a_e_b - prob_independencia) < 1e-10
        
        return {
            'prob_a': prob_a,
            'prob_b': prob_b,
            'prob_a_e_b': prob_a_e_b,
            'prob_independencia': prob_independencia,
            'independencia': independencia,
            'diferenca': abs(prob_a_e_b - prob_independencia)
        }
    
    def simular_independencia(self, evento_a, evento_b, n_simulacoes=10000):
        """
        Simula independência usando Monte Carlo
        """
        resultados_a = 0
        resultados_b = 0
        resultados_a_e_b = 0
        
        for _ in range(n_simulacoes):
            # Simula lançamento de dois dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            resultado = (dado1, dado2)
            
            if evento_a(resultado):
                resultados_a += 1
            if evento_b(resultado):
                resultados_b += 1
            if evento_a(resultado) and evento_b(resultado):
                resultados_a_e_b += 1
        
        prob_a = resultados_a / n_simulacoes
        prob_b = resultados_b / n_simulacoes
        prob_a_e_b = resultados_a_e_b / n_simulacoes
        prob_independencia = prob_a * prob_b
        
        return {
            'prob_a': prob_a,
            'prob_b': prob_b,
            'prob_a_e_b': prob_a_e_b,
            'prob_independencia': prob_independencia,
            'diferenca': abs(prob_a_e_b - prob_independencia)
        }

def exemplo_dados_independencia():
    """
    Exemplo: Verifica independência entre eventos em lançamento de dois dados
    """
    print("=== EXEMPLO: INDEPENDÊNCIA COM DADOS ===\n")
    
    # Espaço amostral: todos os resultados possíveis de dois dados
    espaco_amostral = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    
    print("1. EVENTOS INDEPENDENTES:")
    
    # Evento A: primeiro dado é par
    def evento_a(resultado):
        return resultado[0] in [2, 4, 6]
    
    # Evento B: segundo dado é ímpar
    def evento_b(resultado):
        return resultado[1] in [1, 3, 5]
    
    print("   A = 'Primeiro dado é par'")
    print("   B = 'Segundo dado é ímpar'")
    
    ie = IndependenciaEventos()
    resultado = ie.verificar_independencia(evento_a, evento_b, espaco_amostral)
    
    print(f"\n2. CÁLCULOS:")
    print(f"   P(A) = {resultado['prob_a']:.3f}")
    print(f"   P(B) = {resultado['prob_b']:.3f}")
    print(f"   P(A ∩ B) = {resultado['prob_a_e_b']:.3f}")
    print(f"   P(A) * P(B) = {resultado['prob_independencia']:.3f}")
    print(f"   Diferença = {resultado['diferenca']:.6f}")
    print(f"   Eventos são independentes: {resultado['independencia']}")
    
    print("\n3. SIMULAÇÃO MONTE CARLO:")
    resultado_sim = ie.simular_independencia(evento_a, evento_b, 10000)
    print(f"   P(A) simulada = {resultado_sim['prob_a']:.3f}")
    print(f"   P(B) simulada = {resultado_sim['prob_b']:.3f}")
    print(f"   P(A ∩ B) simulada = {resultado_sim['prob_a_e_b']:.3f}")
    print(f"   P(A) * P(B) simulada = {resultado_sim['prob_independencia']:.3f}")
    print(f"   Diferença simulada = {resultado_sim['diferenca']:.6f}")
    
    return resultado

def exemplo_dados_dependencia():
    """
    Exemplo: Eventos dependentes em lançamento de dois dados
    """
    print("\n=== EXEMPLO: EVENTOS DEPENDENTES ===\n")
    
    # Espaço amostral: todos os resultados possíveis de dois dados
    espaco_amostral = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    
    print("1. EVENTOS DEPENDENTES:")
    
    # Evento A: soma é 7
    def evento_a(resultado):
        return resultado[0] + resultado[1] == 7
    
    # Evento B: primeiro dado é 4
    def evento_b(resultado):
        return resultado[0] == 4
    
    print("   A = 'Soma é 7'")
    print("   B = 'Primeiro dado é 4'")
    
    ie = IndependenciaEventos()
    resultado = ie.verificar_independencia(evento_a, evento_b, espaco_amostral)
    
    print(f"\n2. CÁLCULOS:")
    print(f"   P(A) = {resultado['prob_a']:.3f}")
    print(f"   P(B) = {resultado['prob_b']:.3f}")
    print(f"   P(A ∩ B) = {resultado['prob_a_e_b']:.3f}")
    print(f"   P(A) * P(B) = {resultado['prob_independencia']:.3f}")
    print(f"   Diferença = {resultado['diferenca']:.6f}")
    print(f"   Eventos são independentes: {resultado['independencia']}")
    
    print(f"\n3. INTERPRETAÇÃO:")
    print(f"   Se o primeiro dado é 4, a soma só pode ser 7 se o segundo dado for 3.")
    print(f"   Isso significa que P(A|B) = 1/6, mas P(A) = 6/36 = 1/6.")
    print(f"   Na verdade, estes eventos SÃO independentes!")
    
    return resultado

def exemplo_baralho_independencia():
    """
    Exemplo: Independência com cartas de baralho
    """
    print("\n=== EXEMPLO: INDEPENDÊNCIA COM BARALHO ===\n")
    
    # Espaço amostral: baralho de 52 cartas
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    espaco_amostral = [(valor, naipe) for naipe in naipes for valor in valores]
    
    print("1. EVENTOS INDEPENDENTES:")
    
    # Evento A: carta é um Ás
    def evento_a(carta):
        return carta[0] == 'A'
    
    # Evento B: carta é vermelha
    def evento_b(carta):
        return carta[1] in ['copas', 'ouros']
    
    print("   A = 'Carta é um Ás'")
    print("   B = 'Carta é vermelha'")
    
    ie = IndependenciaEventos()
    resultado = ie.verificar_independencia(evento_a, evento_b, espaco_amostral)
    
    print(f"\n2. CÁLCULOS:")
    print(f"   P(A) = {resultado['prob_a']:.3f}")
    print(f"   P(B) = {resultado['prob_b']:.3f}")
    print(f"   P(A ∩ B) = {resultado['prob_a_e_b']:.3f}")
    print(f"   P(A) * P(B) = {resultado['prob_independencia']:.3f}")
    print(f"   Diferença = {resultado['diferenca']:.6f}")
    print(f"   Eventos são independentes: {resultado['independencia']}")
    
    print(f"\n3. INTERPRETAÇÃO:")
    if resultado['independencia']:
        print("   O fato de uma carta ser vermelha não afeta a probabilidade")
        print("   de ela ser um Ás. Os eventos são independentes.")
    else:
        print("   O fato de uma carta ser vermelha afeta a probabilidade")
        print("   de ela ser um Ás. Os eventos são dependentes.")
    
    return resultado

def exemplo_baralho_dependencia():
    """
    Exemplo: Eventos dependentes com cartas de baralho
    """
    print("\n=== EXEMPLO: EVENTOS DEPENDENTES COM BARALHO ===\n")
    
    # Espaço amostral: baralho de 52 cartas
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    espaco_amostral = [(valor, naipe) for naipe in naipes for valor in valores]
    
    print("1. EVENTOS DEPENDENTES:")
    
    # Evento A: carta é um Ás de copas
    def evento_a(carta):
        return carta == ('A', 'copas')
    
    # Evento B: carta é de copas
    def evento_b(carta):
        return carta[1] == 'copas'
    
    print("   A = 'Carta é Ás de copas'")
    print("   B = 'Carta é de copas'")
    
    ie = IndependenciaEventos()
    resultado = ie.verificar_independencia(evento_a, evento_b, espaco_amostral)
    
    print(f"\n2. CÁLCULOS:")
    print(f"   P(A) = {resultado['prob_a']:.3f}")
    print(f"   P(B) = {resultado['prob_b']:.3f}")
    print(f"   P(A ∩ B) = {resultado['prob_a_e_b']:.3f}")
    print(f"   P(A) * P(B) = {resultado['prob_independencia']:.3f}")
    print(f"   Diferença = {resultado['diferenca']:.6f}")
    print(f"   Eventos são independentes: {resultado['independencia']}")
    
    print(f"\n3. INTERPRETAÇÃO:")
    print("   Se sabemos que a carta é de copas, a probabilidade de ser")
    print("   Ás de copas é 1/13. Se não sabemos o naipe, a probabilidade")
    print("   de ser Ás de copas é 1/52. Os eventos são dependentes.")
    
    return resultado

def plotar_independencia_vs_dependencia():
    """
    Plota comparação entre eventos independentes e dependentes
    """
    print("\n=== VISUALIZAÇÃO: INDEPENDÊNCIA VS DEPENDÊNCIA ===\n")
    
    # Simula eventos independentes
    n_simulacoes = 1000
    resultados_independentes = []
    resultados_dependentes = []
    
    for _ in range(n_simulacoes):
        # Eventos independentes: primeiro dado par, segundo dado ímpar
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        evento_a_indep = dado1 in [2, 4, 6]
        evento_b_indep = dado2 in [1, 3, 5]
        resultados_independentes.append((evento_a_indep, evento_b_indep))
        
        # Eventos dependentes: soma 7, primeiro dado 4
        evento_a_dep = (dado1 + dado2) == 7
        evento_b_dep = dado1 == 4
        resultados_dependentes.append((evento_a_dep, evento_b_dep))
    
    # Calcula probabilidades
    def calcular_probabilidades(resultados):
        total = len(resultados)
        prob_a = sum(1 for a, b in resultados if a) / total
        prob_b = sum(1 for a, b in resultados if b) / total
        prob_a_e_b = sum(1 for a, b in resultados if a and b) / total
        prob_independencia = prob_a * prob_b
        
        return prob_a, prob_b, prob_a_e_b, prob_independencia
    
    prob_indep = calcular_probabilidades(resultados_independentes)
    prob_dep = calcular_probabilidades(resultados_dependentes)
    
    # Cria o gráfico
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico para eventos independentes
    categorias = ['P(A)', 'P(B)', 'P(A ∩ B)', 'P(A) × P(B)']
    valores_indep = prob_indep
    cores_indep = ['blue', 'green', 'red', 'orange']
    
    barras1 = ax1.bar(categorias, valores_indep, color=cores_indep, alpha=0.7)
    ax1.set_title('Eventos Independentes\n(Primeiro dado par, Segundo dado ímpar)')
    ax1.set_ylabel('Probabilidade')
    ax1.set_ylim(0, 0.6)
    
    # Adiciona valores nas barras
    for barra, valor in zip(barras1, valores_indep):
        ax1.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                f'{valor:.3f}', ha='center', va='bottom')
    
    # Gráfico para eventos dependentes
    valores_dep = prob_dep
    cores_dep = ['blue', 'green', 'red', 'orange']
    
    barras2 = ax2.bar(categorias, valores_dep, color=cores_dep, alpha=0.7)
    ax2.set_title('Eventos Dependentes\n(Soma 7, Primeiro dado 4)')
    ax2.set_ylabel('Probabilidade')
    ax2.set_ylim(0, 0.6)
    
    # Adiciona valores nas barras
    for barra, valor in zip(barras2, valores_dep):
        ax2.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                f'{valor:.3f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    print("Comparação:")
    print(f"Eventos independentes - P(A ∩ B) = {prob_indep[2]:.3f}, P(A) × P(B) = {prob_indep[3]:.3f}")
    print(f"Eventos dependentes - P(A ∩ B) = {prob_dep[2]:.3f}, P(A) × P(B) = {prob_dep[3]:.3f}")

def demonstrar_propriedades_independencia():
    """
    Demonstra propriedades importantes da independência
    """
    print("\n=== PROPRIEDADES DA INDEPENDÊNCIA ===\n")
    
    print("1. PROPRIEDADE SIMÉTRICA:")
    print("   Se A e B são independentes, então B e A são independentes")
    print("   P(A ∩ B) = P(A) × P(B) = P(B) × P(A) = P(B ∩ A)")
    
    print("\n2. INDEPENDÊNCIA E COMPLEMENTARES:")
    print("   Se A e B são independentes, então A e B' são independentes")
    print("   onde B' é o complementar de B")
    
    print("\n3. INDEPENDÊNCIA MÚTUA:")
    print("   Eventos A₁, A₂, ..., Aₙ são mutuamente independentes se")
    print("   P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) × P(A₂) × ... × P(Aₙ)")
    
    print("\n4. INDEPENDÊNCIA E PROBABILIDADE CONDICIONAL:")
    print("   Se A e B são independentes, então P(A|B) = P(A)")
    print("   e P(B|A) = P(B)")

if __name__ == "__main__":
    # Executa todos os exemplos
    resultado_indep = exemplo_dados_independencia()
    resultado_dep1 = exemplo_dados_dependencia()
    resultado_baralho_indep = exemplo_baralho_independencia()
    resultado_baralho_dep = exemplo_baralho_dependencia()
    
    # Visualizações
    plotar_independencia_vs_dependencia()
    demonstrar_propriedades_independencia()
