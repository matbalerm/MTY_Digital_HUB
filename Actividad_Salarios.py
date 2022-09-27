# Databricks notebook source
# MAGIC %md #### Actividad Básica
# MAGIC 
# MAGIC Obtener la diferencia entre el salario más alto y el más bajo.

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 14 - Salarios/2022_qna16_remuneraciones.csv'
df = pd.read_csv(path)
df.head()

# COMMAND ----------

df['FULLNAME']=df['NOMBRE']+' '+df['APELLIDO_1']+' '+df['APELLIDO_2']
salario0=df.loc[df['SUELDO_TABULAR_BRUTO'] == df['SUELDO_TABULAR_BRUTO'].min()]
salario1=df.loc[df['SUELDO_TABULAR_BRUTO'] == df['SUELDO_TABULAR_BRUTO'].max()]

# COMMAND ----------

num0=salario0.iloc[0,11]
nom0=salario0.iloc[0,14]
num1=salario1.iloc[0,11]
nom1=salario1.iloc[0,14]
if len(salario0)>1:
    print(f'Más de una persona comparte el sueldo más bajo, que es ${num0:,}.')
else:
    print(f'La persona con el salario más bajo es {nom0}, con un sueldo mensual de ${num0:,}.')
if len(salario1)>1:
    print(f'Más de una persona comparte el sueldo más bajo, que es ${num1:,}.')
else:
    print(f'La persona con el salario más bajo es {nom1}, con un sueldo mensual de ${num1:,}.')
# Determinando la diferencia de sueldos    
dif=num1-num0    
print(f'La diferencia entre el sueldo más alto y el más bajo es de ${dif:,}')

# COMMAND ----------

# MAGIC %md ####  Actividad Avanzada
# MAGIC 
# MAGIC Obtener los estadísticos descriptivos de los salarios. (media, mediana, desviación estándar, etc.

# COMMAND ----------

df1=df.drop(columns=['ID_TIPO_NOMINA','ID_NIVEL_SALARIAL'])
df1.describe()
