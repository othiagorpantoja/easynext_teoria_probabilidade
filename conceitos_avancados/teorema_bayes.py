"""
Teorema de Bayes
Demonstra P(A|B) = P(B|A) * P(A) / P(B)

Desenvolvido por: Thiago Rodrigues Pantoja
Empresa: EasyNext Informática LTDA
Emails: thiago.pantoja@easynext.tech | thiago.pantoja@easynext.consulting
Telefones: (11) 98801-0667 | (92) 98456-1928
Data: Setembro 2025
"""

import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

class TeoremaBayes:
    """
    Classe para demonstrar o Teorema de Bayes
    """
    
    def __init__(self):
        pass
    
    def calcular_bayes(self, prob_a, prob_b_dado_a, prob_b):
        """
        Calcula P(A|B) usando o Teorema de Bayes
        P(A|B) = P(B|A) * P(A) / P(B)
        """
        if prob_b == 0:
            return 0
        return (prob_b_dado_a * prob_a) / prob_b
    
    def calcular_bayes_completo(self, prob_a, prob_b_dado_a, prob_b_dado_nao_a):
        """
        Calcula P(A|B) usando o Teorema de Bayes completo
        P(A|B) = P(B|A) * P(A) / [P(B|A) * P(A) + P(B|A') * P(A')]
        """
        prob_nao_a = 1 - prob_a
        prob_b = prob_b_dado_a * prob_a + prob_b_dado_nao_a * prob_nao_a
        return self.calcular_bayes(prob_a, prob_b_dado_a, prob_b)

def exemplo_doenca_teste():
    """
    Exemplo clássico: Teste de doença com falsos positivos
    """
    print("=== EXEMPLO: TESTE DE DOENÇA ===\n")
    
    # Parâmetros
    prevalencia = 0.01  # 1% da população tem a doença
    sensibilidade = 0.95  # 95% dos doentes testam positivo
    especificidade = 0.98  # 98% dos não-doentes testam negativo
    
    print("1. PARÂMETROS:")
    print(f"   Prevalência (P(doença)): {prevalencia:.1%}")
    print(f"   Sensibilidade (P(teste+|doença)): {sensibilidade:.1%}")
    print(f"   Especificidade (P(teste-|não doença)): {especificidade:.1%}")
    
    print("\n2. CÁLCULO USANDO TEOREMA DE BAYES:")
    
    # P(teste positivo | não doença) = 1 - especificidade
    prob_positivo_nao_doenca = 1 - especificidade
    
    # P(teste positivo) = P(teste+|doença) * P(doença) + P(teste+|não doença) * P(não doença)
    prob_positivo = (sensibilidade * prevalencia + 
                    prob_positivo_nao_doenca * (1 - prevalencia))
    
    # P(doença | teste positivo) usando Bayes
    tb = TeoremaBayes()
    prob_doenca_positivo = tb.calcular_bayes(prevalencia, sensibilidade, prob_positivo)
    
    print(f"   P(teste positivo | não doença): {prob_positivo_nao_doenca:.1%}")
    print(f"   P(teste positivo): {prob_positivo:.1%}")
    print(f"   P(doença | teste positivo): {prob_doenca_positivo:.1%}")
    
    print(f"\n3. INTERPRETAÇÃO:")
    print(f"   Mesmo com um teste muito bom, a probabilidade de ter a doença")
    print(f"   dado um teste positivo é apenas {prob_doenca_positivo:.1%}")
    print(f"   Isso acontece porque a doença é rara (prevalência baixa)")
    
    return prob_doenca_positivo

def exemplo_spam_email():
    """
    Exemplo: Filtro de spam usando Teorema de Bayes
    """
    print("\n=== EXEMPLO: FILTRO DE SPAM ===\n")
    
    # Parâmetros do problema
    prob_spam = 0.3  # 30% dos emails são spam
    prob_palavra_spam = 0.8  # 80% dos spams contêm a palavra "oferta"
    prob_palavra_nao_spam = 0.1  # 10% dos não-spams contêm a palavra "oferta"
    
    print("1. PARÂMETROS:")
    print(f"   P(spam): {prob_spam:.1%}")
    print(f"   P('oferta' | spam): {prob_palavra_spam:.1%}")
    print(f"   P('oferta' | não spam): {prob_palavra_nao_spam:.1%}")
    
    print("\n2. CÁLCULO USANDO TEOREMA DE BAYES:")
    
    # P('oferta')
    prob_oferta = (prob_palavra_spam * prob_spam + 
                  prob_palavra_nao_spam * (1 - prob_spam))
    
    # P(spam | 'oferta')
    tb = TeoremaBayes()
    prob_spam_oferta = tb.calcular_bayes(prob_spam, prob_palavra_spam, prob_oferta)
    
    print(f"   P('oferta'): {prob_oferta:.1%}")
    print(f"   P(spam | 'oferta'): {prob_spam_oferta:.1%}")
    
    print(f"\n3. INTERPRETAÇÃO:")
    print(f"   Se um email contém a palavra 'oferta', a probabilidade")
    print(f"   de ser spam é {prob_spam_oferta:.1%}")
    
    return prob_spam_oferta

