"""
Probabilidade Condicional
Demonstra como calcular P(A|B) = P(A ∩ B) / P(B)

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

class ProbabilidadeCondicional:
    """
    Classe para demonstrar probabilidade condicional
    """
    
    def __init__(self):
        pass
    
    def calcular_probabilidade_condicional(self, evento_a, evento_b, espaco_amostral):
        """
        Calcula P(A|B) = P(A ∩ B) / P(B)
        """
        # P(A ∩ B)
        intersecao = [x for x in espaco_amostral if evento_a(x) and evento_b(x)]
        prob_intersecao = len(intersecao) / len(espaco_amostral)
        
        # P(B)
        evento_b_resultados = [x for x in espaco_amostral if evento_b(x)]
        prob_b = len(evento_b_resultados) / len(espaco_amostral)
        
        if prob_b == 0:
            return 0
        
        return prob_intersecao / prob_b
    
    def simular_probabilidade_condicional(self, evento_a, evento_b, n_simulacoes=10000):
        """
        Simula probabilidade condicional usando Monte Carlo
        """
        # Simula lançamentos de dois dados
        resultados_a_dado_b = []
        total_evento_b = 0
        
        for _ in range(n_simulacoes):
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            resultado = (dado1, dado2)
            
            if evento_b(resultado):
                total_evento_b += 1
                if evento_a(resultado):
                    resultados_a_dado_b.append(resultado)
        
        if total_evento_b == 0:
            return 0
        
        return len(resultados_a_dado_b) / total_evento_b

def exemplo_dados_soma():
    """
    Exemplo: Probabilidade de soma ser 7 dado que o primeiro dado é 4
    """
    print("=== EXEMPLO: PROBABILIDADE CONDICIONAL COM DADOS ===\n")
    
    # Espaço amostral: todos os resultados possíveis de dois dados
    espaco_amostral = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    
    # Evento A: soma é 7
    def evento_a(resultado):
        return resultado[0] + resultado[1] == 7
    
    # Evento B: primeiro dado é 4
    def evento_b(resultado):
        return resultado[0] == 4
    
    print("1. DEFINIÇÃO DOS EVENTOS:")
    print("   A = 'Soma é 7'")
    print("   B = 'Primeiro dado é 4'")
    print("   Queremos calcular P(A|B)")
    
    print("\n2. CÁLCULO TEÓRICO:")
    
    # Resultados onde B ocorre
    resultados_b = [r for r in espaco_amostral if evento_b(r)]
    print(f"   Resultados onde B ocorre: {resultados_b}")
    print(f"   P(B) = {len(resultados_b)}/{len(espaco_amostral)} = {len(resultados_b)/len(espaco_amostral):.3f}")
    
    # Resultados onde A e B ocorrem
    resultados_a_e_b = [r for r in espaco_amostral if evento_a(r) and evento_b(r)]
    print(f"   Resultados onde A e B ocorrem: {resultados_a_e_b}")
    print(f"   P(A ∩ B) = {len(resultados_a_e_b)}/{len(espaco_amostral)} = {len(resultados_a_e_b)/len(espaco_amostral):.3f}")
    
    # Probabilidade condicional
    prob_condicional = len(resultados_a_e_b) / len(resultados_b)
    print(f"   P(A|B) = P(A ∩ B) / P(B) = {len(resultados_a_e_b)}/{len(resultados_b)} = {prob_condicional:.3f}")
    
    print("\n3. SIMULAÇÃO MONTE CARLO:")
    pc = ProbabilidadeCondicional()
    prob_simulada = pc.simular_probabilidade_condicional(evento_a, evento_b, 10000)
    print(f"   P(A|B) simulada = {prob_simulada:.3f}")
    
    return prob_condicional, prob_simulada

def exemplo_baralho_cartas():
    """
    Exemplo: Probabilidade de sair Ás dado que a carta é vermelha
    """
    print("\n=== EXEMPLO: PROBABILIDADE CONDICIONAL COM BARALHO ===\n")
    
    # Espaço amostral: baralho de 52 cartas
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    espaco_amostral = [(valor, naipe) for naipe in naipes for valor in valores]
    
    # Evento A: carta é um Ás
    def evento_a(carta):
        return carta[0] == 'A'
    
    # Evento B: carta é vermelha (copas ou ouros)
    def evento_b(carta):
        return carta[1] in ['copas', 'ouros']
    
    print("1. DEFINIÇÃO DOS EVENTOS:")
    print("   A = 'Carta é um Ás'")
    print("   B = 'Carta é vermelha'")
    print("   Queremos calcular P(A|B)")
    
    print("\n2. CÁLCULO TEÓRICO:")
    
    # P(A)
    ases = [carta for carta in espaco_amostral if evento_a(carta)]
    prob_a = len(ases) / len(espaco_amostral)
    print(f"   P(A) = {len(ases)}/{len(espaco_amostral)} = {prob_a:.3f}")
    
    # P(B)
    cartas_vermelhas = [carta for carta in espaco_amostral if evento_b(carta)]
    prob_b = len(cartas_vermelhas) / len(espaco_amostral)
    print(f"   P(B) = {len(cartas_vermelhas)}/{len(espaco_amostral)} = {prob_b:.3f}")
    
    # P(A ∩ B)
    ases_vermelhos = [carta for carta in espaco_amostral if evento_a(carta) and evento_b(carta)]
    prob_a_e_b = len(ases_vermelhos) / len(espaco_amostral)
    print(f"   P(A ∩ B) = {len(ases_vermelhos)}/{len(espaco_amostral)} = {prob_a_e_b:.3f}")
    
    # P(A|B)
    prob_condicional = len(ases_vermelhos) / len(cartas_vermelhas)
    print(f"   P(A|B) = P(A ∩ B) / P(B) = {len(ases_vermelhos)}/{len(cartas_vermelhas)} = {prob_condicional:.3f}")
    
    print(f"\n   Áses vermelhos: {ases_vermelhos}")
    
    return prob_condicional

def exemplo_doenca_teste():
    """
    Exemplo clássico: Teste de doença com falsos positivos e negativos
    """
    print("\n=== EXEMPLO: TESTE DE DOENÇA ===\n")
    
    # Parâmetros do problema
    prevalencia = 0.01  # 1% da população tem a doença
    sensibilidade = 0.95  # 95% dos doentes testam positivo
    especificidade = 0.98  # 98% dos não-doentes testam negativo
    
    print("1. PARÂMETROS DO PROBLEMA:")
    print(f"   Prevalência da doença: {prevalencia:.1%}")
    print(f"   Sensibilidade do teste: {sensibilidade:.1%}")
    print(f"   Especificidade do teste: {especificidade:.1%}")
    
    print("\n2. CÁLCULO DE PROBABILIDADES:")
    
    # P(doença) = 0.01
    prob_doenca = prevalencia
    print(f"   P(doença) = {prob_doenca:.3f}")
    
    # P(teste positivo | doença) = 0.95
    prob_positivo_dado_doenca = sensibilidade
    print(f"   P(teste positivo | doença) = {prob_positivo_dado_doenca:.3f}")
    
    # P(teste negativo | não doença) = 0.98
    prob_negativo_dado_nao_doenca = especificidade
    print(f"   P(teste negativo | não doença) = {prob_negativo_dado_nao_doenca:.3f}")
    
    # P(teste positivo | não doença) = 1 - 0.98 = 0.02
    prob_positivo_dado_nao_doenca = 1 - especificidade
    print(f"   P(teste positivo | não doença) = {prob_positivo_dado_nao_doenca:.3f}")
    
    # P(teste positivo) = P(teste positivo | doença) * P(doença) + P(teste positivo | não doença) * P(não doença)
    prob_positivo = (prob_positivo_dado_doenca * prob_doenca + 
                    prob_positivo_dado_nao_doenca * (1 - prob_doenca))
    print(f"   P(teste positivo) = {prob_positivo:.3f}")
    
    # P(doença | teste positivo) usando Teorema de Bayes
    prob_doenca_dado_positivo = (prob_positivo_dado_doenca * prob_doenca) / prob_positivo
    print(f"   P(doença | teste positivo) = {prob_doenca_dado_positivo:.3f}")
    
    print(f"\n3. INTERPRETAÇÃO:")
    print(f"   Mesmo com um teste muito bom (95% sensibilidade, 98% especificidade),")
    print(f"   a probabilidade de ter a doença dado um teste positivo é apenas {prob_doenca_dado_positivo:.1%}")
    print(f"   Isso acontece porque a doença é rara (prevalência de 1%)")
    
    return prob_doenca_dado_positivo

def plotar_probabilidade_condicional():
    """
    Plota como a probabilidade condicional varia com diferentes parâmetros
    """
    print("\n=== VISUALIZAÇÃO: VARIAÇÃO DA PROBABILIDADE CONDICIONAL ===\n")
    
    # Varia a prevalência da doença
    prevalencias = np.linspace(0.001, 0.1, 100)
    sensibilidade = 0.95
    especificidade = 0.98
    
    probabilidades_condicionais = []
    
    for prevalencia in prevalencias:
        prob_positivo = (sensibilidade * prevalencia + 
                        (1 - especificidade) * (1 - prevalencia))
        prob_condicional = (sensibilidade * prevalencia) / prob_positivo
        probabilidades_condicionais.append(prob_condicional)
    
    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(prevalencias * 100, probabilidades_condicionais, 'b-', linewidth=2)
    plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='50%')
    plt.xlabel('Prevalência da Doença (%)')
    plt.ylabel('P(doença | teste positivo)')
    plt.title('Probabilidade Condicional vs Prevalência da Doença')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    print("O gráfico mostra como a probabilidade condicional aumenta")
    print("conforme a prevalência da doença aumenta.")

def demonstrar_regra_multiplicacao():
    """
    Demonstra a regra da multiplicação: P(A ∩ B) = P(A|B) * P(B)
    """
    print("\n=== REGRA DA MULTIPLICAÇÃO ===\n")
    
    # Exemplo com dois dados
    espaco_amostral = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    
    # Evento A: segundo dado é 6
    def evento_a(resultado):
        return resultado[1] == 6
    
    # Evento B: primeiro dado é par
    def evento_b(resultado):
        return resultado[0] in [2, 4, 6]
    
    print("1. EVENTOS:")
    print("   A = 'Segundo dado é 6'")
    print("   B = 'Primeiro dado é par'")
    print("   Queremos calcular P(A ∩ B)")
    
    print("\n2. CÁLCULO DIRETO:")
    resultados_a_e_b = [r for r in espaco_amostral if evento_a(r) and evento_b(r)]
    prob_direta = len(resultados_a_e_b) / len(espaco_amostral)
    print(f"   P(A ∩ B) = {len(resultados_a_e_b)}/{len(espaco_amostral)} = {prob_direta:.3f}")
    
    print("\n3. CÁLCULO USANDO REGRA DA MULTIPLICAÇÃO:")
    
    # P(B)
    resultados_b = [r for r in espaco_amostral if evento_b(r)]
    prob_b = len(resultados_b) / len(espaco_amostral)
    print(f"   P(B) = {len(resultados_b)}/{len(espaco_amostral)} = {prob_b:.3f}")
    
    # P(A|B)
    pc = ProbabilidadeCondicional()
    prob_a_dado_b = pc.calcular_probabilidade_condicional(evento_a, evento_b, espaco_amostral)
    print(f"   P(A|B) = {prob_a_dado_b:.3f}")
    
    # P(A ∩ B) = P(A|B) * P(B)
    prob_multiplicacao = prob_a_dado_b * prob_b
    print(f"   P(A ∩ B) = P(A|B) * P(B) = {prob_a_dado_b:.3f} * {prob_b:.3f} = {prob_multiplicacao:.3f}")
    
    print(f"\n4. VERIFICAÇÃO:")
    print(f"   Cálculo direto: {prob_direta:.3f}")
    print(f"   Regra da multiplicação: {prob_multiplicacao:.3f}")
    print(f"   Diferença: {abs(prob_direta - prob_multiplicacao):.6f}")

if __name__ == "__main__":
    # Executa todos os exemplos
    prob_dados, prob_sim = exemplo_dados_soma()
    prob_baralho = exemplo_baralho_cartas()
    prob_doenca = exemplo_doenca_teste()
    
    # Visualizações
    plotar_probabilidade_condicional()
    demonstrar_regra_multiplicacao()
