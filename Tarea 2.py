# Databricks notebook source
x = 10
print("Identidad:", id(x))
print("Tipo:", type(x))
print("Value:", x)

# COMMAND ----------

# Mutables: Si permiten ser modificados una vez creados.
# Inmutables: Si no permiten ser modificados una vez creados.

# COMMAND ----------

# MAGIC %md # 1.- Crea una tupla con una longitud de 5. usando diferentes tipos de datos.

# COMMAND ----------

l = (1,"Colombia",[1,2,3],True,1.5)

# COMMAND ----------

type(l)

# COMMAND ----------

# MAGIC %md # 2.- Cambiar la tupla a lista

# COMMAND ----------

l=list(l)

# COMMAND ----------

l[1]="Argentina"

# COMMAND ----------

l

# COMMAND ----------

l[2][0]

# COMMAND ----------

d1=[1,2,3,4,5,6]
d2 = ['a','b','c']
d1 = {}
d3 = {}


# COMMAND ----------

for i in range(0,5):
    d1[i+1] = l[i]

d1

for i in range(len(d2)):
    d3[d2[i]] = l[i]

d3



# COMMAND ----------

d3['c']

# COMMAND ----------

# MAGIC %md # 3.- Crea un diccionario donde la clave sea del 1 al 5 y los elementos los datos de la lista

# COMMAND ----------

tarea1 = {}

# COMMAND ----------

for i in range(len(l)):
    tarea1[i+1]=l[i]
    
tarea1
