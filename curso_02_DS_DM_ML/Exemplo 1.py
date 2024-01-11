# -*- coding: utf-8 -*-
"""Novo_Exemplo_1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JN3zenBCzGaPEa2M8osSP1wROO14TaLF

#CURSO 2 - CIENCIA DE DADOS, APRENDIZADO DE MÁQUINA e DATA MINING
##PROFa. Roseli A F Romero


# Exercício 01
## Exploração e visualização de dados
 


## Dados unidimensionais
## Dados multidimensionais
"""

# Permissão de leitura para o Drive
# Autorize o Collab a acessar seus arquivos no drive
from google.colab import drive
drive.mount('/content/drive')

"""Considerando dados de duas cidades diferentes fornecendo as temperaturas máximas (celsius) durante diferente dias do ano.
Os dados foram disponibilizados nos arquivos "cidade_1.txt" e "cidade_2.txt".

As leituras estão em ordem cronológica, porém, o sensor da cidade 1 falhou em alguns dias. Nesses casos, a leitura foi substituida pelo o caracter "?".

### Questão 0
- Substitua os valores faltantes pela média das leituras do dia anterior e do dia seguinte.
"""

import numpy as np
import pandas as pd

# leia o arquivo da cidade 1
with open("/content/drive/MyDrive/Colab Notebooks/Curso 2/Arquivos/cidade_1.txt") as f: #abrir o arquivo como f
    cidade_1_lines = f.readlines() #estruturar as linhas e chamar de cidade_1_lines
for i in range(0,len(cidade_1_lines)):
  if cidade_1_lines[i] == "?\n":
    cidade_1_lines[i] = (float(cidade_1_lines[i-1])+float(cidade_1_lines[i+1]))/2 #média do anterior e posterior
cidade_1 = np.array([float(x) for x in cidade_1_lines]) #transforma tudo em um array float?

# lendo arquivo da cidade 2
with open("/content/drive/MyDrive/Colab Notebooks/Curso 2/Arquivos/cidade_2.txt") as f:
    cidade_2_lines = f.readlines()
cidade_2 = np.array([float(x) for x in cidade_2_lines])

from google.colab import drive #permissão para o colap acessar os arquivos no drive
drive.mount('/content/drive')

"""### Questão 01. 
Consideramos um dia como quente caso sua temperatura máxima tenha sido maior ou igual 25 graus celsius.

1. Calcule a média de temperatura no ano para cada cidade.

2. Demonstre visualmente o porque essa métrica não é uma boa forma de estimarmos qual cidade teve mais dias quente.

   - Dica: Transforme os arrays de cada cidade em estruturas do tipo `DataFrame` da biblioteca **pandas** e utilize as funções de histograma e/ou boxplot.
"""

import seaborn as sns
from matplotlib import pyplot as plt
print('Media cidade 1: ', np.mean(cidade_1))
print('Media cidade 2: ', np.mean(cidade_2))
print('\n')
#gráfico de distribuição de cada cidade
sns.distplot(cidade_1, bins=20, color="red")
sns.distplot(cidade_2, bins=20, color = "purple")

import pandas as pd
import numpy as np
#transformando os dados em um único df
cidades = pd.DataFrame({'Cidade': (['SCarlos']*len(cidade_1)) + (['Rio_Claro']*len(cidade_2)),
                        'Temperatura': np.concatenate([cidade_1, cidade_2])})
sns.boxplot(x='Cidade', y='Temperatura', data=cidades, showmeans=True) #showmeans mostra media

"""Apesar da média da cidade 2 ser maior, percebemos que são apenas alguns outliers que puxam seu valor para cima. Pelo bloxplot, percebemos também que a cidade 1 teve uma variância menor do que a cidade 2.

---

### Questão 02.
1. Calcule o número de dias quentes em cada cidade.
- Dica: Use a função `argwhere` da biblioteca **numpy**.
"""

#Dias quentes cidade 1
dias_quentes_1 = np.argwhere(cidade_1>=25) #
print("Numero de Dias quentes cidade 1:" , len(dias_quentes_1))

