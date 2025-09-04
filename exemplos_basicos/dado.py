"""
Exemplo básico: Lançamento de Dado
Demonstra espaço amostral, eventos e probabilidades
"""

import random
import matplotlib.pyplot as plt
from collections import Counter

class Dado:
    """
    Classe que representa um dado de 6 faces e suas operações probabilísticas
    """
    
    def __init__(self, faces=6):
        self.faces = faces
        self.espaco_amostral = list(range(1, faces + 1))
        self.historico = []
    
    def lancar(self):
        """
        Lança o dado e retorna o resultado
        """
        resultado = random.choice(self.espaco_amostral)
        self.historico.append(resultado)
        return resultado
    
    def lancar_multiplas_vezes(self, n):
        """
        Lança o dado n vezes e retorna os resultados
        """
        resultados = []
        for _ in range(n):
            resultados.append(self.lancar())
        return resultados
    
    def probabilidade_evento(self, evento):
        """
        Calcula a probabilidade de um evento específico
        evento: lista de resultados desejados
        """
        if not isinstance(evento, list):
            evento = [evento]
        
        # Verifica se todos os elementos do evento estão no espaço amostral
        for elemento in evento:
            if elemento not in self.espaco_amostral:
                raise ValueError(f"Elemento {elemento} não está no espaço amostral")
        
        return len(evento) / len(self.espaco_amostral)
    
    def probabilidade_empirica(self, evento, n_lancamentos=None):
        """
        Calcula a probabilidade empírica de um evento
        """
        if n_lancamentos is None:
            n_lancamentos = len(self.historico)
        
        if n_lancamentos == 0:
            return 0
        
        if not isinstance(evento, list):
            evento = [evento]
        
        # Usa apenas os últimos n_lancamentos
        historico_recente = self.historico[-n_lancamentos:]
        
        # Conta quantas vezes o evento ocorreu
        ocorrencias = sum(1 for resultado in historico_recente if resultado in evento)
        
        return ocorrencias / n_lancamentos
    
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
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gráfico de barras
        faces = list(range(1, self.faces + 1))
        valores = [contagem[face] for face in faces]
        
        cores = plt.cm.viridis([i/self.faces for i in range(self.faces)])
        barras = ax1.bar(faces, valores, color=cores, alpha=0.7)
        ax1.set_title(f'Resultados de {n_lancamentos} lançamentos')
        ax1.set_ylabel('Frequência')
        ax1.set_xlabel('Face do Dado')
        ax1.set_xticks(faces)
        
        # Adiciona valores nas barras
        for barra, valor in zip(barras, valores):
            ax1.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                    str(valor), ha='center', va='bottom')
        
        # Gráfico de probabilidade empírica ao longo do tempo
        probabilidades_face_1 = []
        for i in range(1, n_lancamentos + 1):
            prob = self.probabilidade_empirica(1, i)
            probabilidades_face_1.append(prob)
        
        ax2.plot(range(1, n_lancamentos + 1), probabilidades_face_1, 'b-', alpha=0.7)
        ax2.axhline(y=1/self.faces, color='r', linestyle='--', 
                   label=f'Probabilidade Teórica (1/{self.faces})')
        ax2.set_title('Convergência da Probabilidade Empírica (Face 1)')
        ax2.set_xlabel('Número de lançamentos')
        ax2.set_ylabel('Probabilidade da Face 1')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        return contagem

