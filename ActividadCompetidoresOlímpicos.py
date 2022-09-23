# Databricks notebook source
import pandas as pd
import numpy as np
path='/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
df_Olimpicos = pd.read_csv(path)
df_Olimpicos.head()

# COMMAND ----------

df_Olimpicos[df_Olimpicos["Age"]==df_Olimpicos["Age"].max()]

# COMMAND ----------

filter1=['ARG','COL','MEX']
df_OlimpicosACM=df_Olimpicos[df_Olimpicos['NOC'].isin(filter1)]
df_OlimpicosACM=df_OlimpicosACM.dropna(subset=['Medal'])
df_OlimpicosACM2=df_OlimpicosACM.groupby(['NOC'])['Age'].transform(max) == df_OlimpicosACM['Age']
df_OlimpicosACM[df_OlimpicosACM2].sort_values(by=['Age'])

# COMMAND ----------

filter2=['USA','CAN']
filter3=['Gold']
df_OlimpicosUC=df_Olimpicos[df_Olimpicos['NOC'].isin(filter2) & df_Olimpicos['Medal'].isin(filter3)]
df_OlimpicosUC2=df_OlimpicosUC.groupby(['NOC'])['Age'].transform(min) == df_OlimpicosUC['Age']
df_OlimpicosUC[df_OlimpicosUC2].sort_values(by=['Age'])

# COMMAND ----------

filter4=['USA','CHN','RUS']
df_OlimpicosUCR=df_Olimpicos[['Medal','NOC','Name']][df_Olimpicos['NOC'].isin(filter4)]
df_OlimpicosUCR=df_OlimpicosUCR.dropna(subset=['Medal'])
#df_Olimpicosfin['Counter']=1
df_OlimpicosUCR=df_OlimpicosUCR.groupby(['Name','NOC'])['Medal'].count().sort_values(ascending=False).head(5).reset_index()
print('El competidor que ha ganado más medallas en la historia es: ')
df_OlimpicosUCR.style.apply(lambda x: ['background: yellow' 
                                          if x.Medal == df_OlimpicosUCR.loc[0]['Medal']
                                      else '' for i in x], axis=1)

# COMMAND ----------

filter4=['USA','CHN','RUS']
filter5=['Gold']
df_OlimpicosUCR=df_Olimpicos[['Medal','NOC','Name']][df_Olimpicos['NOC'].isin(filter4) & df_Olimpicos['Medal'].isin(filter5)]
df_OlimpicosUCR=df_OlimpicosUCR.dropna(subset=['Medal'])
#df_Olimpicosfin['Counter']=1
df_OlimpicosUCR=df_OlimpicosUCR.groupby(['Name','NOC'])['Medal'].count().sort_values(ascending=False).head(5).reset_index()
print('El competidor que ha ganado más medallas de Oro en la historia es: ')
df_OlimpicosUCR.style.apply(lambda x: ['background: yellow' 
                                          if x.Medal == df_OlimpicosUCR.loc[0]['Medal']
                                      else '' for i in x], axis=1)

# COMMAND ----------

filter4=['USA','CHN','RUS']
filter6=['Silver']
df_OlimpicosUCR=df_Olimpicos[['Medal','NOC','Name']][df_Olimpicos['NOC'].isin(filter4) & df_Olimpicos['Medal'].isin(filter6)]
df_OlimpicosUCR=df_OlimpicosUCR.dropna(subset=['Medal'])
#df_Olimpicosfin['Counter']=1
df_OlimpicosUCR=df_OlimpicosUCR.groupby(['Name','NOC'])['Medal'].count().sort_values(ascending=False).head(5).reset_index()
print('El competidor que ha ganado más medallas de Plata en la historia es: ')
df_OlimpicosUCR.style.apply(lambda x: ['background: lightgray' 
                                          if x.Medal == df_OlimpicosUCR.loc[0]['Medal']
                                      else '' for i in x], axis=1)

# COMMAND ----------

filter4=['USA','CHN','RUS']
filter7=['Bronze']
df_OlimpicosUCR=df_Olimpicos[['Medal','NOC','Name']][df_Olimpicos['NOC'].isin(filter4) & df_Olimpicos['Medal'].isin(filter7)]
df_OlimpicosUCR=df_OlimpicosUCR.dropna(subset=['Medal'])
#df_Olimpicosfin['Counter']=1
df_OlimpicosUCR=df_OlimpicosUCR.groupby(['Name','NOC'])['Medal'].count().sort_values(ascending=False).head(5).reset_index()
print('El competidor que ha ganado más medallas de Bronce en la historia es: ')
df_OlimpicosUCR.style.apply(lambda x: ['background: gold' 
                                          if x.Medal == df_OlimpicosUCR.loc[0]['Medal']
                                      else '' for i in x], axis=1)