#Dias quentes cidade 2
dias_quentes_2 = np.argwhere(cidade_2>=25)
print("Numero de Dias quentes cidade 2:" , len(dias_quentes_2))

"""## Dados multidimensionais

Considere o conjunto de dados dos jogadores de futebol, que está no formato .csv.



"""

players = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Curso 2/Arquivos/jogadores_exercicio1.csv")
players

"""

---


### Questão 03.

1. Calcule os quatro momentos (média, variância, obliquidade e achatamento) para cada atributo do tipo numerico (float) do conjunto.
"""

#Média .mean()
media_altura = players['height'].mean()
media_peso = players['weight'].mean()
media_idade = players['age'].mean()
print("Média de altura é:", media_altura, "\n","Média de peso é:", media_peso, "\n","Média de idade é:", media_idade)
print("\n")

#variância .var()
var_altura = players['height'].var()
var_peso = players['weight'].var()
var_idade = players['age'].var()
print("Variância de altura é:", var_altura, "\n","Variância de peso é:", var_peso, "\n","Variância de idade é:", var_idade)

print("\n")

#obliquidade .skew()   -- inclinação
obliq_altura = players['height'].skew()
obliq_peso = players['weight'].skew()
obliq_idade = players['age'].skew()  
print("Obliquidade de altura é:", obliq_altura,"\n","Obliquidade de peso é:", obliq_peso,"\n","Obliquidade de idade é:", obliq_idade)

print("\n")

#
kurt_altura = players['height'].kurtosis()
kurt_peso = players['weight'].kurtosis()
kurt_idade = players['age'].kurtosis()
print("Achatamento de altura é:", kurt_altura,"\n","Achatamento de peso é:", kurt_peso, "\n","Achatamento de idade é:", kurt_idade)

"""

---

### Questão 04.

1. Gere o boxplot de atributo Height do conjunto, analise se os dados estão centrados (simetria) e estime os quartis deste atributo.  
"""

from scipy import stats
#Boxplot e análise da altura
boxplot_height = players.boxplot(column='height', showmeans=True)
print('Obliquidade: {}'.format(stats.skew(players.height))) #bibli.fun(df.colun)

#quartis/quantile
print('25 %:', players.height.quantile(0.25)) #1
print('50 %:', players.height.quantile(0.5)) #2 -- mediana
print('75 %:', players.height.quantile(0.75)) #3

print('Media: ', players.height.mean())
print('Mediana: ', players.height.median())

"""Observamos uma sutil diferença entre a média e mediana, mostrando que os dados não estão perfeitamente centralizados mas sua obliquidade é desconsiderável.

Podemos confirmar calculando diretamente a obliquidade da distribuição, que teve resultado negativo porém perto de 0, indicando que a distribuição tem uma cauda à esquerda porém não muito significativa.

### Questão 05.
O arquivo **player_attributes.csv** contém mais informações sobre os jogadores. Leia-o como DataFrame e combine suas informações com o DataFrame já existente.

1. Caso um atributo não esteja disponível para algum jogador, substitua o valor NaN pela média ou valor mais comum para aquele atributo.

2. Calcule a moda de cada atributo após a combinação das bases. 

- Dica: Utilize a função [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) para combinar dois DataFrames que contém ao menos um atributo em comum

- Dica 2: Ambos DataFrames possuem o atributo "player_api_id"
"""

players_attrs = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Curso 2/Arquivos/player_attributes1.csv")
# o parâmetro how poderia ter outros valores que também funcionam
jogadores = players.merge(players_attrs, how='right', on='player_api_id') #primeiro_df.merge(segundo_df)

# Usando a moda ou média dependendo do tipo do atributo.
# Como o enunciado estava ambíguo, aceitei que usou só a moda
jogadores.apply(lambda x:x.fillna(
    x.mode()[0] if x.dtype == 'object' else x.mean(), axis=0, inplace=True))

for column in jogadores.columns:
  if 'id' not in column:
    print('Atributo: ', column, ' Resultado: ', jogadores[column].mode()[0])