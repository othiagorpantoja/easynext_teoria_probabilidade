# Fórmulas Importantes da Teoria da Probabilidade

**Desenvolvido por:** Thiago Rodrigues Pantoja  
**Empresa:** EasyNext Informática LTDA  
**Emails:** thiago.pantoja@easynext.tech | thiago.pantoja@easynext.consulting  
**Telefones:** (11) 98801-0667 | (92) 98456-1928  
**Data:** Setembro 2025  

## 1. Fórmulas Básicas

### 1.1 Probabilidade de um Evento
```
P(A) = número de resultados favoráveis / número total de resultados
```

### 1.2 Probabilidade do Complementar
```
P(A') = 1 - P(A)
```

### 1.3 Probabilidade da União
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

### 1.4 Probabilidade da Interseção
```
P(A ∩ B) = P(A) + P(B) - P(A ∪ B)
```

## 2. Probabilidade Condicional

### 2.1 Definição
```
P(A|B) = P(A ∩ B) / P(B)
```

### 2.2 Regra da Multiplicação
```
P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)
```

### 2.3 Regra da Multiplicação para Múltiplos Eventos
```
P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) × P(A₂|A₁) × P(A₃|A₁ ∩ A₂) × ... × P(Aₙ|A₁ ∩ A₂ ∩ ... ∩ Aₙ₋₁)
```

## 3. Teorema de Bayes

### 3.1 Fórmula Básica
```
P(A|B) = P(B|A) × P(A) / P(B)
```

### 3.2 Versão Completa
```
P(A|B) = P(B|A) × P(A) / [P(B|A) × P(A) + P(B|A') × P(A')]
```

### 3.3 Teorema de Bayes para Múltiplas Hipóteses
```
P(Aᵢ|B) = P(B|Aᵢ) × P(Aᵢ) / Σⱼ P(B|Aⱼ) × P(Aⱼ)
```

## 4. Independência

### 4.1 Independência de Dois Eventos
```
P(A ∩ B) = P(A) × P(B)
```

### 4.2 Independência Condicional
```
P(A ∩ B|C) = P(A|C) × P(B|C)
```

### 4.3 Independência Mútua
```
P(A₁ ∩ A₂ ∩ ... ∩ Aₙ) = P(A₁) × P(A₂) × ... × P(Aₙ)
```

## 5. Variáveis Aleatórias Discretas

### 5.1 Esperança
```
E[X] = Σ x × P(X = x)
```

### 5.2 Variância
```
Var(X) = E[X²] - (E[X])²
```

### 5.3 Desvio Padrão
```
σ = √Var(X)
```

### 5.4 Esperança de Função
```
E[g(X)] = Σ g(x) × P(X = x)
```

## 6. Variáveis Aleatórias Contínuas

### 6.1 Esperança
```
E[X] = ∫ x × f(x) dx
```

### 6.2 Variância
```
Var(X) = E[X²] - (E[X])²
```

### 6.3 Esperança de Função
```
E[g(X)] = ∫ g(x) × f(x) dx
```

## 7. Distribuições Discretas

### 7.1 Bernoulli
```
P(X = k) = p^k × (1-p)^(1-k), k ∈ {0,1}
E[X] = p
Var(X) = p(1-p)
```

### 7.2 Binomial
```
P(X = k) = C(n,k) × p^k × (1-p)^(n-k)
E[X] = np
Var(X) = np(1-p)
```

### 7.3 Poisson
```
P(X = k) = (λ^k × e^(-λ)) / k!
E[X] = λ
Var(X) = λ
```

### 7.4 Geométrica
```
P(X = k) = (1-p)^(k-1) × p
E[X] = 1/p
Var(X) = (1-p)/p²
```

### 7.5 Hipergeométrica
```
P(X = k) = C(K,k) × C(N-K,n-k) / C(N,n)
E[X] = n × K/N
Var(X) = n × (K/N) × (1-K/N) × (N-n)/(N-1)
```

## 8. Distribuições Contínuas

### 8.1 Uniforme
```
f(x) = 1/(b-a), a ≤ x ≤ b
E[X] = (a+b)/2
Var(X) = (b-a)²/12
```

### 8.2 Normal (Gaussiana)
```
f(x) = (1/√(2πσ²)) × e^(-(x-μ)²/(2σ²))
E[X] = μ
Var(X) = σ²
```

### 8.3 Exponencial
```
f(x) = λe^(-λx), x ≥ 0
E[X] = 1/λ
Var(X) = 1/λ²
```

### 8.4 Gama
```
f(x) = (λ^α × x^(α-1) × e^(-λx)) / Γ(α), x ≥ 0
E[X] = α/λ
Var(X) = α/λ²
```

### 8.5 Beta
```
f(x) = (x^(α-1) × (1-x)^(β-1)) / B(α,β), 0 ≤ x ≤ 1
E[X] = α/(α+β)
Var(X) = (αβ)/((α+β)²(α+β+1))
```

## 9. Distribuições Conjuntas

### 9.1 Probabilidade Conjunta
```
P(X = x, Y = y) = P(X = x) × P(Y = y|X = x)
```

### 9.2 Probabilidade Marginal
```
P(X = x) = Σᵧ P(X = x, Y = y)
```

### 9.3 Covariância
```
Cov(X,Y) = E[XY] - E[X]E[Y]
```

