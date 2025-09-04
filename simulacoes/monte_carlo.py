"""
Simulações Monte Carlo
Demonstra como usar simulação para resolver problemas probabilísticos

Desenvolvido por: Thiago Rodrigues Pantoja
Empresa: EasyNext Informática LTDA
Emails: thiago.pantoja@easynext.tech | thiago.pantoja@easynext.consulting
Telefones: (11) 98801-0667 | (92) 98456-1928
Data: Setembro 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

class SimulacaoMonteCarlo:
    """
    Classe para realizar simulações Monte Carlo
    """
    
    def __init__(self, n_simulacoes=10000):
        self.n_simulacoes = n_simulacoes
        self.resultados = []
    
    def simular_lancamento_dados(self, n_dados=2, n_lancamentos=1):
        """
        Simula lançamento de dados
        """
        resultados = []
        for _ in range(self.n_simulacoes):
            lancamentos = []
            for _ in range(n_lancamentos):
                soma = sum(random.randint(1, 6) for _ in range(n_dados))
                lancamentos.append(soma)
            resultados.append(lancamentos)
        return resultados
    
    def simular_probabilidade_soma(self, soma_desejada, n_dados=2):
        """
        Simula a probabilidade de obter uma soma específica
        """
        sucessos = 0
        for _ in range(self.n_simulacoes):
            soma = sum(random.randint(1, 6) for _ in range(n_dados))
            if soma == soma_desejada:
                sucessos += 1
        
        probabilidade = sucessos / self.n_simulacoes
        return probabilidade
    
    def simular_problema_monty_hall(self):
        """
        Simula o problema de Monty Hall
        """
        sucessos_mudanca = 0
        sucessos_nao_mudanca = 0
        
        for _ in range(self.n_simulacoes):
            # Coloca o prêmio atrás de uma porta aleatória
            porta_premio = random.randint(1, 3)
            
            # Jogador escolhe uma porta aleatória
            porta_escolhida = random.randint(1, 3)
            
            # Monty abre uma porta que não tem o prêmio
            portas_disponiveis = [1, 2, 3]
            portas_disponiveis.remove(porta_premio)
            if porta_escolhida in portas_disponiveis:
                portas_disponiveis.remove(porta_escolhida)
            porta_aberta = random.choice(portas_disponiveis)
            
            # Estratégia: não mudar
            if porta_escolhida == porta_premio:
                sucessos_nao_mudanca += 1
            
            # Estratégia: mudar
            portas_restantes = [1, 2, 3]
            portas_restantes.remove(porta_escolhida)
            portas_restantes.remove(porta_aberta)
            nova_porta = portas_restantes[0]
            
            if nova_porta == porta_premio:
                sucessos_mudanca += 1
        
        prob_mudanca = sucessos_mudanca / self.n_simulacoes
        prob_nao_mudanca = sucessos_nao_mudanca / self.n_simulacoes
        
        return prob_mudanca, prob_nao_mudanca
    
    def simular_integral_monte_carlo(self, funcao, a, b, n_pontos=None):
        """
        Estima uma integral usando Monte Carlo
        """
        if n_pontos is None:
            n_pontos = self.n_simulacoes
        
        # Gera pontos aleatórios
        x_aleatorios = np.random.uniform(a, b, n_pontos)
        y_aleatorios = np.random.uniform(0, 1, n_pontos)
        
        # Avalia a função nos pontos
        valores_funcao = [funcao(x) for x in x_aleatorios]
        
        # Conta pontos abaixo da curva
        pontos_abaixo = sum(1 for i in range(n_pontos) 
                          if y_aleatorios[i] <= valores_funcao[i])
        
        # Estima a integral
        area_retangulo = (b - a) * 1.0
        integral_estimada = (pontos_abaixo / n_pontos) * area_retangulo
        
        return integral_estimada, x_aleatorios, y_aleatorios, valores_funcao

def exemplo_soma_dados():
    """
    Exemplo: Simulação da soma de dois dados
    """
    print("=== EXEMPLO: SOMA DE DOIS DADOS ===\n")
    
    # Cria simulador
    simulador = SimulacaoMonteCarlo(n_simulacoes=10000)
    
    print("1. SIMULAÇÃO DA SOMA DE DOIS DADOS:")
    
    # Simula múltiplas somas
    resultados = simulador.simular_lancamento_dados(n_dados=2, n_lancamentos=1)
    somas = [resultado[0] for resultado in resultados]
    
    # Conta frequências
    frequencias = {}
    for soma in somas:
        frequencias[soma] = frequencias.get(soma, 0) + 1
    
    print("   Soma | Frequência | Probabilidade")
    print("   -----|------------|--------------")
    for soma in sorted(frequencias.keys()):
        freq = frequencias[soma]
        prob = freq / len(somas)
        print(f"   {soma:4d} | {freq:10d} | {prob:.3f}")
    
    # Compara com probabilidade teórica
    print(f"\n2. COMPARAÇÃO COM PROBABILIDADE TEÓRICA:")
    print("   Soma | Simulada | Teórica | Diferença")
    print("   -----|----------|---------|----------")
    
    for soma in range(2, 13):
        prob_simulada = simulador.simular_probabilidade_soma(soma)
        
        # Probabilidade teórica
        if soma <= 7:
            prob_teorica = (soma - 1) / 36
        else:
            prob_teorica = (13 - soma) / 36
        
        diferenca = abs(prob_simulada - prob_teorica)
        print(f"   {soma:4d} | {prob_simulada:.3f}    | {prob_teorica:.3f}    | {diferenca:.3f}")
    
    # Plota histograma
    plt.figure(figsize=(10, 6))
    plt.hist(somas, bins=11, range=(1.5, 12.5), density=True, alpha=0.7, color='skyblue')
    plt.xlabel('Soma dos Dados')
    plt.ylabel('Probabilidade')
    plt.title('Distribuição da Soma de Dois Dados (Simulação Monte Carlo)')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return simulador, somas

def exemplo_monty_hall():
    """
    Exemplo: Problema de Monty Hall
    """
    print("\n=== EXEMPLO: PROBLEMA DE MONTY HALL ===\n")
    
    # Cria simulador
    simulador = SimulacaoMonteCarlo(n_simulacoes=10000)
    
    print("1. PROBLEMA DE MONTY HALL:")
    print("   - 3 portas, 1 com prêmio")
    print("   - Jogador escolhe uma porta")
    print("   - Monty abre uma porta sem prêmio")
    print("   - Jogador pode mudar ou não")
    
    # Simula o problema
    prob_mudanca, prob_nao_mudanca = simulador.simular_problema_monty_hall()
    
    print(f"\n2. RESULTADOS DA SIMULAÇÃO:")
    print(f"   Estratégia: NÃO mudar")
    print(f"   Probabilidade de ganhar: {prob_nao_mudanca:.3f}")
    print(f"   Estratégia: MUDAR")
    print(f"   Probabilidade de ganhar: {prob_mudanca:.3f}")
    
    print(f"\n3. ANÁLISE:")
    print(f"   Diferença: {prob_mudanca - prob_nao_mudanca:.3f}")
    print(f"   É melhor mudar: {'Sim' if prob_mudanca > prob_nao_mudanca else 'Não'}")
    
    # Plota resultados
    estrategias = ['Não Mudar', 'Mudar']
    probabilidades = [prob_nao_mudanca, prob_mudanca]
    cores = ['lightcoral', 'lightgreen']
    
    plt.figure(figsize=(8, 6))
    barras = plt.bar(estrategias, probabilidades, color=cores, alpha=0.7)
    plt.ylabel('Probabilidade de Ganhar')
    plt.title('Problema de Monty Hall - Comparação de Estratégias')
    plt.ylim(0, 1)
    
    # Adiciona valores nas barras
    for barra, prob in zip(barras, probabilidades):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                f'{prob:.3f}', ha='center', va='bottom')
    
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return prob_mudanca, prob_nao_mudanca

def exemplo_integral_monte_carlo():
    """
    Exemplo: Estimação de integral usando Monte Carlo
    """
    print("\n=== EXEMPLO: INTEGRAL MONTE CARLO ===\n")
    
    # Cria simulador
    simulador = SimulacaoMonteCarlo(n_simulacoes=10000)
    
    print("1. ESTIMAÇÃO DA INTEGRAL ∫₀¹ x² dx:")
    
    # Define a função
    def funcao(x):
        return x**2
    
    # Estima a integral
    integral_estimada, x_aleatorios, y_aleatorios, valores_funcao = simulador.simular_integral_monte_carlo(
        funcao, 0, 1, 10000)
    
    # Valor teórico
    integral_teorica = 1/3
    
    print(f"   Integral estimada: {integral_estimada:.6f}")
    print(f"   Integral teórica:  {integral_teorica:.6f}")
    print(f"   Erro absoluto:     {abs(integral_estimada - integral_teorica):.6f}")
    print(f"   Erro relativo:     {abs(integral_estimada - integral_teorica)/integral_teorica:.2%}")
    
    # Plota a simulação
    plt.figure(figsize=(12, 8))
    
    # Subplot 1: Função e pontos
    plt.subplot(2, 2, 1)
    x_plot = np.linspace(0, 1, 1000)
    y_plot = [funcao(x) for x in x_plot]
    plt.plot(x_plot, y_plot, 'b-', linewidth=2, label='f(x) = x²')
    plt.scatter(x_aleatorios, y_aleatorios, c='red', alpha=0.5, s=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Função e Pontos Aleatórios')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 2: Pontos abaixo e acima da curva
    plt.subplot(2, 2, 2)
    pontos_abaixo = [i for i in range(len(x_aleatorios)) if y_aleatorios[i] <= valores_funcao[i]]
    pontos_acima = [i for i in range(len(x_aleatorios)) if y_aleatorios[i] > valores_funcao[i]]
    
    plt.plot(x_plot, y_plot, 'b-', linewidth=2, label='f(x) = x²')
    plt.scatter([x_aleatorios[i] for i in pontos_abaixo], 
               [y_aleatorios[i] for i in pontos_abaixo], 
               c='green', alpha=0.5, s=1, label='Abaixo da curva')
    plt.scatter([x_aleatorios[i] for i in pontos_acima], 
               [y_aleatorios[i] for i in pontos_acima], 
               c='red', alpha=0.5, s=1, label='Acima da curva')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Pontos Abaixo e Acima da Curva')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 3: Convergência
    plt.subplot(2, 2, 3)
    n_pontos = range(100, 10001, 100)
    integrais_convergencia = []
    
    for n in n_pontos:
        integral, _, _, _ = simulador.simular_integral_monte_carlo(funcao, 0, 1, n)
        integrais_convergencia.append(integral)
    
    plt.plot(n_pontos, integrais_convergencia, 'b-', alpha=0.7)
    plt.axhline(y=integral_teorica, color='r', linestyle='--', label='Valor Teórico')
    plt.xlabel('Número de Pontos')
    plt.ylabel('Integral Estimada')
    plt.title('Convergência da Estimativa')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 4: Erro
    plt.subplot(2, 2, 4)
    erros = [abs(integral - integral_teorica) for integral in integrais_convergencia]
    plt.plot(n_pontos, erros, 'r-', alpha=0.7)
    plt.xlabel('Número de Pontos')
    plt.ylabel('Erro Absoluto')
    plt.title('Erro da Estimativa')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return integral_estimada, integral_teorica

def exemplo_estimacao_pi():
    """
    Exemplo: Estimação de π usando Monte Carlo
    """
    print("\n=== EXEMPLO: ESTIMAÇÃO DE π ===\n")
    
    print("1. MÉTODO DE MONTE CARLO PARA ESTIMAR π:")
    print("   - Gera pontos aleatórios no quadrado [0,1] × [0,1]")
    print("   - Conta quantos estão dentro do círculo unitário")
    print("   - π ≈ 4 × (pontos dentro do círculo) / (total de pontos)")
    
    # Parâmetros
    n_pontos = 10000
    
    # Gera pontos aleatórios
    x = np.random.uniform(0, 1, n_pontos)
    y = np.random.uniform(0, 1, n_pontos)
    
    # Conta pontos dentro do círculo
    distancias = np.sqrt(x**2 + y**2)
    pontos_dentro = np.sum(distancias <= 1)
    
    # Estima π
    pi_estimado = 4 * pontos_dentro / n_pontos
    
    print(f"\n2. RESULTADOS:")
    print(f"   Número de pontos: {n_pontos}")
    print(f"   Pontos dentro do círculo: {pontos_dentro}")
    print(f"   π estimado: {pi_estimado:.6f}")
    print(f"   π real: {np.pi:.6f}")
    print(f"   Erro absoluto: {abs(pi_estimado - np.pi):.6f}")
    print(f"   Erro relativo: {abs(pi_estimado - np.pi)/np.pi:.2%}")
    
    # Plota a simulação
    plt.figure(figsize=(10, 8))
    
    # Subplot 1: Pontos e círculo
    plt.subplot(2, 2, 1)
    theta = np.linspace(0, 2*np.pi, 1000)
    x_circulo = np.cos(theta)
    y_circulo = np.sin(theta)
    
    plt.plot(x_circulo, y_circulo, 'b-', linewidth=2, label='Círculo unitário')
    plt.scatter(x, y, c='red', alpha=0.5, s=1)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pontos Aleatórios e Círculo Unitário')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # Subplot 2: Pontos dentro e fora
    plt.subplot(2, 2, 2)
    pontos_dentro_idx = distancias <= 1
    pontos_fora_idx = distancias > 1
    
    plt.plot(x_circulo, y_circulo, 'b-', linewidth=2, label='Círculo unitário')
    plt.scatter(x[pontos_dentro_idx], y[pontos_dentro_idx], 
               c='green', alpha=0.5, s=1, label='Dentro do círculo')
    plt.scatter(x[pontos_fora_idx], y[pontos_fora_idx], 
               c='red', alpha=0.5, s=1, label='Fora do círculo')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pontos Dentro e Fora do Círculo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # Subplot 3: Convergência
    plt.subplot(2, 2, 3)
    n_pontos_convergencia = range(100, 10001, 100)
    pi_estimados = []
    
    for n in n_pontos_convergencia:
        x_temp = np.random.uniform(0, 1, n)
        y_temp = np.random.uniform(0, 1, n)
        distancias_temp = np.sqrt(x_temp**2 + y_temp**2)
        pontos_dentro_temp = np.sum(distancias_temp <= 1)
        pi_estimado_temp = 4 * pontos_dentro_temp / n
        pi_estimados.append(pi_estimado_temp)
    
    plt.plot(n_pontos_convergencia, pi_estimados, 'b-', alpha=0.7)
    plt.axhline(y=np.pi, color='r', linestyle='--', label='π real')
    plt.xlabel('Número de Pontos')
    plt.ylabel('π Estimado')
    plt.title('Convergência da Estimativa de π')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Subplot 4: Erro
    plt.subplot(2, 2, 4)
    erros = [abs(pi_est - np.pi) for pi_est in pi_estimados]
    plt.plot(n_pontos_convergencia, erros, 'r-', alpha=0.7)
    plt.xlabel('Número de Pontos')
    plt.ylabel('Erro Absoluto')
    plt.title('Erro da Estimativa de π')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return pi_estimado, np.pi

if __name__ == "__main__":
    # Executa todos os exemplos
    simulador, somas = exemplo_soma_dados()
    prob_mudanca, prob_nao_mudanca = exemplo_monty_hall()
    integral_estimada, integral_teorica = exemplo_integral_monte_carlo()
    pi_estimado, pi_real = exemplo_estimacao_pi()
