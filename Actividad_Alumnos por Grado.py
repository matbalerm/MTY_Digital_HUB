# Databricks notebook source
# MAGIC %md #### Actividad Avanzada: Alumnos
# MAGIC 
# MAGIC Crea/Presenta  la forma que creas más conveniente para describir cuántos alumnos hay por grados, segmentanto por género, asignatura y grado.

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

grade_index=df[['Student ID','grade']].groupby('grade').count().reset_index()
new_index=[3,0,1,2]
grade_index=grade_index.reindex(new_index)

import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize=(10,4))
ax.bar(grade_index['grade'], grade_index['Student ID'],width=.4,color='lightsteelblue')
plt.xlabel("Grade",fontweight='bold')
plt.ylabel("No. of Students",fontweight='bold')

# COMMAND ----------

# Excelencia Académica

# Filtramos la base original con las máximas calificaciones en ambas asignaturas
df1=df[(df['reading_score'].max()==df['reading_score']) & (df['math_score'].max()==df['math_score'])]
#Contamos el número de estudiantes 
df1=df1.groupby(['school_name'])['student_name'].count().reset_index()
df1['total_students']=df.groupby(['school_name'])['student_name'].count()
df2=df1.sort_values(by=['student_name'],ascending=False)

name01=df2.iloc[0,0]
numb01=df2.iloc[0,1]
print(f'La escuela con más estudiantes de excelencia académica (máxima calificación en ambas asignaturas) es {name01} High School, con {numb01} alumnos.')

# COMMAND ----------

# Tabla con suma de alumnos por escuela y grado
df3=df.groupby(['school_name','grade'])['student_name'].count().reset_index()

#Tabla con suma de alumnos por escuela ordenados de mayor a menor
df4=df.groupby(['school_name'])['student_name'].count().reset_index().sort_values(by=['student_name'],ascending=False)

# Tabla original sólo Masculino
df10=df.where(df['gender']=='M')
df10=df10.dropna(subset='gender')
# Tabla con suma de estudiantes hombres por escuela y grado
df11=df10.groupby(['school_name'])['student_name'].count().reset_index().sort_values(by=['school_name'])

# Tabla original sólo Femenino
df20=df.where(df['gender']=='F')
df20=df20.dropna(subset='gender')
# Tabla con suma de estudiantes mujeres por escuela y grado
df21=df20.groupby(['school_name'])['student_name'].count().reset_index().sort_values(by=['school_name'])

x=list(df4['school_name'])
leg_name=list(df3['grade'].unique())

# COMMAND ----------

#Visualización de tablas
df21.head()

# COMMAND ----------

#Check para no dejar fuera ningún alumno
df11['student_name'].sum()+df21['student_name'].sum()-len(df)

# COMMAND ----------

# Método 1 para obtener el conteo de alumnos por escuela usando un for + concat sobre un DataFrame vacío
checklist=pd.DataFrame()
for x in df['school_name'].unique():
    df_temp=df.where(df['school_name']==x)
    df_temp=df_temp.dropna(subset='school_name')
    sum_school=df_temp.groupby(['school_name'])['student_name'].count()
    checklist = pd.concat([checklist, sum_school])
checklist.reset_index()

# COMMAND ----------

# Método 2 para obtener el conteo de alumnos por escuela usando un groupby
df[['Student ID','school_name']].groupby('school_name').count().reset_index()

# COMMAND ----------

df30=df[['school_name','reading_score','math_score']].groupby(['school_name']).mean().reset_index()
df30.sort_values(by=['school_name'])

# COMMAND ----------

df40=list(df[['reading_score']].mean())
df50=list(df[['math_score']].mean())

# COMMAND ----------

f, ax = plt.subplots(figsize=(25,12))
ax.bar(df11['school_name'], df11['student_name'],align='edge',width=.4,color='lightsteelblue',label='Men')
ax.bar(df21['school_name'], df21['student_name'], align='edge',width=-.4,color='mistyrose',label='Women')
ax.set_xticklabels(df4['school_name'].sort_values())
ax.legend(loc=9)
plt.xlabel("High School",fontweight='bold')
plt.ylabel("No. of Students",fontweight='bold')
ax2 = ax.twinx()
ax2.scatter(df30['school_name'], df30['reading_score'], color = 'crimson',marker='o',s=50,label='School Avg Reading Score')
ax2.hlines(y=df40,xmin=0,xmax=len(df['school_name'].unique())-1,linewidth=1, color='crimson',label=f'Total Avg Reading Score = {round(df40[0],2)}')

ax2.scatter(df30['school_name'], df30['math_score'], color = 'darkgreen',marker='d',s=50,label='School Avg Math Score')
ax2.hlines(y=df50,xmin=0,xmax=len(df['school_name'].unique())-1,linewidth=1, color='darkgreen',label=f'Total Avg Math Score = {round(df50[0],2)}')

ax2.set_ylim(70,100)
ax2.set_ylabel('Grade',fontweight='bold')
ax2.legend(loc=1)

plt.show()
