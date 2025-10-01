# 📊 Análise Estatística de E-commerce

Este projeto realiza uma análise estatística completa de dados de e-commerce, explorando padrões de vendas, avaliações de produtos, preços e comportamento do consumidor através de visualizações interativas.

## 📋 Sobre o Projeto

O projeto analisa um dataset de produtos de e-commerce contendo informações sobre:
- **Avaliações e notas** dos produtos
- **Preços e descontos** aplicados
- **Marcas e materiais** dos produtos
- **Vendas e engajamento** dos clientes
- **Segmentação** por gênero e categoria

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** - Manipulação de dados
- **Matplotlib** - Visualizações gráficas
- **Seaborn** - Visualizações estatísticas avançadas
- **NumPy** - Cálculos numéricos

## 📁 Estrutura do Projeto
ecommerce-analysis/
│
├── ecommerce_estatistica.csv # Dataset principal
├── analise_ecommerce.py # Script de análise principal
└── README.md # Este arquivo




## 📊 Gráficos e Análises Implementadas

### 1. 📈 **Histogramas (Melhores Distribuições)**
- Distribuição das notas dos produtos
- Distribuição de preços
- Distribuição de descontos aplicados
- Distribuição do número de avaliações
- Notas por faixa de preço
- Comparação de notas por gênero

### 2. 🔍 **Gráficos de Dispersão**
- Relação entre preço e número de avaliações
- Desconto vs preço (colorido por nota)

### 3. 🌡 **Mapa de Calor**
- Matriz de correlação entre variáveis numéricas
- Identificação de relações estatísticas significativas

### 4. 📊 **Gráficos de Barras**
- Top 10 marcas mais frequentes
- Top 8 materiais mais utilizados

### 5. 🥧 **Gráfico de Pizza**
- Distribuição de produtos por gênero (Masculino, Feminino, Sem gênero)
- Agrupamento inteligente de categorias

### 6. 📉 **Gráficos de Densidade**
- Distribuição de probabilidade dos preços
- Análise de concentração de valores

### 7. 📐 **Gráficos de Regressão (Melhores Comparações)**
- Nota vs Preço
- Nota vs Número de avaliações
- Preço vs Desconto
- Nota vs Quantidade vendida
- Gráfico múltiplo (Nota, Preço e Desconto)

### 8. 📦 **Boxplots**
- Distribuição de notas por gênero
- Análise de outliers e variabilidade

## 🎯 Insights Principais

### 📈 **Padrões de Qualidade**
- Distribuição de notas concentrada acima de 4.0
- Relação entre preço e qualidade dos produtos
- Impacto das avaliações nas vendas

### 💰 **Estratégia de Preços**
- Faixas de preço mais comuns
- Políticas de desconto aplicadas
- Segmentação por valor

### 👥 **Comportamento do Consumidor**
- Preferências por gênero
- Engajamento por tipo de produto
- Padrões de compra por categoria

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install pandas matplotlib seaborn numpy
