"""
Classificação Probabilística
Demonstra como usar probabilidade para classificação em Machine Learning

Desenvolvido por: Thiago Rodrigues Pantoja
Empresa: EasyNext Informática LTDA
Emails: thiago.pantoja@easynext.tech | thiago.pantoja@easynext.consulting
Telefones: (11) 98801-0667 | (92) 98456-1928
Data: Setembro 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

class ClassificadorProbabilistico:
    """
    Classe para demonstrar classificação probabilística
    """
    
    def __init__(self):
        self.modelo = None
        self.classes = None
    
    def treinar_naive_bayes(self, X, y):
        """
        Treina um classificador Naive Bayes
        """
        self.modelo = GaussianNB()
        self.modelo.fit(X, y)
        self.classes = self.modelo.classes_
        return self.modelo
    
    def prever_probabilidades(self, X):
        """
        Retorna as probabilidades de cada classe
        """
        if self.modelo is None:
            raise ValueError("Modelo não foi treinado!")
        
        return self.modelo.predict_proba(X)
    
    def prever_classes(self, X):
        """
        Retorna as classes previstas
        """
        if self.modelo is None:
            raise ValueError("Modelo não foi treinado!")
        
        return self.modelo.predict(X)
    
    def calcular_incerteza(self, X):
        """
        Calcula a incerteza das previsões
        """
        probabilidades = self.prever_probabilidades(X)
        # Entropia como medida de incerteza
        entropia = -np.sum(probabilidades * np.log(probabilidades + 1e-10), axis=1)
        return entropia

def exemplo_classificacao_simples():
    """
    Exemplo de classificação probabilística simples
    """
    print("=== EXEMPLO: CLASSIFICAÇÃO PROBABILÍSTICA SIMPLES ===\n")
    
    # Gera dados sintéticos
    X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, 
                             n_informative=2, n_clusters_per_class=1, 
                             random_state=42)
    
    # Divide em treino e teste
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, 
                                                           random_state=42)
    
    print("1. DADOS:")
    print(f"   Amostras de treino: {X_treino.shape[0]}")
    print(f"   Amostras de teste: {X_teste.shape[0]}")
    print(f"   Número de classes: {len(np.unique(y))}")
    
    # Treina o classificador
    classificador = ClassificadorProbabilistico()
    modelo = classificador.treinar_naive_bayes(X_treino, y_treino)
    
    # Faz previsões
    y_pred = classificador.prever_classes(X_teste)
    probabilidades = classificador.prever_probabilidades(X_teste)
    
    # Calcula métricas
    acuracia = accuracy_score(y_teste, y_pred)
    
    print(f"\n2. RESULTADOS:")
    print(f"   Acurácia: {acuracia:.3f}")
    
    print(f"\n3. PROBABILIDADES DE EXEMPLO:")
    for i in range(5):
        print(f"   Amostra {i+1}:")
        for j, classe in enumerate(classificador.classes):
            print(f"     P(classe {classe}) = {probabilidades[i][j]:.3f}")
        print(f"     Classe prevista: {y_pred[i]}")
        print(f"     Classe real: {y_teste[i]}")
    
    return classificador, X_treino, X_teste, y_treino, y_teste

def exemplo_naive_bayes_texto():
    """
    Exemplo de Naive Bayes para classificação de texto
    """
    print("\n=== EXEMPLO: NAIVE BAYES PARA TEXTO ===\n")
    
    # Dados de exemplo (emails)
    emails = [
        "oferta especial desconto promoção",
        "reunião amanhã projeto importante",
        "ganhe dinheiro rápido fácil",
        "relatório mensal vendas crescimento",
        "clique aqui ganhe prêmio",
        "apresentação cliente proposta negócio",
        "urgente pagamento vencido",
        "treinamento equipe desenvolvimento",
        "gratuito sem custo aproveite",
        "planejamento estratégico empresa"
    ]
    
    # Labels: 0 = spam, 1 = não spam
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    
    print("1. DADOS DE EXEMPLO:")
    for i, email in enumerate(emails):
        tipo = "SPAM" if labels[i] == 0 else "NÃO SPAM"
        print(f"   {tipo}: {email}")
    
    # Converte para matriz de características (bag of words simples)
    todas_palavras = set()
    for email in emails:
        todas_palavras.update(email.split())
    
    todas_palavras = list(todas_palavras)
    
    # Cria matriz de características
    X = np.zeros((len(emails), len(todas_palavras)))
    for i, email in enumerate(emails):
        palavras = email.split()
        for palavra in palavras:
            if palavra in todas_palavras:
                X[i, todas_palavras.index(palavra)] = 1
    
    print(f"\n2. CARACTERÍSTICAS:")
    print(f"   Número de palavras únicas: {len(todas_palavras)}")
    print(f"   Palavras: {todas_palavras}")
    
    # Treina Naive Bayes
    modelo = MultinomialNB()
    modelo.fit(X, labels)
    
    # Testa com novos emails
    novos_emails = [
        "promoção especial desconto",
        "reunião projeto amanhã",
        "ganhe dinheiro fácil"
    ]
    
    print(f"\n3. TESTE COM NOVOS EMAILS:")
    for email in novos_emails:
        # Converte para vetor de características
        X_novo = np.zeros((1, len(todas_palavras)))
        palavras = email.split()
        for palavra in palavras:
            if palavra in todas_palavras:
                X_novo[0, todas_palavras.index(palavra)] = 1
        
        # Faz previsão
        probabilidades = modelo.predict_proba(X_novo)[0]
        classe_predita = modelo.predict(X_novo)[0]
        
        tipo = "SPAM" if classe_predita == 0 else "NÃO SPAM"
        print(f"   Email: {email}")
        print(f"   P(SPAM) = {probabilidades[0]:.3f}")
        print(f"   P(NÃO SPAM) = {probabilidades[1]:.3f}")
        print(f"   Classificação: {tipo}")
        print()

def exemplo_incerteza_previsoes():
    """
    Demonstra como medir incerteza nas previsões
    """
    print("\n=== EXEMPLO: INCERTEZA NAS PREVISÕES ===\n")
    
    # Gera dados com diferentes níveis de separabilidade
    X1, y1 = make_classification(n_samples=500, n_features=2, n_redundant=0, 
                               n_informative=2, n_clusters_per_class=1, 
                               class_sep=2.0, random_state=42)
    
    X2, y2 = make_classification(n_samples=500, n_features=2, n_redundant=0, 
                               n_informative=2, n_clusters_per_class=1, 
                               class_sep=0.5, random_state=42)
    
    print("1. DADOS COM DIFERENTES NÍVEIS DE SEPARABILIDADE:")
    print("   Dataset 1: Classes bem separadas")
    print("   Dataset 2: Classes mal separadas")
    
    # Treina classificadores
    classificador1 = ClassificadorProbabilistico()
    classificador1.treinar_naive_bayes(X1, y1)
    
    classificador2 = ClassificadorProbabilistico()
    classificador2.treinar_naive_bayes(X2, y2)
    
    # Calcula incerteza
    incerteza1 = classificador1.calcular_incerteza(X1)
    incerteza2 = classificador2.calcular_incerteza(X2)
    
    print(f"\n2. ESTATÍSTICAS DE INCERTEZA:")
    print(f"   Dataset 1 - Média: {np.mean(incerteza1):.3f}, Desvio: {np.std(incerteza1):.3f}")
    print(f"   Dataset 2 - Média: {np.mean(incerteza2):.3f}, Desvio: {np.std(incerteza2):.3f}")
    
    # Plota os resultados
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Dataset 1 - Dados
    scatter1 = ax1.scatter(X1[:, 0], X1[:, 1], c=y1, cmap='viridis', alpha=0.7)
    ax1.set_title('Dataset 1: Classes Bem Separadas')
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    
    # Dataset 1 - Incerteza
    scatter2 = ax2.scatter(X1[:, 0], X1[:, 1], c=incerteza1, cmap='Reds', alpha=0.7)
    ax2.set_title('Dataset 1: Incerteza das Previsões')
    ax2.set_xlabel('Feature 1')
    ax2.set_ylabel('Feature 2')
    plt.colorbar(scatter2, ax=ax2)
    
    # Dataset 2 - Dados
    scatter3 = ax3.scatter(X2[:, 0], X2[:, 1], c=y2, cmap='viridis', alpha=0.7)
    ax3.set_title('Dataset 2: Classes Mal Separadas')
    ax3.set_xlabel('Feature 1')
    ax3.set_ylabel('Feature 2')
    
    # Dataset 2 - Incerteza
    scatter4 = ax4.scatter(X2[:, 0], X2[:, 1], c=incerteza2, cmap='Reds', alpha=0.7)
    ax4.set_title('Dataset 2: Incerteza das Previsões')
    ax4.set_xlabel('Feature 1')
    ax4.set_ylabel('Feature 2')
    plt.colorbar(scatter4, ax=ax4)
    
    plt.tight_layout()
    plt.show()
    
    print("\n3. INTERPRETAÇÃO:")
    print("   - Pontos vermelhos indicam alta incerteza")
    print("   - Dataset 2 tem maior incerteza média")
    print("   - Incerteza é maior nas fronteiras entre classes")

def exemplo_comparacao_naive_bayes():
    """
    Compara diferentes tipos de Naive Bayes
    """
    print("\n=== EXEMPLO: COMPARAÇÃO DE NAIVE BAYES ===\n")
    
    # Gera dados
    X, y = make_classification(n_samples=1000, n_features=10, n_redundant=2, 
                             n_informative=8, n_clusters_per_class=1, 
                             random_state=42)
    
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, 
                                                           random_state=42)
    
    # Diferentes tipos de Naive Bayes
    modelos = {
        'GaussianNB': GaussianNB(),
        'MultinomialNB': MultinomialNB(),
        'BernoulliNB': BernoulliNB()
    }
    
    print("1. COMPARAÇÃO DE MODELOS:")
    
    resultados = {}
    for nome, modelo in modelos.items():
        # Treina o modelo
        modelo.fit(X_treino, y_treino)
        
        # Faz previsões
        y_pred = modelo.predict(X_teste)
        probabilidades = modelo.predict_proba(X_teste)
        
        # Calcula métricas
        acuracia = accuracy_score(y_teste, y_pred)
        incerteza_media = np.mean(-np.sum(probabilidades * np.log(probabilidades + 1e-10), axis=1))
        
        resultados[nome] = {
            'acuracia': acuracia,
            'incerteza': incerteza_media
        }
        
        print(f"   {nome}:")
        print(f"     Acurácia: {acuracia:.3f}")
        print(f"     Incerteza média: {incerteza_media:.3f}")
    
    # Plota comparação
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de acurácia
    nomes = list(resultados.keys())
    acuracias = [resultados[nome]['acuracia'] for nome in nomes]
    
    barras1 = ax1.bar(nomes, acuracias, color=['skyblue', 'lightgreen', 'lightcoral'])
    ax1.set_title('Comparação de Acurácia')
    ax1.set_ylabel('Acurácia')
    ax1.set_ylim(0, 1)
    
    for barra, acuracia in zip(barras1, acuracias):
        ax1.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                f'{acuracia:.3f}', ha='center', va='bottom')
    
    # Gráfico de incerteza
    incertezas = [resultados[nome]['incerteza'] for nome in nomes]
    
    barras2 = ax2.bar(nomes, incertezas, color=['skyblue', 'lightgreen', 'lightcoral'])
    ax2.set_title('Comparação de Incerteza')
    ax2.set_ylabel('Incerteza Média')
    
    for barra, incerteza in zip(barras2, incertezas):
        ax2.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                f'{incerteza:.3f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    print(f"\n2. INTERPRETAÇÃO:")
    print("   - GaussianNB: Assume distribuição normal para features contínuas")
    print("   - MultinomialNB: Adequado para contagens de palavras")
    print("   - BernoulliNB: Adequado para features binárias")

def demonstrar_teorema_bayes_naive():
    """
    Demonstra como o Naive Bayes usa o Teorema de Bayes
    """
    print("\n=== TEOREMA DE BAYES NO NAIVE BAYES ===\n")
    
    print("1. FÓRMULA:")
    print("   P(classe | features) = P(features | classe) * P(classe) / P(features)")
    print("   P(classe | features) ∝ P(features | classe) * P(classe)")
    
    print("\n2. ASSUMPÇÃO NAIVE:")
    print("   P(features | classe) = P(f1 | classe) * P(f2 | classe) * ... * P(fn | classe)")
    print("   Assume independência entre features")
    
    print("\n3. VANTAGENS:")
    print("   - Simples de implementar")
    print("   - Funciona bem com poucos dados")
    print("   - Não é sensível a features irrelevantes")
    print("   - Fornece probabilidades de classe")
    
    print("\n4. LIMITAÇÕES:")
    print("   - Assumção de independência pode ser violada")
    print("   - Pode ter performance ruim com features correlacionadas")
    print("   - Sensível à distribuição dos dados")

if __name__ == "__main__":
    # Executa todos os exemplos
    classificador, X_treino, X_teste, y_treino, y_teste = exemplo_classificacao_simples()
    exemplo_naive_bayes_texto()
    exemplo_incerteza_previsoes()
    exemplo_comparacao_naive_bayes()
    demonstrar_teorema_bayes_naive()