def exemplo_urna_bolas():
    """
    Exemplo: Urna com bolas de diferentes cores
    """
    print("\n=== EXEMPLO: URNA COM BOLAS ===\n")
    
    # Urna 1: 3 bolas vermelhas, 2 azuis
    # Urna 2: 1 bola vermelha, 4 azuis
    # Escolhe-se uma urna aleatoriamente e depois uma bola
    
    print("1. SITUAÇÃO:")
    print("   Urna 1: 3 bolas vermelhas, 2 azuis")
    print("   Urna 2: 1 bola vermelha, 4 azuis")
    print("   Escolhe-se uma urna aleatoriamente, depois uma bola")
    
    print("\n2. PERGUNTA:")
    print("   Se a bola sorteada é vermelha, qual a probabilidade")
    print("   de ter vindo da Urna 1?")
    
    print("\n3. CÁLCULO USANDO TEOREMA DE BAYES:")
    
    # P(Urna 1) = P(Urna 2) = 0.5
    prob_urna1 = 0.5
    prob_urna2 = 0.5
    
    # P(vermelha | Urna 1) = 3/5
    prob_vermelha_urna1 = 3/5
    
    # P(vermelha | Urna 2) = 1/5
    prob_vermelha_urna2 = 1/5
    
    # P(vermelha) = P(vermelha|Urna1)*P(Urna1) + P(vermelha|Urna2)*P(Urna2)
    prob_vermelha = prob_vermelha_urna1 * prob_urna1 + prob_vermelha_urna2 * prob_urna2
    
    # P(Urna 1 | vermelha)
    tb = TeoremaBayes()
    prob_urna1_vermelha = tb.calcular_bayes(prob_urna1, prob_vermelha_urna1, prob_vermelha)
    
    print(f"   P(Urna 1): {prob_urna1:.1%}")
    print(f"   P(vermelha | Urna 1): {prob_vermelha_urna1:.1%}")
    print(f"   P(vermelha | Urna 2): {prob_vermelha_urna2:.1%}")
    print(f"   P(vermelha): {prob_vermelha:.1%}")
    print(f"   P(Urna 1 | vermelha): {prob_urna1_vermelha:.1%}")
    
    print(f"\n4. INTERPRETAÇÃO:")
    print(f"   Se a bola é vermelha, a probabilidade de ter vindo")
    print(f"   da Urna 1 é {prob_urna1_vermelha:.1%}")
    
    return prob_urna1_vermelha

def exemplo_diagnostico_medico():
    """
    Exemplo: Diagnóstico médico com múltiplos sintomas
    """
    print("\n=== EXEMPLO: DIAGNÓSTICO MÉDICO ===\n")
    
    # Doença A: 2% da população
    # Doença B: 1% da população
    # Doença C: 0.5% da população
    # Sem doença: 96.5% da população
    
    print("1. PREVALÊNCIAS:")
    print("   Doença A: 2%")
    print("   Doença B: 1%")
    print("   Doença C: 0.5%")
    print("   Sem doença: 96.5%")
    
    print("\n2. PROBABILIDADES DE SINTOMA:")
    print("   P(sintoma | Doença A): 80%")
    print("   P(sintoma | Doença B): 60%")
    print("   P(sintoma | Doença C): 40%")
    print("   P(sintoma | Sem doença): 5%")
    
    # Cálculos
    prob_a = 0.02
    prob_b = 0.01
    prob_c = 0.005
    prob_sem = 0.965
    
    prob_sintoma_a = 0.8
    prob_sintoma_b = 0.6
    prob_sintoma_c = 0.4
    prob_sintoma_sem = 0.05
    
    # P(sintoma)
    prob_sintoma = (prob_sintoma_a * prob_a + 
                   prob_sintoma_b * prob_b + 
                   prob_sintoma_c * prob_c + 
                   prob_sintoma_sem * prob_sem)
    
    print(f"\n3. CÁLCULO USANDO TEOREMA DE BAYES:")
    print(f"   P(sintoma): {prob_sintoma:.1%}")
    
    tb = TeoremaBayes()
    
    # P(Doença A | sintoma)
    prob_a_sintoma = tb.calcular_bayes(prob_a, prob_sintoma_a, prob_sintoma)
    
    # P(Doença B | sintoma)
    prob_b_sintoma = tb.calcular_bayes(prob_b, prob_sintoma_b, prob_sintoma)
    
    # P(Doença C | sintoma)
    prob_c_sintoma = tb.calcular_bayes(prob_c, prob_sintoma_c, prob_sintoma)
    
    # P(Sem doença | sintoma)
    prob_sem_sintoma = tb.calcular_bayes(prob_sem, prob_sintoma_sem, prob_sintoma)
    
    print(f"\n4. PROBABILIDADES POSTERIORES:")
    print(f"   P(Doença A | sintoma): {prob_a_sintoma:.1%}")
    print(f"   P(Doença B | sintoma): {prob_b_sintoma:.1%}")
    print(f"   P(Doença C | sintoma): {prob_c_sintoma:.1%}")
    print(f"   P(Sem doença | sintoma): {prob_sem_sintoma:.1%}")
    
    print(f"\n5. INTERPRETAÇÃO:")
    print(f"   Dado que o paciente tem o sintoma, a doença mais provável")
    print(f"   é a Doença A com {prob_a_sintoma:.1%} de probabilidade")
    
    return prob_a_sintoma, prob_b_sintoma, prob_c_sintoma, prob_sem_sintoma

