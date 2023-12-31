# -*- coding: utf-8 -*-
"""Analise games.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IaiP-7dBZuR_a1uju5pLOTMu2ELQOFMp

Análise mercado de games
"""

# Libs para Modelagem e Matrizez
import numpy as np
import pandas as pd

# Libs para análises gráficas
import matplotlib.pyplot as plt
import seaborn as sns

# Lib para ignorar avisos
import warnings
warnings.filterwarnings('ignore')

bd = pd.read_csv('PS4_GamesSales.csv', encoding='latin-1') #encoding para ler

bd.head()

bd.shape # dimensão

# campos nulos
bd.isnull().sum()

# Gráfico de Nulos
plt.figure(figsize=(14,5))
plt.title('Verificando Campos Nulos')
sns.heatmap(bd.isnull(), cbar=False);

#retirando valores nulos
bd.dropna(inplace=True)

# Estatisticas
bd.describe()

"""Analisando o valor de vendas ao longo dos anos."""

# tamanho da imagem
plt.figure(figsize=(10,5))

# titulo
plt.title('Quantidade de Vendas Globais (mi)', loc='left', fontsize=14)

# Grafico
sns.barplot(data=bd, x='Year', y='Global', ci=None, color='#69b3a2', estimator=sum)#ci=None retira a linha no grafico de barra
# label
plt.ylabel('Quantidade de Vendas (mi)')

# retirar 2019, 2020
bd = bd.loc[ (bd['Year'] != 2019) &  (bd['Year'] != 2020)]
# verificar
bd.head()

# Conferindo valores únicos dos anos
bd.loc[ (bd['Year'] != 2019) &  (bd['Year'] != 2020)]['Year'].unique()

plt.figure( figsize=(12,5))

# estilo
plt.style.use('ggplot')
plt.title('Distribuição de Vendas Globais', loc='left', fontsize=14)
# plot
sns.kdeplot(bd['Global'], shade=True, bw=1, color='#96a8aB', linewidth=2.5);

bd.groupby(by=['Year']).sum()

# tamanho
plt.figure(figsize=(10,4))
plt.title('Análise da Distribuição Global')
sns.boxplot(data=bd, x='Year', y='Global')

bd.loc[bd['Global']>= 10]

bd

Analise = bd.groupby(by=['Year']).sum().reset_index()
America = [America / Total * 100 for America, Total in zip( Analise['North America'], Analise['Global'] ) ]
Europa = [Europa / Total * 100 for Europa, Total in zip(Analise['Europe'], Analise['Global'])]
Japão = [Japão / Total * 100 for Japão, Total in zip(Analise['Japan'], Analise['Global'])]
Mundo = [ Mundo / Total * 100 for Mundo, Total in zip( Analise['Rest of World'], Analise['Global'] ) ]

America, Europa, Japão, Mundo

Analise

from matplotlib.offsetbox import bbox_artist
# grafico de barra

# tamanho
plt.figure(figsize=(10,5))

#largura da barra no grafico
largura = 0.85
rotulos = Analise['Year']
grupos = [0,1,2,3,4,5]

#plot America
plt.bar(grupos, America, width=largura, color='#b5ffb9', edgecolor='white')

#plot Europa
plt.bar(grupos, Europa, bottom=America, width=largura, color='#f9bc86', edgecolor='white')

#plot japão
plt.bar(grupos, Japão, bottom=[A + B for A, B in zip(America, Europa)], width=largura, color='#a3acff', edgecolor='white')

#plot mundo

plt.bar(grupos, Mundo, bottom=[A + B + C for A, B, C in zip(America, Europa, Japão)], width=largura, color='#d3acfe', edgecolor='white')


# labels
plt.xticks(grupos, rotulos)
plt.xlabel('Grupo')
plt.ylabel('Distribuição %')

# legenda
plt.legend(['America N', 'Europa', 'Japão', 'Mundo'], loc='upper left', bbox_to_anchor=(0.15, -0.1), ncol=4 )


plt.title('Análise Distribuição por Continente');

bd['Publisher'].unique();

# converter os dados em valor quantitativo

from sklearn.preprocessing import LabelEncoder


funcaolabel = LabelEncoder()

