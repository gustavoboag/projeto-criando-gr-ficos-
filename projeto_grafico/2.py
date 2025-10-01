import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Carregar os dados
df = pd.read_csv('ecommerce_estatistica.csv')
# Configurações gerais
plt.rcParams['figure.figsize'] = (10, 6)

# 2. GRÁFICO DE HISTOGRAMA - Distribuição de Preços (SEGUNDO MELHOR)
plt.figure(2)
plt.hist(df['Preço'].dropna(), bins=20, alpha=0.7, color='#4682B4', edgecolor='black', density=True)
plt.title('Distribuição de Preços dos Produtos', fontsize=14, fontweight='bold')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.axvline(df['Preço'].mean(), color='red', linestyle='--', linewidth=2, label=f'Média: R$ {df["Preço"].mean():.2f}')
plt.axvline(df['Preço'].median(), color='orange', linestyle='--', linewidth=2, label=f'Mediana: R$ {df["Preço"].median():.2f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()



# 1. GRÁFICO DE HISTOGRAMA - Distribuição das notas
plt.figure(1)
plt.hist(df['Nota'].dropna(), bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribuição das Notas dos Produtos', fontsize=14, fontweight='bold')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

