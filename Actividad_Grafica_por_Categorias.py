# Databricks notebook source
# MAGIC %md #### Actividad Básica
# MAGIC 
# MAGIC Crea / Presenta un algoritmo que genere los datos de "reading_score" y "math_score", en variables categóricas, y guárdalo en dos columnas diferentes (cada columna nueva representa la nueva columna con variables categórica).
# MAGIC 
# MAGIC Crea / Presenta una gráfica que condense la información obtenida ahora categóricamente.

# COMMAND ----------

import pandas as pd
import numpy as np
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

conditions_read=[
    df['reading_score']<60,
    (df['reading_score']>=60) & (df['reading_score']<df['reading_score'].mean()),
    (df['reading_score']>df['reading_score'].mean()) & (df['reading_score']<90),
    (df['reading_score']>=90) & (df['reading_score']<df['reading_score'].max()),
    df['reading_score']==df['reading_score'].max()
    ]
conditions_math=[
    df['math_score']<60,
    (df['math_score']>=60) & (df['math_score']<df['math_score'].mean()),
    (df['math_score']>df['math_score'].mean()) & (df['math_score']<90),
    (df['math_score']>=90) & (df['math_score']<df['math_score'].max()),
    df['math_score']==df['math_score'].max()
    ]
values=[
    'Failed',
    'Below Average',
    'Above Average',
    'Outstanding',
    'Academic Excellence'
    ]
df['cat_read']=np.select(conditions_read,values)
df['cat_math']=np.select(conditions_math,values)
df.head()

# COMMAND ----------

# Filtrar tabla
df1=df[df['gender']=='F'].reset_index()

df[df['gender']=='M']['reading_score'].mean()
df[df['gender']=='M']['math_score'].mean()

df2=df.groupby(['school_name','cat_read'])['student_name'].count().reset_index()

df3=df2[df2['cat_read']=='Failed'].reset_index()
df4=df2[df2['cat_read']=='Below Average'].reset_index()
df5=df2[df2['cat_read']=='Above Average'].reset_index()
df6=df2[df2['cat_read']=='Outstanding'].reset_index()
df7=df2[df2['cat_read']=='Academic Excellence'].reset_index()

df10=df.groupby(['school_name','cat_math'])['student_name'].count().reset_index()

df11=df10[df10['cat_math']=='Failed'].reset_index()
df12=df10[df10['cat_math']=='Below Average'].reset_index()
df13=df10[df10['cat_math']=='Above Average'].reset_index()
df14=df10[df10['cat_math']=='Outstanding'].reset_index()
df15=df10[df10['cat_math']=='Academic Excellence'].reset_index()

temp= {'index':[1]*8,'school_name':['Cabrera','Griffin','Holden','Pena','Shelton','Thomas','Wilson','Wright'],'cat_math':['Failed']*8,'student_name':[0]*8}
df11_temp = pd.DataFrame(data=temp)
df11=pd.concat([df11,df11_temp]).sort_values(by='school_name').reset_index()
df11

# COMMAND ----------

import matplotlib.pyplot as plt
f, ax = plt.subplots(1,2,figsize=(30,8))

ax[0].bar(df4['school_name'], df4['student_name'],width=.8,color='gold',label='Below Average')
ax[0].bar(df5['school_name'], df5['student_name'],width=.8,color='greenyellow',label='Above Average',bottom=df4['student_name'])
ax[0].bar(df6['school_name'], df6['student_name'],width=.8,color='yellowgreen',label='Outstanding',bottom=df4['student_name']+df5['student_name'])
ax[0].bar(df7['school_name'], df7['student_name'],width=.8,color='green',label='Academic Excellence',bottom=df4['student_name']+df5['student_name']+df6['student_name'])
ax[0].set_xticklabels(df4['school_name'].sort_values(),rotation=90)
ax[0].legend(loc='upper right')
ax[0].set_xlabel("High School",fontweight='bold')
ax[0].set_ylabel("No. of Students",fontweight='bold')
ax[0].set_title('Reading Score',fontweight='bold')

ax[1].bar(df11['school_name'], df11['student_name'],width=.8,color='crimson',label='Failed')
ax[1].bar(df12['school_name'], df12['student_name'],width=.8,color='gold',label='Below Average',bottom=df11['student_name'])
ax[1].bar(df13['school_name'], df13['student_name'],width=.8,color='greenyellow',label='Above Average',bottom=df11['student_name']+df12['student_name'])
ax[1].bar(df14['school_name'], df14['student_name'],width=.8,color='yellowgreen',label='Outstanding',bottom=df11['student_name']+df12['student_name']+df13['student_name'])
ax[1].bar(df15['school_name'], df15['student_name'],width=.8,color='green',label='Academic Excellence',bottom=df11['student_name']+df12['student_name']+df13['student_name']+df14['student_name'])
ax[1].set_xticklabels(df11['school_name'].sort_values(),rotation=90)
ax[1].legend(loc='upper right')
ax[1].set_xlabel("High School",fontweight='bold')
ax[1].set_ylabel("No. of Students",fontweight='bold')
ax[1].set_title('Math Score',fontweight='bold')

plt.show()
