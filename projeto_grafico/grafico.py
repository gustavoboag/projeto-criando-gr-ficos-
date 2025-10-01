import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Configurações gerais
plt.rcParams['figure.figsize'] = (10, 6)

# 1. GRÁFICO DE HISTOGRAMA - Distribuição de Descontos
plt.figure(1)
plt.hist(df['Desconto'].dropna(), bins=15, alpha=0.7, color='#DC143C', edgecolor='black', density=True)
plt.title('Distribuição de Descontos Aplicados', fontsize=14, fontweight='bold')
plt.xlabel('Desconto (%)')
plt.ylabel('Densidade')
plt.axvline(df['Desconto'].mean(), color='red', linestyle='--', linewidth=2, label=f'Média: {df["Desconto"].mean():.1f}%')
plt.axvline(df['Desconto'].median(), color='orange', linestyle='--', linewidth=2, label=f'Mediana: {df["Desconto"].median():.1f}%')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()



# 2. GRÁFICO DE DISPERSÃO - Preço vs Número de Avaliações
plt.figure(2)
plt.scatter(df['Preço'], df['N_Avaliações'], alpha=0.6, color='coral')
plt.title('Relação: Preço vs Número de Avaliações', fontsize=14, fontweight='bold')
plt.xlabel('Preço (R$)')
plt.ylabel('Número de Avaliações')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()




# 3. MAPA DE CALOR - Correlação entre variáveis numéricas
plt.figure(3)
numeric_cols = ['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
plt.title('Mapa de Calor - Correlação entre Variáveis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()





# 4. GRÁFICO DE BARRA - Top 10 marcas por frequência
plt.figure(4)
top_marcas = df.groupby('Marca').size().sort_values(ascending=False).head(10)
colors = plt.cm.Set3(np.linspace(0, 1, len(top_marcas)))
top_marcas.plot(kind='bar', color=colors)
plt.title('Top 10 Marcas Mais Frequentes', fontsize=14, fontweight='bold')
plt.xlabel('Marca')
plt.ylabel('Quantidade de Produtos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





# 5. GRÁFICO DE PIZZA - Distribuição por Gênero (AGRUPAÇÃO CORRIGIDA)
plt.figure(5)

# Agrupar categorias: Meninos → Masculino, Meninas → Feminino
df_genero_agrupado = df.copy()
df_genero_agrupado['Gênero_Agrupado'] = df_genero_agrupado['Gênero'].replace({
    'Meninos': 'Masculino',
    'Meninas': 'Feminino',
    'Sem gênero infantil': 'Sem gênero',
    'Bebês': 'Sem gênero',
    'Unissex': 'Sem gênero',
    'Unissex rupa para gordinha pluss P ao 52': 'Sem gênero',
    'Sem gênero': 'Sem gênero'})

# Manter apenas as três categorias principais
genero_filtrado = df_genero_agrupado[df_genero_agrupado['Gênero_Agrupado'].isin(['Masculino', 'Feminino', 'Sem gênero'])]
genero_dist = genero_filtrado['Gênero_Agrupado'].value_counts()

colors = ['#66b3ff', '#ff9999', '#99ff99']  # Azul, Rosa, Verde
plt.pie(genero_dist.values, labels=genero_dist.index, autopct='%1.1f%%',
        startangle=90, colors=colors, shadow=True, explode=(0.05, 0.05, 0.05))
plt.title('Distribuição de Produtos por Gênero', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()






# 6. GRÁFICO DE DENSIDADE - Distribuição de preços
plt.figure(6)
df['Preço'].plot(kind='density', color='purple', linewidth=2)
plt.title('Densidade de Distribuição de Preços', fontsize=14, fontweight='bold')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()





# 7. GRÁFICO DE REGRESSÃO - Preço vs Desconto
plt.figure(7)
sns.regplot(x='Preço', y='Desconto', data=df,
            scatter_kws={'alpha':0.6, 'color':'purple', 's':50},
            line_kws={'color':'yellow', 'linewidth':3})
plt.title('Relação: Preço vs Desconto Aplicado', fontsize=14, fontweight='bold')
plt.xlabel('Preço (R$)')
plt.ylabel('Desconto (%)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
