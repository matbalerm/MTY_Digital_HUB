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

# Excelencia Académica

# Filtramos la base original con las máximas calificaciones en ambas asignaturas
df1=df[(df['reading_score'].max()==df['reading_score'])]
df2=df[(df['reading_score'].min()==df['reading_score'])]

df3=df1.groupby(['school_name','gender'])['student_name'].count().reset_index()
df3=df3[df3['gender']=='M']
df4=df1.groupby(['school_name','gender'])['student_name'].count().reset_index()
df4=df4[df4['gender']=='F']

df5=df2.groupby(['school_name','gender'])['student_name'].count().reset_index()
df5=df5[df5['gender']=='M']
df6=df2.groupby(['school_name','gender'])['student_name'].count().reset_index()
df6=df6[df6['gender']=='F']

# COMMAND ----------

import matplotlib.pyplot as plt
f, ax = plt.subplots(1,2,figsize=(30,7))

ax[0].bar(df3['school_name'], df3['student_name'],align='edge',width=.4,color='lightsteelblue',label='Men')
ax[0].bar(df4['school_name'], df4['student_name'],align='edge',width=-.4,color='lavenderblush',label='Women')
ax[0].set_xticklabels(df3['school_name'].sort_values(),rotation=90)
ax[0].legend(loc='upper right')
ax[0].set_xlabel("High School",fontweight='bold')
ax[0].set_ylabel("No. of Students",fontweight='bold')
ax[0].set_title('Academic Excellence - Reading',fontweight='bold')

ax[1].bar(df5['school_name'], df5['student_name'],align='edge',width=.4,color='lightsteelblue',label='Men')
ax[1].bar(df6['school_name'], df6['student_name'],align='edge',width=-.4,color='lavenderblush',label='Women')
ax[1].set_xticklabels(df6['school_name'].sort_values())
ax[1].legend(loc='upper right')
ax[1].set_xlabel("High School",fontweight='bold')
ax[1].set_ylabel("No. of Students",fontweight='bold')
ax[1].set_title('Struggling Students - Reading',fontweight='bold')

plt.show()

# COMMAND ----------

#Validacion de Datos
h=df2.groupby(['school_name','gender'])['student_name'].count().reset_index()
h

# COMMAND ----------

#Validacion de Datos
k=df1.groupby(['school_name','gender'])['student_name'].count().reset_index()
k
