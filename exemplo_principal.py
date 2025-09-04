"""
Exemplo Principal - Teoria da Probabilidade
Demonstra como usar os diferentes módulos do repositório
"""

import sys
import os

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def demonstrar_exemplos_basicos():
    """
    Demonstra os exemplos básicos de probabilidade
    """
    print("=" * 60)
    print("DEMONSTRAÇÃO DOS EXEMPLOS BÁSICOS")
    print("=" * 60)
    
    try:
        from exemplos_basicos.moeda import demonstrar_conceitos
        print("\n1. LANÇAMENTO DE MOEDA:")
        demonstrar_conceitos()
        
        from exemplos_basicos.dado import demonstrar_eventos
        print("\n2. LANÇAMENTO DE DADO:")
        demonstrar_eventos()
        
        from exemplos_basicos.baralho import demonstrar_eventos_baralho
        print("\n3. SORTEIO DE CARTAS:")
        demonstrar_eventos_baralho()
        
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")
        print("Certifique-se de que todos os arquivos estão no diretório correto.")

def demonstrar_conceitos_avancados():
    """
    Demonstra os conceitos avançados de probabilidade
    """
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO DOS CONCEITOS AVANÇADOS")
    print("=" * 60)
    
    try:
        from conceitos_avancados.probabilidade_condicional import exemplo_dados_soma
        print("\n1. PROBABILIDADE CONDICIONAL:")
        exemplo_dados_soma()
        
        from conceitos_avancados.independencia import exemplo_dados_independencia
        print("\n2. INDEPENDÊNCIA DE EVENTOS:")
        exemplo_dados_independencia()
        
        from conceitos_avancados.teorema_bayes import exemplo_doenca_teste
        print("\n3. TEOREMA DE BAYES:")
        exemplo_doenca_teste()
        
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")

def demonstrar_aplicacoes_ia():
    """
    Demonstra as aplicações em inteligência artificial
    """
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO DAS APLICAÇÕES EM IA")
    print("=" * 60)
    
    try:
        from aplicacoes_ia.redes_bayesianas import exemplo_rede_simples
        print("\n1. REDES BAYESIANAS:")
        exemplo_rede_simples()
        
        from aplicacoes_ia.classificacao_probabilistica import exemplo_classificacao_simples
        print("\n2. CLASSIFICAÇÃO PROBABILÍSTICA:")
        exemplo_classificacao_simples()
        
        from aplicacoes_ia.filtro_kalman import exemplo_movimento_retilineo
        print("\n3. FILTRO DE KALMAN:")
        exemplo_movimento_retilineo()
        
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")

def demonstrar_simulacoes():
    """
    Demonstra as simulações Monte Carlo
    """
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO DAS SIMULAÇÕES")
    print("=" * 60)
    
    try:
        from simulacoes.monte_carlo import exemplo_soma_dados
        print("\n1. SIMULAÇÃO MONTE CARLO:")
        exemplo_soma_dados()
        
        from simulacoes.caminhada_aleatoria import exemplo_caminhada_simples
        print("\n2. CAMINHADA ALEATÓRIA:")
        exemplo_caminhada_simples()
        
    except ImportError as e:
        print(f"Erro ao importar módulos: {e}")

def menu_principal():
    """
    Menu principal para escolher qual demonstração executar
    """
    while True:
        print("\n" + "=" * 60)
        print("REPOSITÓRIO DE TEORIA DA PROBABILIDADE - EASYNEXT")
        print("=" * 60)
        print("Escolha uma opção:")
        print("1. Exemplos Básicos (Moeda, Dado, Baralho)")
        print("2. Conceitos Avançados (Prob. Condicional, Independência, Bayes)")
        print("3. Aplicações em IA (Redes Bayesianas, Classificação, Filtro Kalman)")
        print("4. Simulações (Monte Carlo, Caminhada Aleatória)")
        print("5. Executar Todas as Demonstrações")
        print("0. Sair")
        print("=" * 60)
        
        opcao = input("Digite sua opção (0-5): ").strip()
        
        if opcao == "0":
            print("Obrigado por usar o repositório de Teoria da Probabilidade!")
            break
        elif opcao == "1":
            demonstrar_exemplos_basicos()
        elif opcao == "2":
            demonstrar_conceitos_avancados()
        elif opcao == "3":
            demonstrar_aplicacoes_ia()
        elif opcao == "4":
            demonstrar_simulacoes()
        elif opcao == "5":
            demonstrar_exemplos_basicos()
            demonstrar_conceitos_avancados()
            demonstrar_aplicacoes_ia()
            demonstrar_simulacoes()
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

def verificar_dependencias():
    """
    Verifica se as dependências necessárias estão instaladas
    """
    print("Verificando dependências...")
    
    dependencias = [
        'numpy',
        'matplotlib',
        'scipy',
        'pandas',
        'seaborn',
        'sklearn'
    ]
    
    dependencias_faltando = []
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"✓ {dep}")
        except ImportError:
            print(f"✗ {dep} - NÃO INSTALADO")
            dependencias_faltando.append(dep)
    
    if dependencias_faltando:
        print(f"\nDependências faltando: {', '.join(dependencias_faltando)}")
        print("Instale com: pip install " + " ".join(dependencias_faltando))
        return False
    else:
        print("\n✓ Todas as dependências estão instaladas!")
        return True

def main():
    """
    Função principal
    """
    print("Bem-vindo ao Repositório de Teoria da Probabilidade!")
    print("Este repositório contém exemplos práticos e implementações")
    print("dos conceitos fundamentais da teoria da probabilidade.")
    
    # Verifica dependências
    if not verificar_dependencias():
        print("\nPor favor, instale as dependências faltando antes de continuar.")
        return
    
    # Executa o menu principal
    menu_principal()

if __name__ == "__main__":
    main()