bd['Produtor'] = funcaolabel.fit_transform(bd['Publisher'])
bd['Genero'] = funcaolabel.fit_transform(bd['Genre'])
bd['Jogo'] = funcaolabel.fit_transform(bd['Game'])

bd.head();

paleta = sns.color_palette('husl', 8);

plt.figure(figsize=(20,5))
plt.title('Análise dos produtores de Game (mi)')
sns.scatterplot(data=bd, x='Produtor', y='Global', color=paleta[0]);

plt.figure(figsize=(20,5))
plt.title('Análise Gênero de Games(mi)')
sns.scatterplot(data=bd, x='Genero', y='Global', color=paleta[0]);

plt.figure(figsize=(20,5))
plt.title('Análise de Games (mi)')
sns.scatterplot(data=bd, x='Jogo', y='Global', color=paleta[0]);

"""# **Relatório Completo**"""

# Tamanho da Imagem
fig, ax = plt.subplots( figsize=(18, 15) )

# Cor de fundo
Cor_Fundo = '#f5f5f5'
ax.set_facecolor( Cor_Fundo )
fig.set_facecolor( Cor_Fundo )

# Estilo dos gráficos
plt.style.use('seaborn')

# Titulo da figura
plt.suptitle(' Análise Mercado de Games PS4', fontsize=22, color='#404040', fontweight=600 )

# Parametros para o grid
Linhas = 3
Colunas = 2

# Acessando gráfico 1
plt.subplot( Linhas, Colunas, 1)

# Titulo
plt.title('Quantidade de Vendas Globais (mi)', loc='left', fontsize=14 )

# Grafico
plt.bar( bd['Year'], bd['Global'], color='#69b3a2' )

# Label
plt.ylabel('Quantidade Vendas (mi)')


# Acessando gráfico 2
plt.subplot( Linhas, Colunas, 2)

# titulo
plt.title('Análise da distribuição Global (mi)')

# Plot
sns.boxplot( data=bd, x='Year', y='Global')


# Acessando gráfico 3

plt.subplot( Linhas, Colunas, 3)

# LArgura barra no gráfico
largura = 0.85
rotulos = Analise['Year']
grupos = [0, 1, 2, 3, 4, 5]

# titulo
plt.title('Análise distribuição por continentes', loc='left', fontsize=14)

# Plot da America
plt.bar( grupos, America, width=largura, color='#b5ffb9', edgecolor='white' )

# Plot da Europa
plt.bar( grupos, Europa, bottom=America, width=largura, color='#f9bc86', edgecolor='white' )

# Plot do Japao
plt.bar( grupos, Japão, bottom=[ A + B for A, B in zip(America, Europa) ], width=largura, color='#a3acff', edgecolor='white' )

# Plot do Resto do mundo
plt.bar( grupos, Mundo, bottom=[ A + B + C for A, B, C in zip(America, Europa, Japão) ], width=largura, color='#d3acfe', edgecolor='white' )

# Labels
plt.xticks( grupos, rotulos )
plt.xlabel('Grupo')
plt.ylabel('Distribuição %')

# Legenda
plt.legend( ['America N', 'Europa',' Japão', 'Mundo'], loc='upper left', bbox_to_anchor=(0.15, -0.1), ncol=4 );


# Acessando gráfico 4
plt.subplot( Linhas, Colunas, 4)
plt.title('Análise dos produtores de Game (mi)', loc='left', fontsize=14 )
sns.scatterplot(data=bd, x='Produtor', y='Global', color=paleta[0] );


# Acessando gráfico 5
plt.subplot( Linhas, Colunas, 5)
plt.title('Análise dos generos do Game (mi)', loc='left', fontsize=14)
sns.scatterplot(data=bd, x='Genero', y='Global', color=paleta[0] );


# Acessando gráfico 6
plt.subplot( Linhas, Colunas, 6)
plt.title('Análise dos Games (mi)', loc='left', fontsize=14)
sns.scatterplot(data=bd, x='Jogo', y='Global', color=paleta[0] );


# Ajustar o layout
plt.subplots_adjust( hspace=0.35, wspace=0.15 )

# Rodapé
Rodape = '''
Relatório Elaborado
'''

# Incluindo o rodape no relatorio
fig.text( 0.5, -0.02, Rodape, ha='center', va='bottom', size=12, color='#938ca1');

