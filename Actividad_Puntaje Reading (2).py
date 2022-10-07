# Databricks notebook source
# MAGIC %md #### Actividad Básica: Puntaje Reading
# MAGIC 
# MAGIC Crea / Presenta la forma que creas más conveniente para describir cuántos alumnos por escuela tuvieron el mejor puntaje en "reading", y con ello saber que género es el que predomina en este filtro.
# MAGIC 
# MAGIC Crea / Presenta la forma que creas más conveniente para describir cuántos alumnos por escuela tuvieron el peor puntaje en "reading", y con ello saber que género es el que predomina en este filtro.

# COMMAND ----------

import pandas as pd
#Importando el archivo
path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
df= pd.read_csv(path)
#Limpiando la base
df=df.drop(columns='Unnamed: 0')
#Recortando el nombre de las escuelas dado que todas son 'High Schools'
new_school_name=df['school_name'].str.split()
new_school_name=[i[0] for i in new_school_name]
df['school_name']=new_school_name
#Mostrando tabla final
df.head()

# COMMAND ----------

df1 = df.groupby(['school_name','grade','gender'])['reading_score'].mean().reset_index()
df1 = df1.sort_values(['school_name', 'reading_score'],
              ascending = [True, False])
df1

# COMMAND ----------

df5 = df1.groupby(['school_name'])['reading_score'].transform(max) == df1['reading_score']
df1=df1[df5]
df1

# COMMAND ----------

import seaborn as sns
import matplotlib.pyplot as plt

ax=sns.scatterplot(data=df1, x='school_name', y='reading_score', hue='gender')
sns.set_theme()
ax.set_xlabel('High School')
ax.set_ylabel('Average Reading Score')
ax.set_title('Grade and Gender with Highest Average Score')
