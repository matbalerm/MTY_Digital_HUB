# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
df_Olimpicos = pd.read_csv(path)
df_Olimpicos.head()

# COMMAND ----------

df_Olimpicos['Medal'].unique()


# COMMAND ----------

np.mean(df_Olimpicos_recentyear['Medal'])
np.median(df_Olimpicos_recentyear['Medal'])

# COMMAND ----------

df_Olimpicos_recentyear=df_Olimpicos[df_Olimpicos['Year'] == df_Olimpicos['Year'].max()]
df_Olimpicos_recentyear=df_Olimpicos_recentyear.dropna(subset=['Medal'])
df_Olimpicos_recentyear=df_Olimpicos_recentyear.groupby(['NOC'])['Medal'].count().sort_values(ascending=False).reset_index()
df_Olimpicos_recentyear['NOC_Resumed']=np.where(df_Olimpicos_recentyear['Medal']>np.mean(df_Olimpicos_recentyear['Medal']),df_Olimpicos_recentyear['NOC'],'Otros')
df_Olimpicos_recentyear=df_Olimpicos_recentyear.groupby(['NOC_Resumed'])['Medal'].sum().sort_values(ascending=False).reset_index()
df_Olimpicos_recentyear=df_Olimpicos_recentyear[df_Olimpicos_recentyear['NOC_Resumed'] != 'Otros']
df_Olimpicos_recentyear

# COMMAND ----------

explode_array=np.zeros(20)
explode_array[0]=.2
explode_array[1]=.1
explode_array[2]=.05
explode_array

# COMMAND ----------

mylabels=df_Olimpicos_recentyear['NOC_Resumed']
plt.pie(df_Olimpicos_recentyear['Medal'],labels=mylabels,explode=explode_array, shadow=True)
