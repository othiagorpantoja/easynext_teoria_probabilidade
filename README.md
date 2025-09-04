# Teoria da Probabilidade 

Este repositório contém exemplos práticos e implementações em Python dos conceitos fundamentais da teoria da probabilidade.

## 👨‍💻 Desenvolvedor

**Desenvolvido por:** Thiago Rodrigues Pantoja  
**Empresa:** EasyNext Informática LTDA  
**Emails:** thiago.pantoja@easynext.tech | thiago.pantoja@easynext.consulting  
**Telefones:** (11) 98801-0667 | (92) 98456-1928  
**Data:** Setembro 2025  

*Para mais informações sobre o desenvolvedor, consulte o arquivo [DESENVOLVEDOR.md](DESENVOLVEDOR.md)*

## 📚 Conceitos Abordados

- **Espaço Amostral**: Conjunto de todos os resultados possíveis
- **Eventos**: Subconjuntos do espaço amostral
- **Probabilidade Condicional**: Probabilidade de um evento dado que outro ocorreu
- **Independência**: Eventos que não se influenciam mutuamente
- **Aplicações em IA**: Uso da probabilidade em sistemas inteligentes

## 🗂️ Estrutura do Projeto

```
├── exemplos_basicos/          # Exemplos fundamentais
│   ├── moeda.py              # Lançamento de moeda
│   ├── dado.py               # Lançamento de dado
│   └── baralho.py            # Sorteio de cartas
├── conceitos_avancados/      # Conceitos mais complexos
│   ├── probabilidade_condicional.py
│   ├── independencia.py
│   └── teorema_bayes.py
├── aplicacoes_ia/           # Aplicações em IA
│   ├── redes_bayesianas.py
│   ├── classificacao_probabilistica.py
│   └── filtro_kalman.py
├── simulacoes/              # Simulações Monte Carlo
│   ├── monte_carlo.py
│   └── caminhada_aleatoria.py
└── teoria/                  # Documentação teórica
    ├── conceitos_fundamentais.md
    └── formulas_importantes.md
```

## 🚀 Como Usar

### Instalação Rápida
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o exemplo principal: `python exemplo_principal.py`

### Executando Exemplos Individuais
```bash
# Exemplos básicos
python exemplos_basicos/moeda.py
python exemplos_basicos/dado.py
python exemplos_basicos/baralho.py

# Conceitos avançados
python conceitos_avancados/probabilidade_condicional.py
python conceitos_avancados/independencia.py
python conceitos_avancados/teorema_bayes.py

# Aplicações em IA
python aplicacoes_ia/redes_bayesianas.py
python aplicacoes_ia/classificacao_probabilistica.py
python aplicacoes_ia/filtro_kalman.py

# Simulações
python simulacoes/monte_carlo.py
python simulacoes/caminhada_aleatoria.py
```

## 📖 Exemplos Rápidos

### Lançamento de Moeda
```python
from exemplos_basicos.moeda import Moeda

moeda = Moeda()
resultado = moeda.lancar()
probabilidade_cara = moeda.probabilidade_cara()
```

### Lançamento de Dado
```python
from exemplos_basicos.dado import Dado

dado = Dado()
resultado = dado.lancar()
probabilidade_par = dado.probabilidade_evento([2, 4, 6])
```

## 🎯 Objetivos de Aprendizado

- Compreender os conceitos fundamentais da probabilidade
- Implementar algoritmos probabilísticos em Python
- Aplicar probabilidade em problemas de IA
- Desenvolver intuição para análise de incerteza

## 📊 Dependências

- Python 3.8+
- NumPy
- Matplotlib
- SciPy
- Pandas

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Adicionar novos exemplos
- Melhorar a documentação
- Corrigir bugs
- Sugerir melhorias

## 📚 Recursos Adicionais

### Documentação Teórica
- `teoria/conceitos_fundamentais.md`: Conceitos básicos e avançados
- `teoria/formulas_importantes.md`: Compilação de fórmulas essenciais

### Exemplos Práticos
- **Exemplos Básicos**: Moeda, dado, baralho com visualizações
- **Conceitos Avançados**: Probabilidade condicional, independência, Teorema de Bayes
- **Aplicações em IA**: Redes Bayesianas, classificação probabilística, Filtro de Kalman
- **Simulações**: Monte Carlo, caminhadas aleatórias

### Características dos Exemplos
- ✅ Código comentado e didático
- ✅ Visualizações com matplotlib
- ✅ Comparação entre teoria e prática
- ✅ Simulações Monte Carlo
- ✅ Aplicações reais em IA

## 🎯 Público-Alvo

- Estudantes de matemática e estatística
- Desenvolvedores interessados em IA
- Profissionais que trabalham com dados
- Qualquer pessoa interessada em probabilidade

## 🔧 Requisitos do Sistema

- Python 3.8+
- 4GB RAM (recomendado)
- 500MB de espaço em disco

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