### 9.4 Correlação
```
ρ(X,Y) = Cov(X,Y) / (σₓ × σᵧ)
```

## 10. Teoremas Importantes

### 10.1 Lei dos Grandes Números
```
lim(n→∞) (X₁ + X₂ + ... + Xₙ)/n = E[X]
```

### 10.2 Teorema Central do Limite
```
(X₁ + X₂ + ... + Xₙ - nμ)/(σ√n) → N(0,1)
```

### 10.3 Desigualdade de Chebyshev
```
P(|X - E[X]| ≥ kσ) ≤ 1/k²
```

### 10.4 Desigualdade de Markov
```
P(X ≥ a) ≤ E[X]/a, para a > 0
```

## 11. Fórmulas para Amostragem

### 11.1 Média Amostral
```
x̄ = (x₁ + x₂ + ... + xₙ)/n
```

### 11.2 Variância Amostral
```
s² = Σ(xᵢ - x̄)²/(n-1)
```

### 11.3 Desvio Padrão Amostral
```
s = √s²
```

### 11.4 Erro Padrão da Média
```
SE = σ/√n
```

## 12. Fórmulas para Intervalos de Confiança

### 12.1 Intervalo de Confiança para a Média (σ conhecido)
```
x̄ ± z_(α/2) × σ/√n
```

### 12.2 Intervalo de Confiança para a Média (σ desconhecido)
```
x̄ ± t_(α/2,n-1) × s/√n
```

### 12.3 Intervalo de Confiança para Proporção
```
p̂ ± z_(α/2) × √(p̂(1-p̂)/n)
```

## 13. Fórmulas para Testes de Hipóteses

### 13.1 Estatística Z
```
z = (x̄ - μ₀)/(σ/√n)
```

### 13.2 Estatística t
```
t = (x̄ - μ₀)/(s/√n)
```

### 13.3 Estatística Chi-quadrado
```
χ² = Σ(Oᵢ - Eᵢ)²/Eᵢ
```

### 13.4 Estatística F
```
F = (s₁²/σ₁²)/(s₂²/σ₂²)
```

## 14. Fórmulas para Regressão

### 14.1 Coeficiente de Correlação
```
r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)² × Σ(yᵢ - ȳ)²]
```

### 14.2 Coeficiente de Determinação
```
R² = 1 - (SSE/SST)
```

### 14.3 Erro Quadrático Médio
```
MSE = SSE/(n-2)
```

## 15. Fórmulas para Análise de Variância

### 15.1 Soma dos Quadrados Total
```
SST = Σ(yᵢ - ȳ)²
```

### 15.2 Soma dos Quadrados Entre Grupos
```
SSB = Σ nᵢ(ȳᵢ - ȳ)²
```

### 15.3 Soma dos Quadrados Dentro dos Grupos
```
SSW = Σ Σ(yᵢⱼ - ȳᵢ)²
```

### 15.4 Estatística F para ANOVA
```
F = (SSB/(k-1))/(SSW/(N-k))
```

## 16. Fórmulas para Processos Estocásticos

### 16.1 Cadeia de Markov
```
P(Xₙ₊₁ = j | Xₙ = i) = Pᵢⱼ
```

### 16.2 Probabilidade de Transição
```
P(Xₙ = j | X₀ = i) = (Pⁿ)ᵢⱼ
```

### 16.3 Distribuição Estacionária
```
π = πP
```

## 17. Fórmulas para Teoria da Informação

### 17.1 Entropia
```
H(X) = -Σ P(x) × log₂ P(x)
```

### 17.2 Entropia Condicional
```
H(X|Y) = -Σ P(x,y) × log₂ P(x|y)
```

### 17.3 Informação Mútua
```
I(X;Y) = H(X) - H(X|Y)
```

### 17.4 Divergência de Kullback-Leibler
```
D(P||Q) = Σ P(x) × log₂(P(x)/Q(x))
```

## 18. Fórmulas para Métodos Monte Carlo

### 18.1 Estimador Monte Carlo
```
Î = (1/n) × Σ f(Xᵢ)
```

### 18.2 Variância do Estimador
```
Var(Î) = Var(f(X))/n
```

### 18.3 Erro Padrão
```
SE = √(Var(f(X))/n)
```

## 19. Fórmulas para Filtros Bayesianos

### 19.1 Filtro de Kalman - Predição
```
x̂ₖ₋₁ = Fx̂ₖ₋₁
Pₖ₋₁ = FPₖ₋₁Fᵀ + Q
```

### 19.2 Filtro de Kalman - Atualização
```
Kₖ = Pₖ₋₁Hᵀ(HPₖ₋₁Hᵀ + R)⁻¹
x̂ₖ = x̂ₖ₋₁ + Kₖ(zₖ - Hx̂ₖ₋₁)
Pₖ = (I - KₖH)Pₖ₋₁
```

## 20. Fórmulas para Redes Bayesianas

### 20.1 Probabilidade Conjunta
```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | Pa(Xᵢ))
```

### 20.2 Inferência por Enumeração
```
P(X | e) = α × Σ P(X, e, y)
```

### 20.3 Algoritmo de Eliminação de Variáveis
```
P(X | e) = α × P(X, e)
```

---

**Nota**: Esta é uma compilação das fórmulas mais importantes da teoria da probabilidade. Para aplicações específicas, consulte a documentação detalhada e os exemplos práticos fornecidos no repositório.