def plotar_bayes_vs_prevalencia():
    """
    Plota como a probabilidade posterior varia com a prevalência
    """
    print("\n=== VISUALIZAÇÃO: BAYES VS PREVALÊNCIA ===\n")
    
    # Varia a prevalência da doença
    prevalencias = np.linspace(0.001, 0.2, 100)
    sensibilidade = 0.95
    especificidade = 0.98
    
    probabilidades_posteriores = []
    
    tb = TeoremaBayes()
    
    for prevalencia in prevalencias:
        prob_positivo_nao_doenca = 1 - especificidade
        prob_positivo = (sensibilidade * prevalencia + 
                        prob_positivo_nao_doenca * (1 - prevalencia))
        prob_posterior = tb.calcular_bayes(prevalencia, sensibilidade, prob_positivo)
        probabilidades_posteriores.append(prob_posterior)
    
    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(prevalencias * 100, probabilidades_posteriores, 'b-', linewidth=2)
    plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='50%')
    plt.xlabel('Prevalência da Doença (%)')
    plt.ylabel('P(doença | teste positivo)')
    plt.title('Teorema de Bayes: Probabilidade Posterior vs Prevalência')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    print("O gráfico mostra como a probabilidade posterior aumenta")
    print("conforme a prevalência da doença aumenta.")

def demonstrar_versao_completa_bayes():
    """
    Demonstra a versão completa do Teorema de Bayes
    """
    print("\n=== VERSÃO COMPLETA DO TEOREMA DE BAYES ===\n")
    
    print("1. FÓRMULA COMPLETA:")
    print("   P(A|B) = P(B|A) * P(A) / [P(B|A) * P(A) + P(B|A') * P(A')]")
    print("   onde A' é o complementar de A")
    
    print("\n2. EXEMPLO PRÁTICO:")
    print("   A = 'Paciente tem a doença'")
    print("   B = 'Teste é positivo'")
    print("   A' = 'Paciente não tem a doença'")
    
    # Parâmetros
    prevalencia = 0.01
    sensibilidade = 0.95
    especificidade = 0.98
    
    print(f"\n3. PARÂMETROS:")
    print(f"   P(A) = {prevalencia:.1%}")
    print(f"   P(B|A) = {sensibilidade:.1%}")
    print(f"   P(B|A') = {1-especificidade:.1%}")
    
    # Cálculo usando versão completa
    tb = TeoremaBayes()
    prob_posterior = tb.calcular_bayes_completo(prevalencia, sensibilidade, 1-especificidade)
    
    print(f"\n4. CÁLCULO:")
    print(f"   P(A|B) = {prob_posterior:.1%}")
    
    print(f"\n5. VANTAGEM DA VERSÃO COMPLETA:")
    print("   Não precisamos calcular P(B) separadamente")
    print("   A fórmula já inclui todos os cenários possíveis")

if __name__ == "__main__":
    # Executa todos os exemplos
    prob_doenca = exemplo_doenca_teste()
    prob_spam = exemplo_spam_email()
    prob_urna = exemplo_urna_bolas()
    probs_diagnostico = exemplo_diagnostico_medico()
    
    # Visualizações
    plotar_bayes_vs_prevalencia()
    demonstrar_versao_completa_bayes()