def demonstrar_eventos():
    """
    Demonstra diferentes tipos de eventos com um dado
    """
    print("=== DEMONSTRAÇÃO: LANÇAMENTO DE DADO ===\n")
    
    # Cria um dado
    dado = Dado()
    
    print("1. ESPAÇO AMOSTRAL:")
    print(f"   Ω = {dado.espaco_amostral}")
    print(f"   Número de resultados possíveis: {len(dado.espaco_amostral)}\n")
    
    print("2. EVENTOS E SUAS PROBABILIDADES:")
    
    # Evento: sair um número par
    evento_par = [2, 4, 6]
    prob_par = dado.probabilidade_evento(evento_par)
    print(f"   A = 'Sair número par' = {evento_par}")
    print(f"   P(A) = {prob_par}")
    
    # Evento: sair um número ímpar
    evento_impar = [1, 3, 5]
    prob_impar = dado.probabilidade_evento(evento_impar)
    print(f"   B = 'Sair número ímpar' = {evento_impar}")
    print(f"   P(B) = {prob_impar}")
    
    # Evento: sair um número maior que 4
    evento_maior_4 = [5, 6]
    prob_maior_4 = dado.probabilidade_evento(evento_maior_4)
    print(f"   C = 'Sair número > 4' = {evento_maior_4}")
    print(f"   P(C) = {prob_maior_4}")
    
    # Evento: sair um número específico
    evento_especifico = [3]
    prob_especifico = dado.probabilidade_evento(evento_especifico)
    print(f"   D = 'Sair número 3' = {evento_especifico}")
    print(f"   P(D) = {prob_especifico}")
    
    print("\n3. SIMULAÇÃO DE LANÇAMENTOS:")
    n_lancamentos = 100
    resultados = dado.lancar_multiplas_vezes(n_lancamentos)
    print(f"   Resultados de {n_lancamentos} lançamentos: {resultados[:20]}...")
    
    contagem = Counter(resultados)
    print(f"   Contagem: {dict(contagem)}")
    
    print("\n4. PROBABILIDADES EMPÍRICAS:")
    print(f"   P(número par) = {dado.probabilidade_empirica(evento_par):.3f}")
    print(f"   P(número ímpar) = {dado.probabilidade_empirica(evento_impar):.3f}")
    print(f"   P(número > 4) = {dado.probabilidade_empirica(evento_maior_4):.3f}")
    print(f"   P(número 3) = {dado.probabilidade_empirica(evento_especifico):.3f}")
    
    print("\n5. VERIFICAÇÃO DE PROPRIEDADES:")
    print(f"   P(par) + P(ímpar) = {prob_par + prob_impar} (deve ser 1)")
    print(f"   P(par) = P(ímpar) = {prob_par} (eventos equiprováveis)")
    
    return dado

def demonstrar_dois_dados():
    """
    Demonstra o lançamento de dois dados simultaneamente
    """
    print("\n=== DEMONSTRAÇÃO: DOIS DADOS ===\n")
    
    dado1 = Dado()
    dado2 = Dado()
    
    print("1. ESPAÇO AMOSTRAL (dois dados):")
    print("   Ω = {(1,1), (1,2), ..., (6,6)}")
    print(f"   Número de resultados possíveis: {6 * 6} = 36")
    
    print("\n2. SIMULAÇÃO DE LANÇAMENTOS:")
    n_lancamentos = 1000
    resultados = []
    somas = []
    
    for _ in range(n_lancamentos):
        resultado1 = dado1.lancar()
        resultado2 = dado2.lancar()
        resultados.append((resultado1, resultado2))
        somas.append(resultado1 + resultado2)
    
    print(f"   Primeiros 10 resultados: {resultados[:10]}")
    print(f"   Primeiras 10 somas: {somas[:10]}")
    
    # Análise das somas
    contagem_somas = Counter(somas)
    print(f"\n3. DISTRIBUIÇÃO DAS SOMAS:")
    for soma in sorted(contagem_somas.keys()):
        freq = contagem_somas[soma]
        prob_empirica = freq / n_lancamentos
        print(f"   Soma {soma}: {freq} ocorrências (P = {prob_empirica:.3f})")
    
    # Probabilidade teórica da soma 7
    prob_teorica_7 = 6 / 36  # Há 6 maneiras de obter soma 7
    prob_empirica_7 = contagem_somas[7] / n_lancamentos
    print(f"\n4. ANÁLISE DA SOMA 7:")
    print(f"   P(soma = 7) teórica = {prob_teorica_7:.3f}")
    print(f"   P(soma = 7) empírica = {prob_empirica_7:.3f}")
    
    return resultados, somas

if __name__ == "__main__":
    # Executa as demonstrações
    dado = demonstrar_eventos()
    
    # Plota os resultados
    print("\n6. VISUALIZAÇÃO DOS RESULTADOS:")
    print("   Gerando gráficos...")
    dado.plotar_resultados(1000)
    
    # Demonstra dois dados
    resultados_2d, somas = demonstrar_dois_dados()
