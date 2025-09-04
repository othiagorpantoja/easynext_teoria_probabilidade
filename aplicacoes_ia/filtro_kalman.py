"""
Filtro de Kalman
Demonstra como usar probabilidade para estimação de estado em sistemas dinâmicos
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import inv

class FiltroKalman:
    """
    Implementação do Filtro de Kalman para estimação de estado
    """
    
    def __init__(self, dim_estado, dim_observacao):
        self.dim_estado = dim_estado
        self.dim_observacao = dim_observacao
        
        # Matrizes do modelo
        self.F = np.eye(dim_estado)  # Matriz de transição de estado
        self.H = np.eye(dim_observacao, dim_estado)  # Matriz de observação
        self.Q = np.eye(dim_estado)  # Matriz de covariância do ruído do processo
        self.R = np.eye(dim_observacao)  # Matriz de covariância do ruído da observação
        
        # Estado inicial
        self.x = np.zeros(dim_estado)  # Estado estimado
        self.P = np.eye(dim_estado)  # Matriz de covariância do estado
    
    def predicao(self):
        """
        Etapa de predição do Filtro de Kalman
        """
        # Prediz o estado
        self.x = self.F @ self.x
        
        # Prediz a covariância
        self.P = self.F @ self.P @ self.F.T + self.Q
    
    def atualizacao(self, z):
        """
        Etapa de atualização do Filtro de Kalman
        z: observação atual
        """
        # Calcula o ganho de Kalman
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ inv(S)
        
        # Atualiza o estado
        y = z - self.H @ self.x  # Resíduo
        self.x = self.x + K @ y
        
        # Atualiza a covariância
        I = np.eye(self.dim_estado)
        self.P = (I - K @ self.H) @ self.P
    
    def filtrar(self, observacoes):
        """
        Aplica o Filtro de Kalman a uma sequência de observações
        """
        estados_estimados = []
        covariancias = []
        
        for z in observacoes:
            # Predição
            self.predicao()
            
            # Atualização
            self.atualizacao(z)
            
            estados_estimados.append(self.x.copy())
            covariancias.append(self.P.copy())
        
        return np.array(estados_estimados), np.array(covariancias)

def exemplo_movimento_retilineo():
    """
    Exemplo: Filtro de Kalman para movimento retilíneo uniforme
    """
    print("=== EXEMPLO: MOVIMENTO RETILÍNEO UNIFORME ===\n")
    
    # Parâmetros do sistema
    dt = 0.1  # Intervalo de tempo
    tempo_total = 10.0
    n_pontos = int(tempo_total / dt)
    
    # Estado: [posição, velocidade]
    dim_estado = 2
    dim_observacao = 1
    
    # Cria o filtro
    filtro = FiltroKalman(dim_estado, dim_observacao)
    
    # Define as matrizes do modelo
    filtro.F = np.array([[1, dt],
                        [0, 1]])  # Matriz de transição
    
    filtro.H = np.array([[1, 0]])  # Observamos apenas a posição
    
    # Ruídos
    filtro.Q = np.array([[0.1, 0],
                        [0, 0.1]])  # Ruído do processo
    
    filtro.R = np.array([[1.0]])  # Ruído da observação
    
    # Estado inicial
    filtro.x = np.array([0.0, 1.0])  # Posição inicial = 0, velocidade = 1
    filtro.P = np.array([[1.0, 0],
                        [0, 1.0]])
    
    print("1. PARÂMETROS DO SISTEMA:")
    print(f"   Intervalo de tempo: {dt}")
    print(f"   Tempo total: {tempo_total}")
    print(f"   Estado inicial: posição = {filtro.x[0]}, velocidade = {filtro.x[1]}")
    
    # Gera dados simulados
    tempo = np.linspace(0, tempo_total, n_pontos)
    
    # Estado real (sem ruído)
    posicao_real = 1.0 * tempo  # Movimento com velocidade constante = 1
    velocidade_real = np.ones(n_pontos) * 1.0
    
    # Adiciona ruído às observações
    ruido_observacao = np.random.normal(0, 1.0, n_pontos)
    observacoes = posicao_real + ruido_observacao
    
    print(f"\n2. DADOS SIMULADOS:")
    print(f"   Número de observações: {n_pontos}")
    print(f"   Ruído da observação: σ = 1.0")
    
    # Aplica o filtro
    estados_estimados, covariancias = filtro.filtrar(observacoes)
    
    # Extrai posições e velocidades estimadas
    posicoes_estimadas = estados_estimados[:, 0]
    velocidades_estimadas = estados_estimados[:, 1]
    
    # Calcula incertezas (desvios padrão)
    incertezas_posicao = np.sqrt(covariancias[:, 0, 0])
    incertezas_velocidade = np.sqrt(covariancias[:, 1, 1])
    
    print(f"\n3. RESULTADOS:")
    print(f"   Erro médio na posição: {np.mean(np.abs(posicoes_estimadas - posicao_real)):.3f}")
    print(f"   Erro médio na velocidade: {np.mean(np.abs(velocidades_estimadas - velocidade_real)):.3f}")
    
    # Plota os resultados
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Posição vs tempo
    ax1.plot(tempo, posicao_real, 'g-', label='Posição Real', linewidth=2)
    ax1.plot(tempo, observacoes, 'r.', label='Observações', alpha=0.6)
    ax1.plot(tempo, posicoes_estimadas, 'b-', label='Posição Estimada', linewidth=2)
    ax1.fill_between(tempo, posicoes_estimadas - incertezas_posicao, 
                    posicoes_estimadas + incertezas_posicao, 
                    alpha=0.3, color='blue', label='Incerteza')
    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Posição')
    ax1.set_title('Estimação de Posição')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Velocidade vs tempo
    ax2.plot(tempo, velocidade_real, 'g-', label='Velocidade Real', linewidth=2)
    ax2.plot(tempo, velocidades_estimadas, 'b-', label='Velocidade Estimada', linewidth=2)
    ax2.fill_between(tempo, velocidades_estimadas - incertezas_velocidade, 
                    velocidades_estimadas + incertezas_velocidade, 
                    alpha=0.3, color='blue', label='Incerteza')
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Velocidade')
    ax2.set_title('Estimação de Velocidade')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Erro na posição
    erro_posicao = posicoes_estimadas - posicao_real
    ax3.plot(tempo, erro_posicao, 'r-', linewidth=2)
    ax3.fill_between(tempo, -incertezas_posicao, incertezas_posicao, 
                    alpha=0.3, color='red', label='Incerteza')
    ax3.set_xlabel('Tempo')
    ax3.set_ylabel('Erro na Posição')
    ax3.set_title('Erro na Estimação de Posição')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Erro na velocidade
    erro_velocidade = velocidades_estimadas - velocidade_real
    ax4.plot(tempo, erro_velocidade, 'r-', linewidth=2)
    ax4.fill_between(tempo, -incertezas_velocidade, incertezas_velocidade, 
                    alpha=0.3, color='red', label='Incerteza')
    ax4.set_xlabel('Tempo')
    ax4.set_ylabel('Erro na Velocidade')
    ax4.set_title('Erro na Estimação de Velocidade')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return filtro, tempo, posicao_real, observacoes, posicoes_estimadas

def exemplo_movimento_acelerado():
    """
    Exemplo: Filtro de Kalman para movimento com aceleração
    """
    print("\n=== EXEMPLO: MOVIMENTO COM ACELERAÇÃO ===\n")
    
    # Parâmetros do sistema
    dt = 0.1
    tempo_total = 10.0
    n_pontos = int(tempo_total / dt)
    
    # Estado: [posição, velocidade, aceleração]
    dim_estado = 3
    dim_observacao = 1
    
    # Cria o filtro
    filtro = FiltroKalman(dim_estado, dim_observacao)
    
    # Define as matrizes do modelo
    filtro.F = np.array([[1, dt, 0.5*dt**2],
                        [0, 1, dt],
                        [0, 0, 1]])  # Matriz de transição
    
    filtro.H = np.array([[1, 0, 0]])  # Observamos apenas a posição
    
    # Ruídos
    filtro.Q = np.array([[0.01, 0, 0],
                        [0, 0.01, 0],
                        [0, 0, 0.01]])  # Ruído do processo
    
    filtro.R = np.array([[1.0]])  # Ruído da observação
    
    # Estado inicial
    filtro.x = np.array([0.0, 0.0, 0.5])  # Posição=0, velocidade=0, aceleração=0.5
    filtro.P = np.array([[1.0, 0, 0],
                        [0, 1.0, 0],
                        [0, 0, 1.0]])
    
    print("1. PARÂMETROS DO SISTEMA:")
    print(f"   Estado inicial: posição = {filtro.x[0]}, velocidade = {filtro.x[1]}, aceleração = {filtro.x[2]}")
    
    # Gera dados simulados
    tempo = np.linspace(0, tempo_total, n_pontos)
    
    # Estado real (movimento com aceleração constante)
    posicao_real = 0.5 * 0.5 * tempo**2  # s = 0.5 * a * t^2
    velocidade_real = 0.5 * tempo  # v = a * t
    aceleracao_real = np.ones(n_pontos) * 0.5
    
    # Adiciona ruído às observações
    ruido_observacao = np.random.normal(0, 1.0, n_pontos)
    observacoes = posicao_real + ruido_observacao
    
    # Aplica o filtro
    estados_estimados, covariancias = filtro.filtrar(observacoes)
    
    # Extrai estimativas
    posicoes_estimadas = estados_estimados[:, 0]
    velocidades_estimadas = estados_estimados[:, 1]
    aceleracoes_estimadas = estados_estimados[:, 2]
    
    print(f"\n2. RESULTADOS:")
    print(f"   Erro médio na posição: {np.mean(np.abs(posicoes_estimadas - posicao_real)):.3f}")
    print(f"   Erro médio na velocidade: {np.mean(np.abs(velocidades_estimadas - velocidade_real)):.3f}")
    print(f"   Erro médio na aceleração: {np.mean(np.abs(aceleracoes_estimadas - aceleracao_real)):.3f}")
    
    # Plota os resultados
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    
    # Posição
    ax1.plot(tempo, posicao_real, 'g-', label='Real', linewidth=2)
    ax1.plot(tempo, observacoes, 'r.', label='Observações', alpha=0.6)
    ax1.plot(tempo, posicoes_estimadas, 'b-', label='Estimada', linewidth=2)
    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Posição')
    ax1.set_title('Estimação de Posição')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Velocidade
    ax2.plot(tempo, velocidade_real, 'g-', label='Real', linewidth=2)
    ax2.plot(tempo, velocidades_estimadas, 'b-', label='Estimada', linewidth=2)
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Velocidade')
    ax2.set_title('Estimação de Velocidade')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Aceleração
    ax3.plot(tempo, aceleracao_real, 'g-', label='Real', linewidth=2)
    ax3.plot(tempo, aceleracoes_estimadas, 'b-', label='Estimada', linewidth=2)
    ax3.set_xlabel('Tempo')
    ax3.set_ylabel('Aceleração')
    ax3.set_title('Estimação de Aceleração')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return filtro, tempo, posicao_real, observacoes, posicoes_estimadas

def exemplo_filtro_kalman_estendido():
    """
    Demonstra conceitos do Filtro de Kalman Estendido (EKF)
    """
    print("\n=== CONCEITOS DO FILTRO DE KALMAN ESTENDIDO ===\n")
    
    print("1. LIMITAÇÕES DO FILTRO DE KALMAN PADRÃO:")
    print("   - Assume modelos lineares")
    print("   - Assume ruídos gaussianos")
    print("   - Assume matrizes de transição e observação constantes")
    
    print("\n2. FILTRO DE KALMAN ESTENDIDO (EKF):")
    print("   - Lida com modelos não-lineares")
    print("   - Lineariza o modelo em torno do estado atual")
    print("   - Usa matrizes Jacobianas")
    
    print("\n3. APLICAÇÕES DO EKF:")
    print("   - Navegação por GPS")
    print("   - Controle de robôs")
    print("   - Rastreamento de alvos")
    print("   - Fusão de sensores")
    
    print("\n4. VANTAGENS:")
    print("   - Lida com não-linearidades")
    print("   - Fornece estimativas de incerteza")
    print("   - Eficiente computacionalmente")
    print("   - Robusto a ruídos")
    
    print("\n5. LIMITAÇÕES:")
    print("   - Requer linearização")
    print("   - Pode divergir com não-linearidades fortes")
    print("   - Sensível à inicialização")

def demonstrar_incerteza_kalman():
    """
    Demonstra como o Filtro de Kalman quantifica incerteza
    """
    print("\n=== INCERTEZA NO FILTRO DE KALMAN ===\n")
    
    print("1. MATRIZ DE COVARIÂNCIA P:")
    print("   - Quantifica a incerteza no estado estimado")
    print("   - Diagonal: variância de cada componente do estado")
    print("   - Off-diagonal: covariância entre componentes")
    
    print("\n2. EVOLUÇÃO DA INCERTEZA:")
    print("   - Predição: P aumenta (incerteza cresce)")
    print("   - Atualização: P diminui (incerteza diminui)")
    print("   - Convergência: P tende a um valor estável")
    
    print("\n3. GANHO DE KALMAN K:")
    print("   - Balanceia entre predição e observação")
    print("   - K alto: confia mais na observação")
    print("   - K baixo: confia mais na predição")
    
    print("\n4. INTERPRETAÇÃO PROBABILÍSTICA:")
    print("   - Estado estimado: média da distribuição")
    print("   - Matriz P: covariância da distribuição")
    print("   - Intervalos de confiança: ±2σ")

if __name__ == "__main__":
    # Executa todos os exemplos
    filtro1, tempo1, pos_real1, obs1, pos_est1 = exemplo_movimento_retilineo()
    filtro2, tempo2, pos_real2, obs2, pos_est2 = exemplo_movimento_acelerado()
    
    # Demonstrações conceituais
    exemplo_filtro_kalman_estendido()
    demonstrar_incerteza_kalman()
