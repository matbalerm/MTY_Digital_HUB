# Databricks notebook source
import numpy as np

# COMMAND ----------

x=np.arange(1,26)
x=np.resize(x,(5,5))
x

# COMMAND ----------

x[-2][0]

# COMMAND ----------

# MAGIC %md 1.- Crear una matriz 3x3 con valores de 0 a 8

# COMMAND ----------

y=np.arange(0,9)
y=np.resize(y,(3,3))
y

# COMMAND ----------

# MAGIC %md 2.- Crear una matriz identidad de 6x6

# COMMAND ----------

a=np.eye(6,6,dtype='int')
a
